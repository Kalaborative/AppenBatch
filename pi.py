from selenium import webdriver

driver = webdriver.PhantomJS()
driver.set_window_size(1120, 550)
driver.get('https://duckduckgo.com')
