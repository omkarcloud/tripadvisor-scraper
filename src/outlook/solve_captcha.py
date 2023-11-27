import capsolver

def solve_captcha(websitePublicKey, websiteURL, funcaptchaApiJSSubdomain, blob_data, useragent, proxy):
        # Read https://www.capsolver.com/blog/FunCaptcha/funcaptcha-data-blob to learn about blob_data

        capsolver.api_key = "YOUR_API_KEY" # Add Your Capsolver API key here
        if proxy:
                data = {
                        "type":"FunCaptchaTask",
                        "websitePublicKey":  websitePublicKey,
                        "websiteURL": websiteURL,
                        "funcaptchaApiJSSubdomain": funcaptchaApiJSSubdomain ,
                        "data": blob_data,
                        'userAgent': useragent,
                        "proxy": proxy,
                }
        else:
                data = {
                        "type":"FunCaptchaTaskProxyLess", 
                        "websitePublicKey":  websitePublicKey,
                        "websiteURL": websiteURL,
                        "funcaptchaApiJSSubdomain": funcaptchaApiJSSubdomain,
                        "data": blob_data,
                        'userAgent': useragent,
                }

        print(data)
        solution = capsolver.solve(data)
        
        token = solution['token']
        print(solution)
        return token
