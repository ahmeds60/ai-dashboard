
import pandas as pd
import matplotlib.pyplot as plt
import requests
from wordcloud import WordCloud
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def fetch_news():
    url = "https://newsapi.org/v2/top-headlines?country=bd&apiKey=119b1bacf5744158a7157d7a5ba1e452"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return [(article.get('title', 'No Title'), article.get('description', 'No Description')) for article in data.get('articles', [])]
    else:
        return []

def analyze_sentiment(text):
    if not text:
        return "Neutral"
    analyzer = SentimentIntensityAnalyzer()
    sentiment_score = analyzer.polarity_scores(text)['compound']
    if sentiment_score > 0.05:
        return "Positive"
    elif sentiment_score < -0.05:
        return "Negative"
    else:
        return "Neutral"

def generate_wordcloud(text_list):
    if not text_list:
        return None
    text = ' '.join(text_list)
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    return wordcloud

def main():
    print("\nAI-Powered Political Sentiment & Misinformation Analysis Dashboard")
    news = fetch_news()
    if news:
        titles, descriptions = zip(*news)
        df = pd.DataFrame({"Headline": titles, "Description": descriptions})
        df['Sentiment'] = df['Description'].apply(lambda x: analyze_sentiment(x) if x else "Neutral")
        
        print("\nLatest Political News & Sentiment Analysis")
        print(df[['Headline', 'Sentiment']])
        
        sentiment_counts = df['Sentiment'].value_counts()
        plt.figure(figsize=(8, 5))
        sentiment_counts.plot(kind='bar', color=['green', 'red', 'gray'])
        plt.title("Sentiment Distribution")
        plt.xlabel("Sentiment")
        plt.ylabel("Count")
        plt.show()
        
        wordcloud = generate_wordcloud(descriptions)
        if wordcloud:
            plt.figure(figsize=(10, 5))
            plt.imshow(wordcloud, interpolation="bilinear")
            plt.axis("off")
            plt.show()
        else:
            print("No sufficient text data for word cloud generation.")
    else:
        print("No news articles found. Please check API or try again later.")

if __name__ == "__main__":
    main()  


++++++++++++++++++    


