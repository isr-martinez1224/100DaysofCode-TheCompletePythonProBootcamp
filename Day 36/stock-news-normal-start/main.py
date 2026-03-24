import os
import requests
from twilio.rest import Client
import datetime
from dotenv import load_dotenv

load_dotenv("../../variables.env")

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCKS_API_KEY = os.getenv("STOCKS_API_KEY")

stocks_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCKS_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stocks_params)
response.raise_for_status()

print(response.status_code)
data = response.json()


#1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stocks_list = [[key, value] for (key, value) in data["Time Series (Daily)"].items()]
print(stocks_list)


yesterday = datetime.date.today() - datetime.timedelta(days=1)


#only need today, yesterday, day before yesterday = 0,1,2
print(stocks_list[1])
yesterday_close = float(stocks_list[1][1]["4. close"])
print(f"Closing Yesterday: {yesterday_close}")

#2. - Get the day before yesterday's closing stock price
day_before_close = float(stocks_list[2][1]["4. close"])
print(f"Closing Day Before Yesterday: {day_before_close}")

#3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = abs(yesterday_close - day_before_close)
print(f"Difference: {difference}")

#4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
average = (yesterday_close + day_before_close) / 2
percentage_difference = (difference/average) * 100
percentage_difference = round(percentage_difference,2)
print(f"Percentage Difference: {percentage_difference}%")


#6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
def get_news():
    NEWS_API_KEY = os.getenv("NEWS_API_KEY")

    news_params = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
    }

    response = requests.get(NEWS_ENDPOINT, params=news_params)
    response.raise_for_status()

    print(response.status_code)
    data = response.json()

    #7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    articles = []

    for a in range(3):
        articles.append(data["articles"][a])

        ## STEP 3: Use twilio.com/docs/sms/quickstart/python
        #to send a separate message with each article's title and description to your phone number.

    #8. - Create a new list of the first 3 article's headline and description using list comprehension.
    headlines = [[x["title"], x["description"]] for x in articles]
    print(headlines)
    #9. - Send each article as a separate message via Twilio.
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")


    client = Client(account_sid, auth_token)

    emoji = ""
    if yesterday_close > day_before_close:
        emoji = "🔺"
    else :
        emoji = "🔻"

    for x in range(3):
        text = f"TSLA: {emoji}{percentage_difference}%\nHeadline: {headlines[x][0]}\nBrief: {headlines[x][1]}"

        message = client.messages.create(
            body=text,
            from_=os.getenv("FROM_PHONE"),
            to=os.getenv("TO_PHONE"),
        )
        print(message.status)
        print(text)


    #Optional Format the message like this:
    """
    TSLA: 🔺2%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    or
    "TSLA: 🔻5%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    """

#5. - If TODO4 percentage is greater than 5 then print("Get News").

if percentage_difference > 5:
    print("Get News")
    get_news()
else:
    print("No big difference today")
    ## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.


####### Can't completely send messages due to character restrictions on free trials ##################################