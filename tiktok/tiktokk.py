import time
from selenium import webdriver
from tkinter import *

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def autoClick():
##    chrome_options = webdriver.Firefox()
    # chrome_options.add_argument('headless')
##  chrome_options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(executable_path="C:/Users/user/Desktop/tiktok/chromedriver.exe")
    # driver.delete_all_cookies()
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)
    time.sleep(7)


    driver.get("https://www.tiktok.com/login/phone-or-email/email")
    email=driver.find_element_by_name("email")
    email.send_keys("jawadja184@gmail.com")
        # send_keys("ayyanmalik671@gmail.com")
    time.sleep(2)
    pasword = driver.find_element_by_name("password")
    pasword.send_keys("jawad786@")
    # send_keys("MianJani143@")
    button=driver.find_element_by_css_selector('button[type=submit]').click()
    time.sleep(7)
    wait = WebDriverWait(driver, 20)
    driver.get("https://www.tiktok.com/@jawad9t9/video/6955789288005029121?lang=en&is_copy_url=1&is_from_webapp=v1")
        # get("https://www.tiktok.com/@user5036336475872/video/6955727438609386753?lang=en&is_copy_url=1&is_from_webapp=v1")

    wait = WebDriverWait(driver, 20)
    try:
        coment=driver.find_element(By.CSS_SELECTOR, ".lazyload-wrapper:nth-child(1) .jsx-1045706868 > .jsx-1045706868:nth-child(2) svg").click()
    except:
        pass
    print("ddfdfdfd")
    like=driver.find_elements_by_class_name("jsx-2369596684 icon")
    for x in range(0, len(like)):
        if like[x].is_displayed():
            like[x].click()
    time.sleep(29)
    # driver.find_element(By.CSS_SELECTOR, ".jsx-2369596684:nth-child(4) > .icon").click()
    driver.quit()
autoClick()
# user5036336475872

