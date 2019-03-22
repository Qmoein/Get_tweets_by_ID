import tweepy

# Use your twitter Authentication Key, to get them go to https://developer.twitter.com

auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)
#file to read tweet IDs
tweetlist = [line.rstrip('\n') for line in open('tweets.txt')]
tweetlist = list(map(int, tweetlist))

def extraction(tweets):
    i = 0
    extraction = []
    while i < tweets:
        try:
            tweet = api.get_status(tweetlist[i], tweet_mode='extended')
        except tweepy.error.TweepError:
            pass
 
        tweettext = tweet.full_text
        extraction.append(tweettext)
        i+=1

        with open("extracted.txt", "w", encoding= 'utf-8') as f:
            f.write('\n'.join(extraction))
#number of tweets want to extraxt
extraction(1)


