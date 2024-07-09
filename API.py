import requests

def test_kurtosys_api():
    # URL to test
    url = "https://www.kurtosys.com"
    
    # Send a GET request and measure the time taken
    response = requests.get(url)
    
    # Assertion: Check if the response status code is 200
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    
    # Assertion: Check if the response time is less than 2 seconds
    assert response.elapsed.total_seconds() < 2, f"Response time {response.elapsed.total_seconds()} seconds exceeds 2 seconds"
    
    # Assertion: Check if the server header contains 'Cloudflare'
    server_header = response.headers.get('Server', '')
    assert 'Cloudflare' in server_header, f"Expected 'Cloudflare' in Server header, but got {server_header}"
    
    print("API Test passed successfully.")

# Execute the test function
test_kurtosys_api()
