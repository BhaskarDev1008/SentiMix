import pandas as pd
import tweepy
import tkinter as tk
from tkinter import messagebox
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Set up your Twitter API credentials
bearer_token = 'Enter_your_bearer_token'

# Authenticate with Twitter API
client = tweepy.Client(bearer_token=bearer_token)

# Initialize VADER Sentiment Intensity Analyzer
analyzer = SentimentIntensityAnalyzer()

# Function to fetch tweets and analyze sentiment
def fetch_tweets_and_analyze():
    search_query = entry.get()  # Get the keyword from the input field
    
    if not search_query:
        messagebox.showerror("Input Error", "Please enter a keyword.")
        return

    try:
        # Fetch 25 recent tweets based on the keyword
        tweets = client.search_recent_tweets(query=search_query, max_results=25)
        
        # Initialize an empty list to store tweet data
        tweet_data = []

        # Loop through the fetched tweets and extract the text
        for tweet in tweets.data:
            tweet_data.append({'tweet_text': tweet.text})

        # Convert the list of tweet data into a DataFrame
        df = pd.DataFrame(tweet_data)

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
        df['sentiment'] = df['tweet_text'].apply(get_sentiment_score)

        # Save the DataFrame with sentiment analysis results to a CSV file
        df.to_csv('sentimix_tweets_with_vader_numeric.csv', index=False)

        # Display success message
        messagebox.showinfo("Success", f"Successfully fetched 25 tweets for '{search_query}' and saved sentiment analysis to 'sentimix_tweets_with_vader_numeric.csv'")

        # Create visualizations (Pie chart, Bar graph, and Word Cloud)
        create_visualizations(df)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to create visualizations (Pie chart, Bar graph, Word Cloud)
def create_visualizations(df):
    # Pie Chart for sentiment distribution
    sentiment_counts = df['sentiment'].value_counts()
    sentiment_labels = {1: 'Positive', 0: 'Neutral', -1: 'Negative'}
    sentiment_counts.index = sentiment_counts.index.map(sentiment_labels)

    plt.figure(figsize=(6, 6))
    sentiment_counts.plot(kind='pie', autopct='%1.1f%%', colors=['#66b3ff', '#99ff99', '#ff9999'], startangle=90)
    plt.title('Sentiment Distribution')
    plt.ylabel('')  # Hide the y-label
    plt.show()

    # Bar Graph for sentiment counts
    sentiment_counts.plot(kind='bar', color=['#66b3ff', '#99ff99', '#ff9999'])
    plt.title('Sentiment Count')
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.xticks(rotation=0)
    plt.show()

    # Word Cloud for tweet text
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(df['tweet_text']))
    plt.figure(figsize=(8, 8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Word Cloud of Tweets')
    plt.show()

# Set up the GUI window
root = tk.Tk()
root.title("Tweet Fetcher and Sentiment Analyzer")

# Create a label and text box for the user to input the keyword
label = tk.Label(root, text="Enter a keyword to search for tweets:")
label.pack(pady=10)

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

# Create a button that triggers the tweet fetch and sentiment analysis
fetch_button = tk.Button(root, text="Fetch Tweets and Analyze Sentiment", command=fetch_tweets_and_analyze)
fetch_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
