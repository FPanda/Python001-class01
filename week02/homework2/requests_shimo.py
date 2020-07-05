from selenium import webdriver
import time

try:
    # Should use your own account and password.
    # I don't want to expose my own one.
    myAccount = ''
    myPassword = ''
    browser = webdriver.Chrome()

    browser.get('https://shimo.im')
    time.sleep(1)

    login_btn = browser.find_element_by_xpath(
        '//div[@class="entries"]/a[2]')
    login_btn.click()

    time.sleep(1)

    browser.find_element_by_xpath(
        '//div[@type="mobileOrEmail"]/div/input').send_keys(myAccount)
    browser.find_element_by_xpath(
        '//div[@type="password"]/div/input').send_keys(myPassword)

    # Wait for login
    time.sleep(5)

    browser.find_element_by_xpath(
        '//button[@type="black"]').click()

    cookies = browser.get_cookies()  # 获取cookies
    print(cookies)
    time.sleep(3)

except Exception as e:
    print(e)
finally:
    browser.close()
