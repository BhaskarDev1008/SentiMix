# Sentimix Tweet Analyzer: Sentiment Analysis with Data Labeling

**Sentimix** is a comprehensive Python-based tool that not only performs sentiment analysis but also emphasizes **data labeling** as a core part of its workflow. This project reflects the skills required to manage, preprocess, and label real-world datasets, preparing them for advanced analysis or machine learning tasks.

## Features
- **Tweet Collection**: Fetches recent tweets using the Twitter API based on a user-defined keyword.
- **Data Preprocessing**: Clean and standardize tweet text for analysis.
- **Data Labeling**: Automatically labels tweets with sentiment categories (Positive, Neutral, Negative) using VADER sentiment analysis.
- **Visualization**: Generates visual insights with:
  - Pie Chart: Sentiment distribution
  - Bar Graph: Sentiment counts
  - Word Cloud: Most frequent words
- **Graphical User Interface (GUI)**: Simplifies the user experience.
- **CSV Output**: Stores labeled and processed datasets for further use.

---

## Demonstrated Skills
1. **Data Collection**: Use of APIs to collect raw data from external sources.
2. **Data Preprocessing**: Cleaning and organizing text data.
3. **Data Labeling**: Assigning meaningful sentiment labels to raw text data, creating structured datasets.
4. **Data Visualization**: Communicating insights through charts and graphics.
5. **End-to-End Workflow Management**: From data collection to delivering actionable insights.

---

## Requirements
Install the required libraries using:
```bash
pip install -r requirements.txt

---
## Workflow
**1. Data Collection
Enter a keyword in the GUI to fetch 25 recent tweets.
Tweets are saved to a CSV file for further analysis.
**2. Data Labeling
Sentiment scores are computed using the VADER Sentiment Intensity Analyzer.
Tweets are automatically labeled as Positive, Neutral, or Negative and saved in a structured dataset.
**3. Visualization
Pie Chart: Displays the distribution of sentiment categories.
Bar Graph: Counts the number of tweets in each category.
Word Cloud: Highlights frequently used words in the tweets.
**4. Output
A labeled dataset (sentimix_tweets_with_vader_numeric.csv) with sentiment categories.
