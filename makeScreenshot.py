from selenium import webdriver


def make_screenshot(url, query=None, google=False, amazon=False):
    options = webdriver.ChromeOptions()
    options.add_argument('window-size=1440x1440')
    options.headless = True

    driver = webdriver.Chrome(chrome_options=options, executable_path='chromedriver')

    driver.get(url)

    if query is not None:
        if google:
            searchBox = driver.find_element_by_name('q')
            searchBox.send_keys(query)
            searchBox.submit()
        elif amazon:
            searchBox = driver.find_element_by_name('k')
            searchBox.send_keys(query)
            searchBox.submit()

    screenshot = driver.save_screenshot('temp_screenshot.png')
    driver.quit()
