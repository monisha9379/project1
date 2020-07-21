import requests
from bs4 import BeautifulSoup

oyo_url = "https://www.oyorooms.com/hotels-in-bangalore/"
req = requests.get(oyo_url)
content = req.content

soup = BeautifulSoup(content, "html.parser")
all_hotels = soup.find_all("div", {"class": "hotelCardlisting"})

for hotel in all_hotels:
    hotel_name = hotel.find("h3",{"class": "listingHotelDescription_hotelName"}).text
    print(hotel_name)

