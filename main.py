import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

contact = input("Enter name >> ")
contact = f"'{contact}'"
text = input("Enter text to send >> ")
n = int(input("Number of times >> "))

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://web.whatsapp.com/")
print("Scan QR Code")
input("Click Enter>> ")
print("Sending...")
elem = driver.find_element_by_xpath("//span[contains(text()," + contact + ")]")
elem.click()

inp_xpath = '//div[@class="_1awRl copyable-text selectable-text"][@contenteditable="true"][@data-tab="6"]'
for i in range(n):
    input_box = driver.find_element_by_xpath(inp_xpath)
    time.sleep(0.1)
    input_box.send_keys(text + Keys.ENTER)
    time.sleep(0.1)
time.sleep(2)
driver.quit()
print("DONE!") 
input("Press enter to quit")
