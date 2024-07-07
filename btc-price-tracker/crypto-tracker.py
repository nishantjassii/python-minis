import requests
import json

# fetching data via coinmarketcap API
def get_bitcoin_data(api_key):
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    parameters = {
        "symbol":"BTC", # can be edited to add other coins, ex. ETH
        "convert":"USD"
    }
    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": api_key,
    }
    response = requests.get(url, params= parameters, headers = headers)
    data = response.json()

    return data

def main():
    api_key = "" # removed API key for privacy purposes, re-add here later
    bitcoin_data = get_bitcoin_data(api_key)

    # displaying data, change BTC for whichever coin data needed
    if bitcoin_data:
        print("Symbol: {}".format(bitcoin_data["data"]["BTC"]["symbol"]))
        print("Price: ${}".format(bitcoin_data["data"]["BTC"]["quote"]["USD"]["price"]))
        print("24 hour change: {}".format(bitcoin_data["data"]["BTC"]["quote"]["USD"]["percent_change_24h"]))
    else:
        print("Failed to retrieve data")

if __name__ == "__main__":
    main()

