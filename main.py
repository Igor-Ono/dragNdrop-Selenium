# Drag and Drop script with Selenium
# Example site: http://www.dhtmlgoodies.com/index.html?page=dragDrop
# Demo: http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

if __name__ == "__main__":
    # Using ChromeDriver, for Firefox, use webdriver.Firefox()
    # If chromedriver was not added to PATH, it needs to be pointed at inside the () below
    driver = webdriver.Chrome("./chromedriver_win32/chromedriver.exe")
    driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')
    source = driver.find_element_by_xpath('//*[@id="box3"]')
    dest = driver.find_element_by_xpath('//*[@id="box103"]')
    actions = ActionChains(driver)
    actions.drag_and_drop(source, dest).perform()

