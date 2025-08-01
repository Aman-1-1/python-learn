import requests

country = input("Enter country name: ")
url = f"https://restcountries.com/v3.1/name/{country}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()[0]
    print("Country:", data["name"]["common"])
    print("Capital:", data.get("capital", ["N/A"])[0])
    print("Region:", data.get("region", "N/A"))
    print("Population:", data.get("population", "N/A"))
    print("Flag:", data["flags"]["png"])
else:
    print(" Country not found or API error.")
