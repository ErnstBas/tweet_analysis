# tweet_analysis

Retrieve tweets with Twint and perform some basic analysis with Pandas (plot timeline, wordcloud, generate most liked tweets, generate ngrams)

# retrieve tweets

To generate a csv file with tweets from Twitter, the program uses Twint. This library permits to use certain search terms, indicate language and search period. The nice thing about Twint is that it does not require the Twitter API and it is possible to scrape relatively large amounts of tweets.

# basic analysis of tweets

The csv file is used as input for a basic analysis with Pandas of the tweets. First it performs a selection of the most relevant columns as well as some cleaning of the data. The program enables to plot a timeline of the tweets, scatterplots of the retweets and likes and comments and likes, it can create a wordcloud, create a separate dataframe with the 100 most liked tweets (which is also written to a separate csv file). Finally the program produces unigrams, bigrams and trigrams.

# some remarks
I am not an experienced programmer. I assembled the program using tutorials and ideas of others. There is certainly room for improvement. Suggestion and corrections are very much appreciated. For example there are two methods for cleaning of the data. This should be merged in some way.
The proposed analysis are rather basic. I am looking for ways to perform more in depth sentiment analysis of the tweets. Hopefully in future iterations I will be able to update the program. 

