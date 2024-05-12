from getpass import getpass
import os
import time
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

def go_msg(driver,to,msg,t):
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div/div[5]/div/div/div/span/div/a/div').click()
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div[4]/div').click()
    driver.implicitly_wait(10)
    ser = driver.find_element(By.TAG_NAME,'input')
    ser.send_keys(to)
    time.sleep(1)
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH,'/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[2]/div/div/div/span/span').click()
    driver.implicitly_wait(10)
    time.sleep(1)
    start = driver.find_element(By.XPATH,'/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[4]/div')
    start.click()
    driver.implicitly_wait(10)
    for item in msg:
        txt = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]')
        txt.send_keys(item)
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[3]').click()
        time.sleep(t)
    time.sleep(2)
def not_now(driver):
    n1 = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div').click()
    driver.implicitly_wait(10)
    n2 = driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
def do_login(driver,user,passw):
    login = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
    login.send_keys(user)
    pas = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
    pas.send_keys(passw)
    pas.submit()

if __name__ == '__main__':
    user = input('Enter user name : ')
    passw = getpass('Enter password : ')
    to = input('To whom : ')
    msg = input('Enter the message: ')
    msg = msg.split(' ')
    t = int(input('Time frequency(in sec) : '))
    os.environ['PATH'] += r"/Users/stijostephen/Developer/selenium_drivers/chromedriver-mac-arm64/chromedriver"
    url = 'https://www.instagram.com/'
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(10)
    do_login(driver,user,passw)
    driver.implicitly_wait(10)
    not_now(driver)
    go_msg(driver,to,msg,t)
    time.sleep(10)
