# test code: selenium plus phantomjs

from selenium import webdriver
driver = webdriver.PhantomJS()
driver.set_window_size(1120, 550)
driver.get("https://duckduckgo.com/")
driver.find_element_by_id('search_form_input_homepage').send_keys("realpython")
driver.find_element_by_id("search_button_homepage").click()
print driver.current_url
driver.quit()

# test code 2

# from selenium import webdriver
# driver = webdriver.Firefox()
# driver.get("https://duckduckgo.com/")
# driver.find_element_by_id('search_form_input_homepage').send_keys("realpython")
# driver.find_element_by_id("search_button_homepage").click()
# driver.quit()
