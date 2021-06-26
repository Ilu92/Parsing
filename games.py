from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()
driver.get('https://app-time.ru/games/list/all/android/2022')
game = driver.find_elements_by_class_name('gamebox')
for i in range(0, len(game)):
    print(game[i].text)


