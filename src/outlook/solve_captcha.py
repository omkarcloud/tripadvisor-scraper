import capsolver

def solve_captcha(websitePublicKey, websiteURL, funcaptchaApiJSSubdomain, blob_data, useragent, proxy, capsolver_apikey):
        # Read https://www.capsolver.com/blog/FunCaptcha/funcaptcha-data-blob to learn about blob_data

        capsolver.api_key = capsolver_apikey # Add Your Capsolver API key here
        data = {
                        "type":"FunCaptchaTaskProxyLess", 
                        "websitePublicKey":  websitePublicKey,
                        "websiteURL": websiteURL,
                        "funcaptchaApiJSSubdomain": funcaptchaApiJSSubdomain,
                        "data": blob_data,
                        'userAgent': useragent,
                }
        
        #print("data", data)
        solution = capsolver.solve(data)
        
        token = solution['token']
        #print("solution",solution)
        print("Captha Solved")
        return token
