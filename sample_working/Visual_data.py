import pandas as pd
import matplotlib.pyplot as plt

# Load your cleaned data
df = pd.read_csv('sentimix_tweets_with_vader_numeric.csv')

# Check the data type of sentiment column
print(df['sentiment'].dtype)

# If sentiment is not numeric, convert it to numeric (optional step if your data contains strings)
df['sentiment'] = pd.to_numeric(df['sentiment'], errors='coerce')  # Convert invalid values to NaN

# Categorize the sentiment
df['sentiment_label'] = df['sentiment'].apply(lambda x: 'positive' if x > 0 else ('negative' if x < 0 else 'neutral'))

# Plot the sentiment distribution
sentiment_counts = df['sentiment_label'].value_counts()

# Plotting a pie chart
sentiment_counts.plot.pie(autopct='%1.1f%%', startangle=90, figsize=(7, 7), colors=['blue', 'red', 'gray'])
plt.title("Sentiment Distribution of Collected Tweets")
plt.ylabel('')
plt.show()

# Alternatively, a bar chart
sentiment_counts.plot(kind='bar', figsize=(7, 7), color=['blue', 'red', 'gray'])
plt.title("Sentiment Distribution of Collected Tweets")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.show()
from wordcloud import WordCloud

# Join all tweets in a single string
all_tweets = " ".join(df['cleaned_text'])

# Create the word cloud
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(all_tweets)

# Display the word cloud
plt.figure(figsize=(10,8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
