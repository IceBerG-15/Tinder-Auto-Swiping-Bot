from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException,ElementClickInterceptedException
import time
import os
from dotenv import load_dotenv

load_dotenv('projects\Tinder autoswipe bot\.env')

chrome_driver_path="C:\\Python310\\chrome_driver\\chromedriver.exe"
driver=webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://tinder.com/')

time.sleep(2)

login=driver.find_element('xpath',"//*[text()='Log in']")
login.click()

time.sleep(2)

try:
    facebook=driver.find_element('xpath','//*[@id="o793001744"]/main/div/div[1]/div/div/div[3]/span/div[2]/button')
    facebook.click()
except  NoSuchElementException:
    more_options=driver.find_element('xpath','//*[@id="o793001744"]/main/div/div[1]/div/div/div[3]/span/button')
    more_options.click()
    time.sleep(2)
    facebook=driver.find_element('xpath','//*[@id="o793001744"]/main/div/div[1]/div/div/div[3]/span/div[2]/button')
    facebook.click()

time.sleep(2)

main_window=driver.window_handles[0]
facebook_window=driver.window_handles[1]

driver.switch_to.window(facebook_window)  #switched to facebook login window

facebook_email=driver.find_element('xpath','//*[@id="email"]')
facebook_email.send_keys(os.getenv('EMAIL'))

facebook_pass=driver.find_element('name','pass')
facebook_pass.send_keys(os.getenv('PASS'))
facebook_pass.send_keys(Keys.ENTER)

driver.switch_to.window(main_window)        #switching back to main tinder window
time.sleep(2)

#allow location acess
allow_location_button = driver.find_element('xpath','#q-839802255 > main > div > div > div > div.CenterAlign.Pb\(24px\).Px\(24px\).Py\(12px\).D\(f\).Fxd\(rr\).Ai\(st\) > button.c1p6lbu0.Fxb\(1\/2\).Mstart\(8px\)')
print(allow_location_button.text)

time.sleep(1)
#Disallow notifications
notifications_button = driver.find_element('xpath','//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

time.sleep(1)
#Allow cookies
cookies = driver.find_element('xpath','//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

time.sleep(2)
#Tinder free tier only allows 100 "Likes" per day. If you have a premium account, feel free to change to a while loop.
for n in range(100):

    #Add a 1 second delay between likes.
    time.sleep(1)

    try:
        print("called")
        like_button = driver.find_element('xpath','//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element('css selector',".itsAMatch a")
            match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            time.sleep(2)



time.sleep(60)
driver.quit()
