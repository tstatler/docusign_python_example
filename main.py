import base64, os
import docusign_esign as docusign
from docusign_esign import EnvelopesApi
import argparse

base_path = 'https://demo.docusign.net/restapi'

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--access_token', required=True)
    parser.add_argument('--account_id', required=True)
    parser.add_argument('--envelope_id', required=True)
    args = parser.parse_args()

    api_client = docusign.ApiClient()
    api_client.host = base_path
    api_client.set_default_header("Authorization", "Bearer " + args.access_token)

    envelope_api = EnvelopesApi(api_client)
    results = envelope_api.get_envelope(args.account_id, args.envelope_id)
    print("\nFetching info for envelope with ID: " + args.envelope_id + '\n')
    print(results)

if __name__ == "__main__":
    main()