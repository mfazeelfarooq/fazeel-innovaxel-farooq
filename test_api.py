import requests
import json

BASE_URL = "http://localhost:5000"

def test_create_url():
    print("\n1. Testing Create URL (POST)")
    data = {
        "url": "https://www.example.com/some/long/url"
    }
    response = requests.post(f"{BASE_URL}/shorten", json=data)
    print(f"Status Code: {response.status_code}")
    print("Response:", json.dumps(response.json(), indent=2))
    return response.json()["short_code"]

def test_get_url(short_code):
    print("\n2. Testing Get URL (GET)")
    response = requests.get(f"{BASE_URL}/shorten/{short_code}")
    print(f"Status Code: {response.status_code}")
    print("Response:", json.dumps(response.json(), indent=2))

def test_update_url(short_code):
    print("\n3. Testing Update URL (PUT)")
    data = {
        "url": "https://www.example.com/some/updated/url"
    }
    response = requests.put(f"{BASE_URL}/shorten/{short_code}", json=data)
    print(f"Status Code: {response.status_code}")
    print("Response:", json.dumps(response.json(), indent=2))

def test_get_stats(short_code):
    print("\n4. Testing Get Stats (GET)")
    response = requests.get(f"{BASE_URL}/shorten/{short_code}/stats")
    print(f"Status Code: {response.status_code}")
    print("Response:", json.dumps(response.json(), indent=2))

def test_delete_url(short_code):
    print("\n5. Testing Delete URL (DELETE)")
    response = requests.delete(f"{BASE_URL}/shorten/{short_code}")
    print(f"Status Code: {response.status_code}")
    if response.status_code == 204:
        print("URL successfully deleted")

def test_list_urls():
    print("\n6. Testing List URLs (GET)")
    response = requests.get(f"{BASE_URL}/shorten")
    print(f"Status Code: {response.status_code}")
    print("Response:", json.dumps(response.json(), indent=2))

def main():
    print("Starting URL Shortener API Tests...")
    
    try:
        # Test Create URL
        short_code = test_create_url()
        
        # Test Get URL
        test_get_url(short_code)
        
        # Test Update URL
        test_update_url(short_code)
        
        # Test Get Stats
        test_get_stats(short_code)
        
        # Test List URLs
        test_list_urls()
        
        # Test Delete URL
        test_delete_url(short_code)
        
        print("\nAll tests completed successfully!")
    except requests.exceptions.ConnectionError:
        print("\nError: Could not connect to the server. Make sure the Flask application is running on http://localhost:5000")
    except Exception as e:
        print(f"\nError during testing: {str(e)}")

if __name__ == "__main__":
    main() 