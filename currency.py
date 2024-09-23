import requests

API_KEY = "fca_live_X3HHFgkzdN6WqY7QbND0zUVVKZu0i1F2x2UIsFRB"
BASE_URL= f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD", "CAD", "EUR", "AUD"]
def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    
    except Exception as e:
        print("Invalid currency code")
        return None

while True:
    base = input("Enter base currency  (q for quit): ").upper()

    if base == "Q":
        break
    
    data = convert_currency(base)
    if not data:
        continue
       
    for ticker, value in data.items():
        print(f"{ticker}:: {value}")