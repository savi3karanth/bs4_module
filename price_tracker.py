import requests
from bs4 import BeautifulSoup
import smtplib
import os
import lxml

static_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
my_email = os.environ.get('MY_EMAIL')
password = os.environ.get('PASSWORD')

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Google Chrome\";v=\"134\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"macOS\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
  }

response = requests.get(url=static_url, headers=headers)
data = response.text



soup = BeautifulSoup(data, "lxml")
price = soup.find(class_="a-offscreen").getText()
price_without_currency = (price.split('$')[1])

price_in_float = float(price_without_currency)
print(price_in_float)

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 100



if price_in_float < BUY_PRICE:
    message = f"{title} is on sale for {price}"
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=my_email,
        msg=f"Subject:Amazon Price Alert!\n\n{message}\n{static_url}".encode("utf-8"))

