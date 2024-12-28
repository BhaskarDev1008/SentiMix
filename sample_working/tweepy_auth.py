import tweepy

# Replace these with your own credentials
api_key = "FGnwM8TDNH3o5L3FcM4NpT2mO"
api_secret = "4IrzBaoJfFjQhO9Kl7dp6w9JKYPqd0OBioOoxM2xoWGNI2dXgf"
access_token = "1872951621828878336-FnSDt9AhXf54uT1P1yLWp6IfVzIVBr"
access_token_secret = "owGhUuHsxtnXb1uGCWt6loyfqPKsl1qqgULEeto2rQdcx"

# Authenticate with Twitter
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

# Test authentication
try:
    api.verify_credentials()
    print("Authentication successful!")
except tweepy.TweepError as e:
    print(f"Authentication failed: {e}")
