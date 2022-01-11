######### Validate Out of stock text over alpages with excel sheet ###########
#Done#
from Screenshot import Screenshot_Clipping
import datetime
import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from loguru import logger
from selenium.webdriver.chrome.options import Options

now = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S") #This is for date format

logger.add("../Logs/Log-"+now+".log",level="TRACE", rotation="500 MB") #This is logger which will create warning or normal message

df = pd.read_excel('../Utilities/Zodiac-dec-2021.xlsx') # Get all the urls from the excel

mylist = df['urls'].tolist() #urls is the column name

ss = Screenshot_Clipping.Screenshot()
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(10)
# now loop through each url & perform actions.
for url in mylist:
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver.get(url)
#verify availablity of text "Out Of stock"
    error1 = driver.page_source.__contains__("Out of stock")
    if error1 == True:
        logger.warning("Found Out of the stock product on:" + driver.current_url)

    else:
        logger.info("Not found:" + driver.current_url)

#now print page name for screenshot name
    url_page = driver.current_url
    filename = url_page.split("/")[-1]
    bad_chars = [';', '', '|', '.html','?' ]
    for i in bad_chars:
        filename = filename.replace(i, '')

    print(filename) #Print page name
    #ss.full_Screenshot(driver, save_path=r'../ScreenShot/', image_name=filename + now + '.png') #page screenshot

logger.info("Task complete")