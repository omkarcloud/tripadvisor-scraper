return (function () {

    function process(r) {
        window.blb = JSON.parse(r?.rsp?.error?.data)?.arkoseBlob
    }
    // Store the original $PageHelper.ajax function in a variable
    var originalAjax = $PageHelper.ajax;
    
    // Override the $PageHelper.ajax function with your custom function
    $PageHelper.ajax = function(options) {
        // Check if the URL contains 'createAccount?lic=1'
        if (options.url.includes('CreateAccount')) {
            // Store the original success function
            return originalAjax(options).then(r=>{
                process(r) 
    
                $PageHelper.ajax = originalAjax;      
                return r
            })
        }
    
        // Call the original $PageHelper.ajax function with the (possibly modified) options
        return originalAjax(options)
    };
})()
 