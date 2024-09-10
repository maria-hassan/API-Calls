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


def Post(title,body):
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        response = requests.post(url, json={'title': title, 'body':body,'userID':1})
        if response.status_code == 201:
            post_data = response.json()
            return post_data
        else:
            print("Error", response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("Failed to call an API", e)
        return None


def main():
    posts = get()
    if posts:
        print("Existing Posts:")
        print("Title:", posts[0]['title'])
        print("Body:", posts[0]['body'])

    new_post=Post("My new post","This is the body of new post")
    if new_post:
        print("New Post Created")
        print("Title",new_post['title'])
        print("Body",new_post['body'])
        print("UserID",new_post['id'])



    else:
        print("Failed to fetch")


if __name__ == '__main__':
    main()
