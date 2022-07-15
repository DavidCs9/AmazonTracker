import requests
import smtplib
from bs4 import BeautifulSoup

URL= "https://www.amazon.com.mx/PHILIPS-242E1GSJ-Pulgadas-FreeSync-Repuesto/dp/B08FNQCS9Z/ref=sr_1_3?keywords=monitor" \
     "%2B24%2Bpulgadas%2B144hz&qid=1657842493&s=electronics&sprefix=monitor%2B24%2B%2Celectronics%2C120&sr=1-3&ufe" \
     "=app_do%3Aamzn1.fos.649fe0ca-1cbf-43f1-a365-f15699263f39&th=1 "

headers = {
    "Accept-Language": "en-US,en;q=0.9,es-419;q=0.8,es;q=0.7,gl;q=0.6",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",

}

response = requests.get(url=URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

price = soup.find("span", class_="a-offscreen")
float_price = price.text.split("$")
float_price2 = float_price[1].split(".")
float_price3 = float_price2[0].split(",")
real_price = int(float_price3[0]+float_price3[1])

EMAIL = "decsiqueiros198@gmail.com"
PSW = "txateqycjekkwvec"

if real_price < 3000:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PSW)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="davidcastrosi@hotmail.com",
            msg=f"Subject:Oferta en monitor gamer\n\n"
                f"El monitor gamer Philips 24 144Hz esta en {real_price}.\n"
                f"El link para comprarlo es el siguiente: {URL}"
        )
