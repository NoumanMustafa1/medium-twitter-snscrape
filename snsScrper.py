import snscrape.modules.twitter as sntwitter
import pandas as pd

# Set the search query and other parameters
query = "machine learning"
min_likes = 20
language = "en"
since_year = "2021-5-01" # Set starting month,year and day here #11 #1
until_year = "2021-5-10" # Set ending month,year and day #30 #31
csv_name = "tweets_july_2021.xlsx"
# Create a list to store the scraped tweets
tweets = []

# Define the search query
search_query = f'{query} min_retweets:0 min_faves:{min_likes} lang:"{language}" since:{since_year} until:{until_year}'

# Scrape tweets based on the search query
for tweet in sntwitter.TwitterSearchScraper(search_query).get_items():
  
    final_tweet = tweet
    tweet_data = {
        "Id":tweet.id,
        "tweet": tweet.rawContent,
        "Likes": tweet.likeCount,
        "Retweets": tweet.retweetCount,
        "Date": tweet.date.strftime("%Y-%m-%d %H:%M:%S"),
        "id": tweet.id,
        "created_at": tweet.date.strftime("%Y-%m-%d %H:%M:%S"),
        "tweet": tweet.rawContent,
        "negative": "",
        "neutral": "",
        "positive": "",
        "dominant": "",
        "replies_count": tweet.replyCount,
        "retweets_count": tweet.retweetCount,
        "likes_count": tweet.likeCount,
        "hashtags": tweet.hashtags,
        "cashtags": tweet.cashtags if tweet.cashtags else [] ,
        "language":tweet.lang,
        "link": tweet.url,
        "conversation_id": tweet.conversationId,
        "Jahr": tweet.date.year,
        "Monat": tweet.date.month,
        "Tag": tweet.date.day,
        "time": tweet.date.time().strftime("%H:%M:%S"),
        "user_id": tweet.user.id,
        "username": tweet.user.username,           
    }
    tweets.append(tweet_data)
# Create a pandas DataFrame from the scraped tweets
df = pd.DataFrame(tweets)
#Save data with name specified in csv_name 
df.to_excel(csv_name, index=False)
