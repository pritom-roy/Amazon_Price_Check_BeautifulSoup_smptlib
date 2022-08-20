import smtplib
import os
import requests
from bs4 import BeautifulSoup


header = {
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,bn;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
}
url = "https://www.amazon.com/BLACK-DECKER-BCRK32B-Compact-Refrigerator/dp/B01DZQI6W4/ref=sr_1_5?crid=YM2UMAV9A21Q&keywords=single+door+fridge&qid=1661004778&sprefix=single+door+fridg%2Caps%2C366&sr=8-5"
response = requests.get(
    url=url,
    headers=header)
response.raise_for_status()

soup = BeautifulSoup(response.text, "lxml")
# print(soup.prettify())

price = soup.find(name="p", class_="twisterSwatchPrice")
price = float(price.getText().split("$")[1].split()[0])
print(price)

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=os.environ['Email'], password=os.environ['password'])
    if price <= 250.00:
        connection.sendmail(from_addr="mtesting.smtp@gmail.com", to_addrs="kamolesh.pritom@yahoo.com",
                            msg=f"Today is the price\n\n{price}\n\n{url}")
