from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


import os
import time
import carid.constants as const

class Vehicle(webdriver.Chrome):

    def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.dirname(__file__)
        return os.path.join(base_path, relative_path)

    def __init__(self, driver_path = r"./SeleniumDriver", teardown = False):
        options = Options()
        options.binary_location = "C:\Program Files\Google\Chrome Beta\Application\chrome.exe"
        options.add_experimental_option('excludeSwitches',['enable-logging'])
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Vehicle, self).__init__(chrome_options=options)
        self.implicitly_wait(60)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.base_url)

    def select_year(self):
        year_button = self.find_element(By.CSS_SELECTOR,"div[data-placeholder='Year']")
        make_button = self.find_element(By.CSS_SELECTOR, "div[data-placeholder='Make']")
        model_button = self.find_element(By.CSS_SELECTOR, "div[data-placeholder='Model']")

        year_button.click()
        years = self.find_elements(By.CSS_SELECTOR,"li[class='item ']")
        final_list = []

        for year in years:
            if year == years[0]:
                yearvalue = year.get_attribute('value')
                year.click()
                make_button.click()
                makers = self.find_elements(By.CSS_SELECTOR,"li[class='item ']")
                for make in makers:
                    if make == makers[0] and year == years[0]:
                        makevalue = make.get_attribute('innerHTML')
                        make.click()
                        model_button.click()
                        models = model_button.find_elements(By.TAG_NAME, "li")[1:]
                        for model in models:
                            modelvalue = model.get_attribute('innerHTML')
                            while yearvalue == '' or makevalue == '':
                                yearvalue = year_button.find_element(By.CSS_SELECTOR, "li[class='item  -active']").text
                                makevalue = make_button.find_element(By.CSS_SELECTOR, "li[class='item  -active']").text
                            list_to_append = [yearvalue,makevalue,modelvalue]
                            print(list_to_append)
                            final_list.append(list_to_append)
                        make_button.click()
                    else:
                        make_button.send_keys(Keys.ARROW_DOWN)
                        makevalue = make_button.find_element(By.CSS_SELECTOR,"li[class='item  -active']").text
                        model_button = self.find_element(By.CSS_SELECTOR, "div[data-placeholder='Model']")
                        model_button.click()
                        models = model_button.find_elements(By.TAG_NAME, "li")[1:]
                        for model in models:
                            modelvalue = model.get_attribute('innerHTML')
                            while yearvalue == '' or makevalue == '':
                                yearvalue = year_button.find_element(By.CSS_SELECTOR, "li[class='item  -active']").text
                                makevalue = make_button.find_element(By.CSS_SELECTOR, "li[class='item  -active']").text
                            list_to_append = [yearvalue,makevalue,modelvalue]
                            print(list_to_append)
                            final_list.append(list_to_append)
                        make_button.click()
            else:
                year_button.send_keys(Keys.ARROW_DOWN)
                yearvalue = year_button.find_element(By.CSS_SELECTOR, "li[class='item  -active']").text
                make_button.click()
                makers = self.find_elements(By.CSS_SELECTOR, "li[class='item ']")
                for make in makers:
                    if make == makers[0] and year == years[0]:
                        makevalue = make.get_attribute('innerHTML')
                        make.click()
                        model_button.click()
                        models = model_button.find_elements(By.TAG_NAME, "li")[1:]
                        for model in models:
                            modelvalue = model.get_attribute('innerHTML')
                            while yearvalue == '' or makevalue == '':
                                yearvalue = year_button.find_element(By.CSS_SELECTOR, "li[class='item  -active']").text
                                makevalue = make_button.find_element(By.CSS_SELECTOR, "li[class='item  -active']").text
                            list_to_append = [yearvalue, makevalue, modelvalue]
                            print(list_to_append)
                            final_list.append(list_to_append)
                        make_button.click()
                    else:
                        make_button.send_keys(Keys.ARROW_DOWN)
                        makevalue = make_button.find_element(By.CSS_SELECTOR, "li[class='item  -active']").text
                        model_button = self.find_element(By.CSS_SELECTOR, "div[data-placeholder='Model']")
                        model_button.click()
                        models = model_button.find_elements(By.TAG_NAME, "li")[1:]
                        for model in models:
                            modelvalue = model.get_attribute('innerHTML')
                            while yearvalue == '' or makevalue == '':
                                yearvalue = year_button.find_element(By.CSS_SELECTOR, "li[class='item  -active']").text
                                makevalue = make_button.find_element(By.CSS_SELECTOR, "li[class='item  -active']").text
                            list_to_append = [yearvalue, makevalue, modelvalue]
                            print(list_to_append)
                            final_list.append(list_to_append)
                        make_button.click()
        return final_list


    def close_popup(self):
        self.implicitly_wait(60*5)
        self.find_element(By.CSS_SELECTOR,"svg[aria-describedby='close-form']").click()













