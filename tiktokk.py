import time
from selenium import webdriver
from tkinter import *

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


def autoClick():
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_experimental_option("debuggerAddress","127.0.0.1:9744")
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    # driver.get("https://www.tiktok.com/login/")
    # login=driver.find_element_by_class_name("channel-name-2qzLW").click()
    # time.sleep(20)
    wait = WebDriverWait(driver, 20)
    driver.get("https://www.tiktok.com/@jawad9t9/video/6955789288005029121?lang=en&is_copy_url=1&is_from_webapp=v1")

        # get("https://www.tiktok.com/@maaheali/video/6956001473973013761?lang=en&is_copy_url=1&is_from_webapp=v1")


        # get("https://www.tiktok.com/@user5036336475872/video/6955727438609386753?lang=en&is_copy_url=1&is_from_webapp=v1")

    wait = WebDriverWait(driver, 20)
    try:
        coment=driver.find_element(By.CSS_SELECTOR, ".lazyload-wrapper:nth-child(1) .jsx-1045706868 > .jsx-1045706868:nth-child(2) svg").click()
    except:
        pass
    print("ddfdfdfd")
    try:
        total_comments=driver.find_element_by_css_selector("div.jsx-3275426247.video-infos-container > div.jsx-2549575510.action-container > div.jsx-2549575510.action-left > div:nth-child(2) > strong")
        n=total_comments.text
        n1=int(n)
        time.sleep(5)
        recentList = driver.find_element(By.CSS_SELECTOR, ".video-infos-container")
        while True:
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", recentList)
            time.sleep(2)

            scrollHeight = (recentList.get_attribute("scrollHeight"))

            # new_height = driver.execute_script("return document.body.scrollHeight")
            print("scroll",scrollHeight)
            n=int(scrollHeight)
            if n==1588:
                break


            # if new_height==last_height:
            #     break
            # else:
            #     last_height=new_height
            #     continue


    except:
        pass
    print("okkkkk")

    for i in range(n1):
        like=driver.find_element_by_css_selector("div.jsx-3275426247.comment-container > div > div:nth-child("+str(i+1) +" ) > div.jsx-2369596684.comment-content.level-1.comment-pc > div.jsx-2369596684.like-container > img")
        # like=driver.find_element(By.CSS_SELECTOR, ".jsx-2369596684:nth-child("+str(i+1) +") > .icon")
        like.click()
        time.sleep(8)

    time.sleep(9)
    # driver.quit()



if __name__ == "__main__":

    autoClick()
# user5036336475872

# email=driver.find_element_by_name("email")
    # email.send_keys("jawadja184@gmail.com")
    #     # send_keys("ayyanmalik671@gmail.com")
    # time.sleep(2)
    # pasword = driver.find_element_by_name("password")
    # pasword.send_keys("jawad786@")
    # # send_keys("MianJani143@")
    # button=driver.find_element_by_css_selector('button[type=submit]').click()

    # main > div.jsx-3461344431.main-body.page-with-header.middle > div.jsx-523345860.video-detail.video-detail-v4.middle > div > div > main > div > div.jsx-3275426247.video-card-big.browse-mode > div.jsx-3275426247.content-container > div.jsx-3275426247.video-infos-container > div.jsx-3275426247.comment-container > div > div:nth-child(1) > div.jsx-2369596684.comment-content.level-1.comment-pc > div.jsx-2369596684.like-container > img
    # main > div.jsx-3461344431.main-body.page-with-header.middle > div.jsx-523345860.video-detail.video-detail-v4.middle > div > div > main > div > div.jsx-3275426247.video-card-big.browse-mode > div.jsx-3275426247.content-container > div.jsx-3275426247.video-infos-container > div.jsx-3275426247.comment-container > div > div:nth-child(2) > div.jsx-2369596684.comment-content.level-1.comment-pc > div.jsx-2369596684.like-container > img