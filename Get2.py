import requests


def get():
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            posts = response.json()
            return posts
        else:
            print("Error", response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("Failed to call an API", e)
        return None


def main():
    posts = get()
    if posts:
        print("Title:", posts[0]['title'])
        print("Body:", posts[0]['body'])
    else:
        print("Failed to fetch")


if __name__ == '__main__':
    main()
