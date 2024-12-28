import pandas as pd
import re

# Load the collected tweets
df = pd.read_csv(r"C:\Users\Bhask\OneDrive\Desktop\SentiMix\Tweepy\sentimix_tweets.csv")

# Data cleaning: Remove URLs, mentions, and special characters
def clean_text(text):
    text = re.sub(r'http\S+', '', text)  # Remove URLs
    text = re.sub(r'@\w+', '', text)  # Remove mentions
    text = re.sub(r'\n', ' ', text)  # Remove newline characters
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    return text.lower()  # Convert to lowercase

# Apply cleaning function to the text column
df['cleaned_text'] = df['text'].apply(clean_text)

# Save cleaned data to a new CSV file
df.to_csv(r"C:\Users\Bhask\OneDrive\Desktop\SentiMix\Tweepy\cleaned_sentimix_tweets.csv", index=False)

print("Data cleaned and saved to cleaned_sentimix_tweets.csv")
