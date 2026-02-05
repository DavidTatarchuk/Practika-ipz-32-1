import requests

# GET-запит
url_get = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url_get)

print("--- GET REQUEST ---")
print(f"Status Code: {response.status_code}")
print("Headers:")
for key, value in response.headers.items():
    print(f"{key}: {value}")
print(f"\nBody: {response.text}")

# POST-запит
url_post = "https://jsonplaceholder.typicode.com/posts"
data = {"title": "foo", "body": "bar", "userId": 1}
response_post = requests.post(url_post, json=data)

print("\n--- POST REQUEST ---")
print(f"Status Code: {response_post.status_code}")
print(f"Response Body: {response_post.json()}")