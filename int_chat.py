from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
import voice_file

def chat_wrt(req):
    with webdriver.Firefox() as driver:

        driver.get('https://deepai.org/chat')
        wait = WebDriverWait(driver, 10)
        driver.find_element(By.CLASS_NAME, 'chatbox').send_keys(req + Keys.ENTER)
        time.sleep(10)
        element = driver.find_element(By.CLASS_NAME, 'outputBox')
        text_content = element.text
        text_pure=text_content.splitlines()
        text_done = text_pure[0]
        #print(text_pure[0])
        #print()
        #print(text_done)
        voice_file.speek(text_done)
        #return text_done

#chat('Какая сегодня дата')
#voice_file.speek(chat(''))




