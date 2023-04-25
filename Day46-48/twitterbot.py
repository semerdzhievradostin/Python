from speed_tweet_class import InternetSpeedTwitterBot

#change UP and DOWN as your provider's advertised speeds
PROMISED_UP = 100
PROMISED_DOWN = 100
TWITTER_EMAIL = "youremail"
TWITTER_USERNAME = "yourusername"
TWITTER_PW = "yourpassword"
INTERNETPROVIDER = "@yourinternetprovider"


# Check your internet speed and tweet to your provider if it's slower than advertised .
check_speed_and_tweet = InternetSpeedTwitterBot()

check_speed_and_tweet.get_internet_speed()
if float(check_speed_and_tweet.up.text) < PROMISED_UP and float(check_speed_and_tweet.down.text) < PROMISED_DOWN:
    check_speed_and_tweet.tweet_at_provider(TWITTER_EMAIL, TWITTER_PW, TWITTER_USERNAME, str(check_speed_and_tweet.up.text), str(check_speed_and_tweet.down.text, INTERNETPROVIDER))




