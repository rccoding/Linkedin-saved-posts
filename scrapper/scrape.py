# import os
# import pickle
from linkedin_scraper import Person, actions
# # from samples import actions
# from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# options = Options()
# # options.add_argument('--headless')
# # options.add_argument() 
# driver = webdriver.Chrome()

email = 'rishikachopra21@gmail.com'
password = 'Mahender@9868'
# driver.get("https://www.linkedin.com/")
# driver.get("https://www.linkedin.com")
# driver = webdriver.Chrome(executable_path='Chrome_driver_path')
# driver.get("https://www.facebook.com")

# Enter Email id and Password if you are already Registered user
# driver.find_element(By.NAME, "email").send_keys(email)
# driver.find_element(By.NAME, "pass").send_keys(password)

# # Submit the form
# driver.find_element(By.NAME, "login").click()

# with open("cookies.pkl", "wb") as file:
#     pickle.dump(driver.get_cookies(), file)
# actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal
# person = Person("https://www.linkedin.com/in/andre-iguodala-65b48ab5", driver=driver)
# export CHROMEDRIVER=~/chromedriver
import pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup

PROFILE_PATH = 'C:/Users/91920/AppData/Local/Google/Chrome/User Data/Profile'

options = Options()
options.add_argument("--user-data-dir=" + PROFILE_PATH)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

# def login(driver):
#     driver.get("https://www.facebook.com")  # replace with the actual login URL

#     # username_field = driver.find_element_by_name("username")  # replace with the actual name or ID of the username field
#     driver.find_element(By.NAME, "email").send_keys(email)
#     driver.find_element(By.NAME, "pass").send_keys(password) # replace with the actual name or ID of the password field

#     # username_field.send_keys(email)
#     # password_fiel'https://www.linkedin.com/feed/update/urn:li:activity:7166628899336998912/'d.send_keys(password)

#     driver.find_element(By.NAME, "login").click()  # press Enter to submit the form

#     # Save cookies to a file
#     with open("cookies.pkl", "wb") as file:
# #         pickle.dump(driver.get_cookies(), file)
# def scrape_website(url):
#     try:
#         # driver = webdriver.Chrome()  # or the browser driver you are using
#         driver.get('https://www.linkedin.com/feed/update/urn:li:activity:7166628899336998912?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7166628899336998912%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29')
#         time.sleep(5)
#         page_source = driver.page_source
#         soup = BeautifulSoup(page_source, 'html.parser')
        
#         time.sleep(5)
#         results = soup.find("div",{'id':'ember1162'})

#         if results:
#             text_content = results.get_text(separator=' ')
#             print(text_content)
#         else:
#             print("No results found")

        
#         # print(cut_url)
#         # specific_div = soup.find('div', attrs={'data_url': cut_url})
#         # text_content = specific_div.get_text(separator=' ')
#         print("scraped data", text_content)
#         # print("scraped data", text_content)
#         # Truncate to the first 8192 characters
#         # return text_content[:2192]
#     except:
#         print("The website is not responding. Please try again later.")
#     finally:
#         driver.quit()
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import re
import urllib3
import socket

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, message, from_addr, to_addr, password):
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_addr, password)
    text = msg.as_string()
    server.sendmail(from_addr, to_addr, text)
    server.quit()

http = urllib3.PoolManager(
   timeout=1.0,
   retries=5
)
def scrape_website(url):
    try:
        try:
            time.sleep(10)
            # WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'ember1162')))
            print ("Page is ready")
            page_source = driver.page_source
            soup = BeautifulSoup(page_source, 'html.parser')
            match = re.search(r'urn:li:activity:(\d+)', url)
            if match:
                print(match.group(0))
                results = soup.find("div",{'data-chameleon-result-urn':match.group(0)})

                if results:
                    button = results.find('button')  # replace 'button' with the actual tag name of your button
                    if button:
                        # get the selenium WebElement from the button
                    # button_web_element = driver.find_element(By.TAG_NAME,'reusable-search-show-more')
                        try:
                            button = driver.find_element(By.XPATH, "//button[@aria-label='See more, click to view the full content.']")
                            button.click()
                        except NoSuchElementException:
                            print("No 'See more' button found")

                        # print("Button clicked")
                        time.sleep(10)
                    else:
                        print("No button found")
                    
                    text_content = results.get_text(separator=' ')
                    # send_email('Scraped Content', text_content, 'rishikachopra21@gmail.com', 'rishikachopra36@@gmail.com', 'Mahender@9868')
                    print(text_content)
                    return text_content
                    
                else:
                    print("No results found")
        except TimeoutException:
            print ("Loading took too much time")
    except Exception as e:
        print("The website is not responding. Please try again later.")
        print(str(e))

def gotosaved(driver):
    driver.get('https://www.linkedin.com/my-items/saved-posts/')
    all_text = ""
    time.sleep(5)
    li_elements = driver.find_elements(By.TAG_NAME, 'a')

    for li in li_elements:
        href = li.get_attribute('href')

        
        if href.startswith('https://www.linkedin.com/feed/update/urn:li:'):
                time.sleep(5)
                text=scrape_website(url=href)
                if(text):
                    all_text += text + "\n"
                    print(text,"GOLAAAAAAAAAAAA")
    
    return text
                
def load_cookies(driver):
    with open("cookies.pkl", "rb") as file:
        cookies = pickle.load(file)
        print(cookies)
        for cookie in cookies:
            driver.add_cookie(cookie)

def save_to_file(content,filename):
    with open(filename, 'a') as file:
        file.write(content)

# Try to load the cookies and go to the page
def myfunc():
    try:
        driver.get("https://www.linkedin.com/")  # replace with the actual URL
        # load_cookies(driver)
        txt=gotosaved(driver)
        save_to_file(txt,'scraped_text.txt')
        time.sleep(10)
        mail()
        
    # driver.refresh()  # refresh the page to apply the cookies
    except (FileNotFoundError, pickle.UnpicklingError):
        # If loading cookies failed, log in manually
        actions.login(driver=driver,email=email,password=password)




import datetime
import time
import smtplib
from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


# create mail object
def mail():
    import os
    import smtplib
    import ssl

    SMTP_SERVER = "smtp.gmail.com"
    PORT = 587
    EMAIL = email
    PASSWORD = 'mbkx xmgp yymt tylq'

    context = ssl.create_default_context()
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = email
    msg['Subject'] = "ko"
    body = MIMEText("kokokok", 'plain')
    msg.attach(body)
    filename = 'scraped_text.txt'
    with open(filename, 'r') as f:
        part = MIMEApplication(f.read(), Name=basename(filename))
        part['Content-Disposition'] = 'attachment; filename="{}"'.format(basename(filename))
    msg.attach(part)

    with smtplib.SMTP(SMTP_SERVER, PORT) as server:
        server.starttls(context=context)
        server.login(EMAIL, PASSWORD)
        message = msg.as_string()
        server.sendmail(EMAIL, "rishikachopra36@gmail.com", message)

myfunc()

# def run_daily_at(func, hour=19):
#     """Runs the given func every day at specified hour"""
#     try:
#         with open('nextrun.txt', 'r') as f:
#             next_run = datetime.datetime.fromisoformat(f.read()) 
#     except FileNotFoundError:
#         # Set next run to today at hour
#         now = datetime.datetime.now()
#         next_run = now.replace(hour=hour, minute=0, second=0, microsecond=0)
        
#     while True:
#         now = datetime.datetime.now()
        
#         if now >= next_run:
#             func() # Call function
#             print('Ran function')
            
#             # Schedule next run 1 day later
#             next_run = now + datetime.timedelta(days=1)  
#             next_run = next_run.replace(hour=6, minute=55, second=0, microsecond=0)
            
#             with open('nextrun.txt','w') as f:
#                 f.write(next_run.isoformat())
                
#         time.sleep(60*10) # Check every 10 mins  

# # Example   
# def my_func():
#     print('Running my daily function!')
    
# run_daily_at(myfunc)
# Rest of your scraping code...
