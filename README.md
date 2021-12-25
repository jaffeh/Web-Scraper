# Web-Scraper
Scrapes data from https://www.benzinga.com/calendars/options using Selenium as a browser, Pytesseract as initial parsing, Pandas and StringIO are used to further parse data into a .csv file. Future plans may entail using this project for a database with data analytics.


# ss.png - 
Sample of the screenshot taken with Selenium that was processed and cropped
# data.csv - 
Contains program output
# driver.py - 
Code for the program - I might separate the code and redo the organization, but for the foreseeable future this will suit my needs, as all I may need is a .csv file for the next project
# chromedriver.exe - 
This project won't work without the right version. (download corresponding version of ChromeDriver for Google Chrome that you have downloaded)
Note: Line 12 is the PATH for Pytesseract, you will need to do "pip install pytesseract" in order to use this program. You may need to update the path on Line 12, but most likely not.
