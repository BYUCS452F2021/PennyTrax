
# TODO: include code in the javascript that returns the public_token
# to the backend so it can be converted to an access_token and stored
# in the database.

def get_html(link_token):
    return """
    <html>
    <head>
        <h1>Plaid API Demo</h1>
        <script src="https://cdn.plaid.com/link/v2/stable/link-initialize.js"></script>
    </head>
    <body>
        <button onclick="open_plaid()">Open Plaid Link</button>
        <script>
            const handler = Plaid.create({
                token: '""" + link_token + """',
                onSuccess: (public_token, metadata) => {
                    console.log("success", public_token, metadata);
                    this.public_token = public_token;
                },
                onLoad: () => {
                    console.log("load");
                },
                onExit: (err, metadata) => {
                    console.log("exit", err);
                },
                onEvent: (eventName, metadata) => {
                    console.log("event", eventName);
                },
                receivedRedirectUri: null,
                });

            function open_plaid() {
                console.log("opening plaid");
                handler.open();
            }
        </script>
    </body>
    </html>
    """