import requests

class RestClient:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip('/')

    def get(self, endpoint):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        try:
            response = requests.get(url)
            response.raise_for_status()  # перевірка на помилки HTTP
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error: {e} (Status code: {response.status_code})")
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
        return None

    def post(self, endpoint, data):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        try:
            response = requests.post(url, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error: {e} (Status code: {response.status_code})")
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
        return None


# --- ПРИКЛАД ВИКОРИСТАННЯ ---
if __name__ == "__main__":
    client = RestClient("https://jsonplaceholder.typicode.com")

    # --- GET: отримати список постів ---
    posts = client.get("/posts")
    print("Перші 3 пости GET:")
    for post in posts[:3]:
        print(post)

    # --- GET: отримати один пост ---
    post1 = client.get("/posts/1")
    print("\nПост #1:")
    print(post1)

    # --- POST: створити новий пост ---
    new_post_data = {
        "title": "Test Post",
        "body": "This is a test post from RestClient",
        "userId": 123
    }
    new_post = client.post("/posts", new_post_data)
    print("\nРезультат POST:")
    print(new_post)