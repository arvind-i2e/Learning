# import requests
# import time

# BEARER_TOKEN = "Your bearer token"  # Replace with your actual Bearer Token

# def get_user_id(username):
#     url = f"https://api.twitter.com/2/users/by/username/{username}"
#     headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
#     while True:
#         response = requests.get(url, headers=headers)
#         if response.status_code == 200:
#             user_data = response.json()
#             return user_data["data"]["id"]
#         elif response.status_code == 429:
#             retry_after = int(response.headers.get("x-rate-limit-reset", time.time())) - int(time.time())
#             print(f"Rate limit exceeded. Retrying in {max(retry_after, 1)} seconds...")
#             time.sleep(max(retry_after, 1))
#         else:
#             print(f"Error: {response.status_code}, {response.json()}")
#             return None

# def get_user_tweets(user_id, max_results=10):
#     url = f"https://api.twitter.com/2/users/{user_id}/tweets"
#     headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
#     params = {
#         "max_results": max_results,
#         "tweet.fields": "created_at,text"
#     }
#     while True:
#         response = requests.get(url, headers=headers, params=params)
#         if response.status_code == 200:
#             return response.json()
#         elif response.status_code == 429:
#             retry_after = int(response.headers.get("x-rate-limit-reset", time.time())) - int(time.time())
#             print(f"Rate limit exceeded. Retrying in {max(retry_after, 1)} seconds...")
#             time.sleep(max(retry_after, 1))
#         else:
#             print(f"Error: {response.status_code}, {response.json()}")
#             return None

# username = "matthewherper"
# user_id = get_user_id(username)
# if user_id:
#     print(f"User ID: {user_id}")
#     tweets = get_user_tweets(user_id, max_results=5)
#     if tweets:
#         with open("tweets.txt", "w", encoding="utf-8") as file:
#             for tweet in tweets["data"]:
#                 tweet_content = f"Time: {tweet['created_at']}\nTweet: {tweet['text']}\n\n"
#                 file.write(tweet_content)
#         print("Tweets have been saved to tweets.txt")

import requests
import time

BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAKKTyQEAAAAAZZr%2F331DoMMrqS1dsa%2F289WjPZk%3DUWvBNXzaWp2ZdcINDIrqhlnEwjVNiZtOEedyTYqxGnVZYtPIh0"  # Replace with your actual Bearer Token

def get_user_id(username):
    url = f"https://api.twitter.com/2/users/by/username/{username}"
    headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
    while True:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            user_data = response.json()
            return user_data["data"]["id"]
        elif response.status_code == 429:
            retry_after = int(response.headers.get("x-rate-limit-reset", time.time())) - int(time.time())
            print(f"Rate limit exceeded. Retrying in {max(retry_after, 1)} seconds...")
            time.sleep(max(retry_after, 1))
        else:
            print(f"Error: {response.status_code}, {response.json()}")
            return None

def get_user_tweets(user_id, max_results=10):
    url = f"https://api.twitter.com/2/users/{user_id}/tweets"
    headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
    params = {
        "max_results": max_results,
        "tweet.fields": "created_at,text"
    }
    while True:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 429:
            retry_after = int(response.headers.get("x-rate-limit-reset", time.time())) - int(time.time())
            print(f"Rate limit exceeded. Retrying in {max(retry_after, 1)} seconds...")
            time.sleep(max(retry_after, 1))
        else:
            print(f"Error: {response.status_code}, {response.json()}")
            return None

def is_medical_tweet(text):
    medical_keywords = ["health", "medicine", "disease", "treatment", "vaccine", "doctor", "hospital", "patient","research"]
    return any(keyword.lower() in text.lower() for keyword in medical_keywords)

usernames = ["matthewherper"]

for username in usernames:
    user_id = get_user_id(username)
    if user_id:
        print(f"Fetching tweets for {username} (User ID: {user_id})")
        tweets = get_user_tweets(user_id, max_results=10)
        if tweets:
            filename = f"{username}_medical_tweets.txt"
            with open(filename, "w", encoding="utf-8") as file:
                for tweet in tweets["data"]:
                    if is_medical_tweet(tweet["text"]):
                        tweet_content = f"Time: {tweet['created_at']}\nTweet: {tweet['text']}\n\n"
                        file.write(tweet_content)
            print(f"Medical-related tweets for {username} have been saved to {filename}")
        else:
            print(f"No tweets found for {username}")
    else:
        print(f"Could not fetch User ID for {username}")

