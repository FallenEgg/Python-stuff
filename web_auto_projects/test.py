from selenium import webdriver

driver = webdriver.Edge(executable_path="C:\webdrivers\msedgedriver.exe")
driver.get("http://www.google.com/")
print(driver.title)
