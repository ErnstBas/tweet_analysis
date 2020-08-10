import seaborn as sns
import warnings

warnings.filterwarnings('ignore')
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import string
from string import digits
import nltk
from nltk.corpus import stopwords
import re


def prepare_file():
    twitter_df = pd.read_csv(file, low_memory=False)
    twitter_df = twitter_df[['date', 'username', 'tweet', 'likes_count', 'replies_count', 'retweets_count']]
    twitter_df['date'] = pd.to_datetime(twitter_df['date'])
    # start_date ='2020-08-01'
    # end_date = '2020-08-02'
    # mask = (twitter_df['date'] > start_date) & (twitter_df['date'] <= end_date)
    # print(twitter_df.head())
    return twitter_df


def plot_timeseries():
    plt.style.use('ggplot')
    plt.plot(data.groupby('date')['tweet'].count())
    plt.title('Number of tweets per day')
    plt.xlabel('datum')
    plt.ylabel('tweets')
    plt.xticks(rotation=45, horizontalalignment='right')
    plt.savefig('tweetplot.png')
    plt.show()


def print_likes():
    """
    plot the distribution of likes
    """
    sns.distplot(data['likes_count'])
    print('description likes: \n', data['likes_count'].describe())
    plt.show(block=False)


def plot_retweets_likes():
    """
    plot the retweets and likes
    """
    var = 'retweets_count'
    new_data = pd.concat([data['likes_count'], data[var]], axis=1)
    new_data.plot.scatter(x=var, y='likes_count')
    plt.show()


def plot_replies_likes():
    """
    plot the replies and likes
    """
    var = 'replies_count'
    new_data = pd.concat([data['likes_count'], data[var]], axis=1)
    new_data.plot.scatter(x=var, y='likes_count')
    plt.show()


def top_100_liked_tweet():
    most_liked_tweets = data.sort_values(by=['likes_count'], ascending=False, na_position='last').head(100)
    most_liked_tweets.to_csv("most_liked_tweets.csv")
    most_liked_tweets_usersandlikes = most_liked_tweets[['username', 'likes_count']]
    print('\nmost liked tweets: \n', most_liked_tweets_usersandlikes.head(10))
    return most_liked_tweets


def cleantxt(df):
    """
    clean text and replace stopwords
    """
    df = df.apply(lambda x: x.translate(str.maketrans(' ', ' ', string.punctuation)))
    df = df.apply(lambda x: x.translate(str.maketrans(' ', ' ', digits)))
    df = df.apply(lambda x: x.lower())
    df = df.replace({'spacex': ''}, regex=True)
    df = df.apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))
    return df


def create_wordcloud():
    """
    Create wordcloud of most used words
    https://www.datacamp.com/community/tutorials/wordcloud-python
    """
    text = cleantxt(data['tweet'])
    text = " ".join(word for word in text)
    wordcloud = WordCloud(max_words=100, background_color="white").generate(text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()


def basic_clean(text):
    """
    A simple function to clean up the data. All the words that
    are not designated as a stop word is then lemmatized after
    encoding and basic regex parsing are performed.
    https://towardsdatascience.com/from-dataframe-to-n-grams-e34e29df3460
    """
    wnl = nltk.stem.WordNetLemmatizer()
    words = re.sub(r'[^\w\s]', '', text).split()
    return [wnl.lemmatize(word) for word in words]


def n_grams():
    most_used_words = data['tweet'].str.split(expand=True).stack().value_counts().head(100)
    print('\nunigrams:\n', most_used_words.head(10))

    words = basic_clean(''.join(str(cleantxt(data['tweet']).tolist())))

    bigrams = (pd.Series(nltk.ngrams(words, 2)).value_counts())[:20]
    print('\nbigrams:\n', bigrams[:20])

    trigrams = (pd.Series(nltk.ngrams(words, 3)).value_counts())[:20]
    print('\ntrigrams:\n', trigrams[:20])


file = 'FileName.csv'
data = prepare_file()
stop = stopwords.words('english')
# plot_timeseries()
# plot_retweets_likes()
# create_wordcloud()
top_100_liked_tweet()
n_grams()
