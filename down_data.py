__author__ = 'yem'
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

def test():

    driver = webdriver.PhantomJS(executable_path=r"D:\phantomjs-2.1.1-windows\bin\phantomjs.exe")

    #driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")

    driver.get("https://touzi.sina.com.cn/public/strategy/ls")

    time.sleep(7)

    savefile = open("stack.html","w",encoding="UTF-8",errors="ignore")



    #print(driver.page_source)

    print(type(driver.page_source))
    savefile.write(driver.page_source)

    savefile.close()

def test_chrome():
    driver = webdriver.Chrome()

    driver.get("http://www.baidu.com")

    time.sleep(7)



URL = "https://touzi.sina.com.cn/public/strategy/ls"


def save_page(source,filename="default.html"):

    fw = open(filename,"w",encoding="UTF-8",errors="ignore")

    fw.write(source)

    fw.close()



def stack_page():

    driver = webdriver.Chrome()

    driver.get(URL)

    try:
        element_flag = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CLASS_NAME,"page-cur")))
    finally:
        print("open page")

        save_page(driver.page_source,"stack_start.html")

        temp_element = driver.find_element_by_css_selector(".ls_list_wrap")


        #print(temp_element)


        if temp_element != None:
            tt = temp_element.find_element_by_css_selector("[data-sort='percentSort']")

            #print(tt)

            time.sleep(2)
            tt.click()
            print("frist click")
            time.sleep(4)
            tt = temp_element.find_element_by_css_selector("[data-sort='percentSort']")
            print("second click")
            tt.click()
            time.sleep(5)



        driver.close()


PHANTOMJS_PATH = r"D:\phantomjs-2.1.1-windows\bin\phantomjs.exe"

class Stack_download():

    def __init__(self):

        self.driver  = webdriver.PhantomJS(executable_path=PHANTOMJS_PATH)
        self.ready_next = False


    def get_page(self,url):

        self.driver.get(url)

        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "page-cur")))

        finally:

            self.ready_next = True
            print("get page!!")

    def save_page(self,filename = "default.html"):

        if self.driver:

            with open(filename,"w",encoding="UTF-8",errors="ignore") as f:

                f.write(self.driver.page_source)

                print("save file as :" + filename)


    def __click(self,element,waittime):

        element.click()

        time.sleep(waittime)

    def __get_list_element(self):

        return self.driver.find_element_by_css_selector(".ls_list_wrap")

    def __get_percent_element(self):

        return self.__get_list_element().find_element_by_css_selector("[data-sort='percentSort']")

    def sort_page_show(self):

        if self.ready_next != True:
            print("not ready!")
            return

        list_element = self.__get_list_element()

        if list_element is not None:

            percent_element = self.__get_percent_element()

            self.__click(percent_element,2)

            percent_element = self.__get_percent_element()

            self.__click(percent_element,2)

            print("ok,you can get the data!")

        else:

            print("not find page")







if __name__ == "__main__":


    #test_chrome()
    ss = Stack_download()
    ss.get_page(URL)
    ss.sort_page_show()
    ss.save_page()

    print("end!!!!")