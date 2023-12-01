(function () {

    if (window.hasRun) {
        return
    }
    window.hasRun = true

    // Store the original fetch function in a variable
    const originalFetch = window.fetch

    function extractAttachments(email) {
        return (email.Attachments ?? []).filter(attachment => !attachment.IsInline).map(({
            AttachmentId, Name, ContentType, ContentId, Size, LastModifiedTime,
        }) => {
    
            return {
                attachment_id: AttachmentId.Id,
                name: Name,
                content_id: ContentId,
                content_type: ContentType,
                size: Size,
                last_modified_time: LastModifiedTime,
            }
    
    
        })
    }
    
    
    function extractMailContent(node) {
        let email = node
        let attachments = extractAttachments(email)
        let bdy = email.UniqueBody ?? email.NormalizedBody 
        return {
            "attachments": attachments,
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
            email_body_format: bdy.BodyType,
            email_body_content: bdy.Value,
            email_subject: email.Subject,
            received_date: email.DateTimeReceived
        }
    }


    function extractNormalEmail(data) {

        try {
            
        const nodes = data[0].Conversation.ConversationNodes
        // Assuming the first item in the Items array is the target email

        // nextReplies: newLocal,

        const node = extractMailContent(nodes[0].Items[0])
        if (nodes.length > 1) {
            node['replies'] = nodes.slice(1).map((node) => {
                const { email_id, ...newLocal } = extractMailContent(node.Items[0])
                return ({ ...newLocal, })
            })
        } else {

            node['replies'] = []
        }
        return node
        } catch (error) {
            console.error(error)
            console.log(data)
        }
    }

    

    function extractJunkEmail(data) {
        const x= extractMailContent(data[0].Items[0])
        x['replies'] = []
        return x
    }

    // Override the window.fetch function
    window.emails = []
    window.scrolledEmails = []

    function getEmail(emailId) {
        return window.emails.find(email => email.email_id === emailId)
    }

    function getEmails(emailIds) {
        return emailIds.map(email_id => getEmail(email_id))
    }

    // Attach the functions to the window object
    window.getEmail = getEmail
    window.getEmails = getEmails

    window.fetch = async function (...args) {
        const isConv = args[0].includes('service.svc?action=GetConversationItems')
        const isJunkConv = args[0].includes('service.svc?action=GetItem')
        // const isJunkFindConv = args[0].includes('service.svc?action=FindItem')
        
        
        // Check if the URL contains 'ConversationItems'
        if (isConv||isJunkConv
            // ||isJunkFindConv
            ) {
            // console.log('Intercepted fetch call for URL containing ConversationItems:', args[0])
            try {
                // Call the original fetch function
                const response = await originalFetch.apply(this, args)

                // Clone the response to not interfere with the original processing
                const clonedResponse = response.clone()

                // Read the response as JSON and log it
                clonedResponse.json().then(json => {
                    if(isJunkConv) {
                        const data = extractJunkEmail(json['Body']['ResponseMessages']['Items'])
                                            
                        if (data){
                            window.emails = [...window.emails, data]
                        }

                    }else {
                        const data = extractNormalEmail(json['Body']['ResponseMessages']['Items'])
                    
                    
                        if (data){
                            window.emails = [...window.emails, data]
                        }
                    }

                })

                // Return the original response
                return response
            } catch (error) {
                console.error('Error in fetch interceptor:', error)
                throw error // Re-throw the error for proper error handling
            }
        }
        else {
            // Call the original fetch function for other URLs
            return originalFetch.apply(this, args)
        }
    }


    
})()