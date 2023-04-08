import tweepy

# Get the consumer key and secret key from the user
consumer_key = input("Enter consumer key: ")
consumer_secret = input("Enter consumer secret: ")

# Get the access token and secret from the user
access_token = input("Enter access token: ")
access_token_secret = input("Enter access token secret: ")

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Get the authenticated user's information
user = user = api.verify_credentials()

# Print user's information
print("Username:", user.screen_name)
print("Name:", user.name)
print("Location:", user.location)
print("Description:", user.description)
print("Followers:", user.followers_count)
print("Friends:", user.friends_count)
print("Listed:", user.listed_count)
print("Favorites:", user.favourites_count)
print("Statuses:", user.statuses_count)

try:
    # Make a tweet
    cuitan = input("masukan cuitan anda: ")
    api.update_status(cuitan)
    print("Cuitan berhasil diterbitkan!")
except Exception as e:
    # Print an error message
    print("Maaf, tidak bisa membuat cuitan. Error: ", e)
