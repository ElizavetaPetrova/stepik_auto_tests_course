from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


try:
    #open page
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome("C:\chromedriver\chromedriver.exe")
    browser.get(link)
    #fill fields
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("Smolensk@gmail.com")
    #download file
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    element = input4 = browser.find_element(By.ID, "file")
    element.send_keys(file_path)
    #click button
    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()