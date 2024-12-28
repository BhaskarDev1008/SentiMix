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
