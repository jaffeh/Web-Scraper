from pandas.core.frame import DataFrame
from selenium import webdriver
from PIL import Image, ImageOps
from time import sleep
from pytesseract import pytesseract
import pandas as pd
from io import StringIO
from datetime import date
today = date.today()

#Setup Path for OCR(Tesseract) and Chrome webdriver(browser) for automation
pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()

#Website to scrap data from
website = "https://www.benzinga.com/calendars/options"
driver.get(website)

#Sleep so data is loaded on page
sleep(3)
#Take screenshot
driver.save_screenshot("ss.png")
driver.close()

#Resize image to reduce text that is parsed
open_image = "ss.png"
raw_image = Image.open(open_image)
raw_image.show()

width, height = raw_image.size   # Get dimensions
left = width/13
top = height/3.3
right = 41 * width/56
bottom = 9 * height/16
processed_image = raw_image.crop((left, top, right, bottom))
processed_image = ImageOps.grayscale(processed_image)
processed_image.save("ss.png")
processed_image.show()


#Convert from Image -> Text
image_data = pytesseract.image_to_string(Image.open("ss.png"))
# Now to parse raw data into components

#Here we take IO -> Dict -> CSV
file = StringIO(image_data)

columns = ['Date','Time', 'AM/PM','Ticker','Put/Call', 'Strike', 'Expiry', 'DTE', 'Trade Vol', 'Day Vol', 'Vol/OI', 'OI']
parse = list()

for line in file:
        nibble = [item.strip() for item in line.split(' ')]
        parse.append(nibble)

#for line in file:
final_data = pd.DataFrame(data=parse, columns= columns )
final_data.to_csv('data.csv')
print(final_data)