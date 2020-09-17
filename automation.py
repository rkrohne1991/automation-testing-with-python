from selenium import webdriver


chrome_browser = webdriver.Chrome("./chromedriver")
# chrome_browser.maximize_window()
chrome_browser.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")

assert "Selenium Easy Demo" in chrome_browser.title
show_message_button = chrome_browser.find_element_by_class_name("btn-default")

assert "Show Message" in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id("user-message")
user_buton2 = chrome_browser.find_element_by_css_selector("#get-input > .btn")
user_message.clear()
user_message.send_keys("I AM EXTRA TEXT")

show_message_button.click()
output_message = chrome_browser.find_element_by_id("display")

assert "I AM EXTRA TEXT" in output_message.text
chrome_browser.close()