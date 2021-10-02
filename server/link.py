
# TODO: include code in the javascript that returns the public_token
# to the backend so it can be converted to an access_token and stored
# in the database.

def get_link_html(user_id, link_token):
    return """
    <html>
    <head>
        <!-- <h1>Plaid API Demo</h1> -->
        <script src="https://cdn.plaid.com/link/v2/stable/link-initialize.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
    </head>
    <body>
        <script>
            const BASE_URL = "http://localhost:8000";

            const link_token = '""" + link_token + """';
            const user_id = '""" + str(user_id) + """';

            const handler = Plaid.create({
                token:  link_token,
                onSuccess: (public_token, metadata) => {
                    console.log("success", public_token, metadata);
                    // this.public_token = public_token;
                    let data = {
                        user_id: user_id,
                        public_token: public_token
                    };
                    axios.post(BASE_URL+'/link/store_token', data)
                        .then((resp) => {
                            console.log(resp);
                            // NAVIGATE
                            window.location.href = BASE_URL + '/link/done';
                    });
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

            open_plaid();
        </script>
    </body>
    </html>
    """

def get_done_html():
    return """
    <html>
        <h1>Your account has been linked!</h1>
        <p>The app will automatically detect that the process is complete
        and redirect you back to the accounts page.</p>
    </html>
    """