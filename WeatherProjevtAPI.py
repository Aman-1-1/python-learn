import requests
API_KEY="262011ebce604f68ed033339cc339ef3"
CITY=input("Enter City Name : ")
url=f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response=requests.get(url)

data=response.json()
print( data["main"]["temp"], data["visibility"],data["wind"]["speed"])
if data["wind"]["speed"]>=1:
    print ("its fairly windy")
else:
    print ("its not windy")