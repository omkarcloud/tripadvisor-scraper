/**
 * @typedef {import('../../frontend/node_modules/botasaurus-controls/dist/index').Controls} Controls
 */
function isEmpty(x) {
    return (
        x === null || x === undefined || (typeof x == "string" && x.trim() === "")
    )
}

function isNotEmpty(x) {
    return !isEmpty(x)
}

/**
 * @param {Controls} controls
 */
function getInput(controls) {
    const validUrls = [
        "new york",
    ]

    controls
        .choose('type', {
            options: [
                {
                    label: 'Hotel',
                    value: "hotel",
                },
                {
                    label: 'Restaurant',
                    value: "restaurant",
                },

            ],
            isRequired:true,
            defaultValue: "hotel",
        })
        .listOfTexts('search_queries', {
            isRequired: true,
            placeholder: "New York",
            defaultValue: [
                "New York",
            ]
        })
        .numberGreaterThanOrEqualToOne('max_results', {
            placeholder: 30,
            defaultValue: 30,
            label: 'Max Results (Leave empty to extract all places)'
        })
        .text('api_key', {
            placeholder: "2e5d346ap4db8mce4fj7fc112s9h26s61e1192b6a526af51n9",
            label: 'Rapid API Key',
            helpText: 'Enter your Rapid API key to extract tripadvisor listings.',
            validate: (x, data) => {
                if (isEmpty(x)) {
                    const ls = data['search_queries'].filter(isNotEmpty)

                    if (ls.length && !ls.every(query => validUrls.includes(query.trim().toLowerCase()))) {
                        return 'To get different listings, please enter your Rapid API Key. You can use the starter plan, which offers a 200 monthly requests.'
                    }
                } 

            }
        })
        .switch('enable_detailed_extraction', {
            label: "Enable Detailed Extraction to obtain more information such as Website, Email, and Phone Number, please note that Detailed Extraction is more time intensive.", defaultValue: true,
        })
}
