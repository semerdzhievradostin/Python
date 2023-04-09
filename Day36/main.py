import json
import datetime
from datetime import date
import requests
from twilio.rest import Client


YESTERDAY_CLOSING = str(date.today())
TODAY_CLOSING = datetime.date.today() - datetime.timedelta(days=1)

# --------------------- AUTHENTICATION CODES CHANGED, YOU NEED TO GENERATE UNIQUE ONES FROM THE BELOW URLS ----------- #
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API = "P666V558MQ28NZ0"
NEWS_API = "2e6d6d6aab15485abafc22fe3ba2ade"
account_ssid = "ACb6b8e71fde0608b188b17d86690d842"
auth_tokena = "91dd88eef0bbfd61ae2e128a5f8a221"


url_news = f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&from={YESTERDAY_CLOSING}&to={TODAY_CLOSING}&sortBy=popularity&apiKey={NEWS_API}"
r_news = requests.get(url_news)
data_news = r_news.json()

with open("data_news.json", "w") as datafile:
    json.dump(data_news, datafile, indent=4)

url_stock = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={STOCK}&interval=60min&apikey={STOCK_API}"
r_stock = requests.get(url_stock)
data_stock = r_stock.json()

with open("data_stock.json", "w") as datafile:
    json.dump(data_stock, datafile, indent=4)


# --------------------- CHECK IF STOCK IS -5% or +5% --------------------- #
def stock_check():
    yesterday_price = data_stock["Time Series (60min)"][f"{YESTERDAY_CLOSING} 20:00:00"]["4. close"]
    today_price = data_stock["Time Series (60min)"][f"{TODAY_CLOSING} 20:00:00"]["4. close"]
    tsla_stock_y = float(yesterday_price)
    tsla_stock_t = float(today_price)
    change_percent = ((float(tsla_stock_t) - tsla_stock_y) / tsla_stock_y) * 100
    return round(change_percent, 2)


# --------------------- SEND AN SMS WITH MESSAGE CONTAINING TSLA: 🔺5%--------------------- #
# -----------------------THE 3 MOST POPULAR NEWS ARTICLES REGARDING THE COMPANY --------------------- #
def message_up():
    account_sid = account_ssid
    auth_token = auth_tokena
    client = Client(account_sid, auth_token)
    for i in range(0, 3):
        title = data_news["articles"][i]["title"]
        description = data_news["articles"][i]["description"]
        link = data_news["articles"][i]["url"]
        message = client.messages \
            .create(
            body=f"TSLA: 🔺5%\n{title}\n{description}\n{link}",
            from_=f"+YOURTWILLIO NUMBER",
            to="+YOURNUMBER"
        )
        print(message.sid)


# --------------------- SEND AN SMS WITH MESSAGE CONTAINING TSLA: 🔻5% --------------------- #
# -----------------------THE 3 MOST POPULAR NEWS ARTICLES REGARDING THE COMPANY --------------------- #
def message_down():
    account_sid = account_ssid
    auth_token = auth_tokena
    client = Client(account_sid, auth_token)
    for i in range(0, 3):
        title = data_news["articles"][i]["title"]
        description = data_news["articles"][i]["description"]
        link = data_news["articles"][i]["url"]
        message = client.messages \
            .create(
            body=f"TSLA: 🔻5%\n{title}\n{description}\n{link}",
            from_=f"+15077105824",
            to="+359889331361"
        )
        print(message.sid)


# ------------- CHECK IF STOCK IS UP OR DOWN AND SEND RESPECTIVE MESSAGE ----------- #
if stock_check() >= 5:
    message_up()
elif stock_check() <= -5:
    message_down()

