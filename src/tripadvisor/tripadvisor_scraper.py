from .get_listings import get_listings


def remove_duplicates_by_key(dict_list, key):
    """
    Removes duplicates from a list of dictionaries based on a specified key.
    
    :param dict_list: List of dictionaries from which duplicates will be removed.
    :param key: The key based on which duplicates are identified and removed.
    :return: A list of dictionaries with duplicates removed.
    """
    seen = set()
    new_dict_list = []
    for d in dict_list:
        if key in d:
            if d[key] not in seen:
                seen.add(d[key])
                new_dict_list.append(d)
        else: 
            new_dict_list.append(d)
    return new_dict_list

def perform_query(search_query, max_results, api_key, enable_detailed_extraction, endpoint) :
        metadata = {"key": api_key}
        output = []
        page = 1
        total_pages = None
        seen = set()

        while True:
            result = get_listings({"endpoint": f"/{endpoint}/list", "query": search_query, "page": str(page)}, metadata=metadata)
            
            has_error = result.get('error')            
            if result is None:
                return [{"error": 'No Results for this query'}]
            if has_error:
                if output:
                    return [*output, {"id": result['error']}]
                return [{"error": result['error']}]
            result = result['data']
            items = result['results']
            
            if enable_detailed_extraction:
                items = [{"endpoint": f"/{endpoint}/detail", "id": product["id"]} for product in items]
                if max_results is not None:
                    items = items [:max_results - len(seen)]
                
                items = get_listings(items, metadata=metadata)
                has_seen_error = False
                for item in items:
                    if item is None:
                        output.append({"id": 'No Results for this query'})
                        has_seen_error = True
                    elif item.get('error'):
                        output.append({"id": item['error']})
                        has_seen_error = True
                    else:
                        x = item['data']
                        if x['id'] not in seen:
                            output.append(x)
                            seen.add(x['id'])
                        if max_results is not None and len(seen) >= max_results:
                            return output[:max_results]

                if has_seen_error:
                    return output
            else:
                for x in items:
                    if x['id'] not in seen:
                        output.append(x)
                        seen.add(x['id'])

            if total_pages is None:
                total_pages = result['total_pages']
            
            if max_results is not None and len(seen) >= max_results:
                return output[:max_results]

            if result['current_page'] >= total_pages:
                return output
            
            page += 1

class Tripadvisor:
    @staticmethod
    def get_restaurants(search_query, max_results, api_key, enable_detailed_extraction):
        return remove_duplicates_by_key(perform_query(search_query, max_results, api_key, enable_detailed_extraction, "restaurants"), "id")
    @staticmethod
    def get_hotels(search_query, max_results, api_key, enable_detailed_extraction) :
        return remove_duplicates_by_key(perform_query(search_query, max_results, api_key, enable_detailed_extraction, "hotels"), "id")
