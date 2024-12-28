import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load the cleaned tweet data
df = pd.read_csv('cleaned_sentimix_tweets.csv')

# Initialize VADER Sentiment Intensity Analyzer
analyzer = SentimentIntensityAnalyzer()

# Function to get sentiment score as numeric values
def get_sentiment_score(text):
    score = analyzer.polarity_scores(text)
    if score['compound'] >= 0.05:
        return 1  # Positive
    elif score['compound'] <= -0.05:
        return -1  # Negative
    else:
        return 0  # Neutral

# Apply VADER to the tweet text and create a new column for sentiment
df['sentiment'] = df['cleaned_text'].apply(get_sentiment_score)

# Save the updated DataFrame with numeric sentiment scores
df.to_csv('sentimix_tweets_with_vader_numeric.csv', index=False)

print("Sentiment analysis complete and saved to 'sentimix_tweets_with_vader_numeric.csv'")
