(function() {

    if (window.hasRun) {
        return;
    }
    window.hasRun = true;

    // Store the original fetch function in a variable
    const originalFetch = window.fetch;

    function extractMail(node) {
        let email = node.Items[0]
    
    
        return {
            email_id: email.ConversationId.Id,
            sender: {
                name: email.From.Mailbox.Name,
                email: email.From.Mailbox.EmailAddress,
            },
            to: email.ToRecipients.map(recipient => {
                return {
                    name: recipient.Name,
                    email: recipient.EmailAddress,
                }
            }),
            read: email.IsRead,
            is_draft: email.IsDraft,
            email_body_format: email.UniqueBody.BodyType,
            email_body_content: email.UniqueBody.Value,
            email_subject: email.Subject,
            received_date: email.DateTimeReceived
        }
    }
    
    
    function extractEmail(data) {
        const nodes = data[0].Conversation.ConversationNodes
        // Assuming the first item in the Items array is the target email
        
        // nextReplies: newLocal,

        const node = extractMail(nodes[0])
        if (nodes.length > 1) {
            node['replies'] = nodes.slice(1).map((node) => {  const {email_id, ...newLocal} = extractMail(node)
            return ({...newLocal,})})
        }else{
            
        node['replies'] = []
        }
        return node
    }

    // Override the window.fetch function
    window.emails = []
    window.scrolledEmails = []

    function getEmail(emailId) {
        return window.emails.find(email => email.email_id === emailId);
    }
    
    function getEmails(emailIds) {
        return emailIds.map(email_id => getEmail(email_id));
    }
    
    // Attach the functions to the window object
    window.getEmail = getEmail;
    window.getEmails = getEmails;
    
    window.fetch = async function(...args) {
        // Check if the URL contains 'ConversationItems'
        if (args[0].includes('service.svc?action=GetConversationItems')) {
            try {
                // Call the original fetch function
                const response = await originalFetch.apply(this, args);

                // Clone the response to not interfere with the original processing
                const clonedResponse = response.clone();

                // Read the response as JSON and log it
                clonedResponse.json().then(json => {

                    const data = extractEmail(json['Body']['ResponseMessages']['Items'])
                    window.emails = [...window.emails, data] 
                    // delete
                    console.log('Captured JSON for URL containing ConversationItems:', data);
                });

                // Return the original response
                return response;
            } catch (error) {
                console.error('Error in fetch interceptor:', error);
                throw error; // Re-throw the error for proper error handling
            }
        } 
        else {
            // Call the original fetch function for other URLs
            return originalFetch.apply(this, args);
        }
    };
})();
