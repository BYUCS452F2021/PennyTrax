import requests

STANDARD_HEADERS = {
    "Content-Type": "application/json",
    "PLAID-CLIENT-ID": "6144e705f66e290010c5865a",
    "PLAID-SECRET": "6677bf5a23ac8e20f2bc08aae42e18" # (Sandbox)
}

PLAID_LINK_URL = "https://sandbox.plaid.com/link/token/create"

# curl https://sandbox.plaid.com/link/token/create -H "Content-Type: application/json" -H "PLAID-CLIENT-ID: 6144e705f66e290010c5865a" -H "PLAID-SECRET: 6677bf5a23ac8e20f2bc08aae42e18" -d '{"client_name": "pennytrax-demo", "language": "en", "country_codes": ["US"], "user": { "client_user_id": "johnny"}, "products": ["transactions"]}'

def get_link_token(user):
    data = {
        "client_name": "pennytrax-DEV", # We will change this when the app is done.
        "language": "en",
        "country_codes": ["US"],
        "user": { "client_user_id": user},
        "products": ["transactions"]
    }
    r = requests.post(PLAID_LINK_URL, headers=STANDARD_HEADERS, json=data)
    resp = r.json()
    print(resp)
    return resp['link_token']