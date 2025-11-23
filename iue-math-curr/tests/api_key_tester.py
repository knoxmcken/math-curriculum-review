import os
import sys
import json
import requests
from dotenv import load_dotenv

def test_api_key(key_name, url, headers, payload_template):
    """
    A general function to test an API key.

    Args:
        key_name (str): The name of the environment variable for the API key.
        url (str): The API endpoint to hit.
        headers (dict): The request headers.
        payload_template (dict): A template for the request payload. 
                                 The API key will be injected into this.
    """
    print(f"--- Testing {key_name} ---")
    
    # Load environment variables from .env file
    load_dotenv()
    
    # Get the API key from environment variables
    api_key = os.getenv(key_name)
    
    if not api_key:
        print(f"SKIPPED: {key_name} not found in .env file or environment variables.")
        return

    # Prepare payload
    payload = payload_template.copy()
    # Find where to inject the API key in the payload, if at all
    for key, value in payload.items():
        if isinstance(value, str) and value == "__API_KEY__":
            payload[key] = api_key
            
    # Also check headers for API key placeholder
    current_headers = headers.copy()
    for key, value in current_headers.items():
        if isinstance(value, str) and value == "__API_KEY__":
            current_headers[key] = api_key
            
    print(f"URL: {url}")
    print(f"Headers: {current_headers}")
    print(f"Payload: {json.dumps(payload)}")

    try:
        # Make the POST request
        response = requests.post(url, headers=current_headers, data=json.dumps(payload), timeout=10)
        
        # Check the response status code
        if response.status_code == 200:
            print(f"✅ Success! Your {key_name} is valid.")
            print("Response snippet:", response.text[:150])
        elif response.status_code in [401, 403]:
            print(f"❌ Failure! Your {key_name} is invalid or has been revoked.")
            print("Response:", response.text)
        else:
            print(f"⚠️ Warning! Received unexpected status code: {response.status_code}")
            print("Response:", response.text)
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Failure! An error occurred while making the request: {e}")
    finally:
        print("-" * (len(key_name) + 12))

def test_serper_api():
    """Tests the SERPER_API_KEY."""
    test_api_key(
        key_name="SERPER_API_KEY",
        url="https://google.serper.dev/search",
        headers={
            "X-API-KEY": "__API_KEY__",
            "Content-Type": "application/json"
        },
        payload_template={"q": "test"}
    )

def test_tavily_api():
    """Tests the TAVILY_API_KEY."""
    test_api_key(
        key_name="TAVILY_API_KEY",
        url="https://api.tavily.com/search",
        headers={"Content-Type": "application/json"},
        payload_template={
            "api_key": "__API_KEY__",
            "query": "test"
        }
    )

def main():
    """Main function to select which API key to test."""
    if len(sys.argv) > 1:
        api_to_test = sys.argv[1].lower()
        if api_to_test == 'serper':
            test_serper_api()
        elif api_to_test == 'tavily':
            test_tavily_api()
        else:
            print(f"Error: Unknown API '{api_to_test}'. Please choose 'serper' or 'tavily'.")
    else:
        print("Testing all available API keys...\n")
        test_serper_api()
        print()
        test_tavily_api()

if __name__ == "__main__":
    main()