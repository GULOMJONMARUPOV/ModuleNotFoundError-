from features.ui.all_imports import *



class Login():

    def test_login(self):
        """takes screenshots if no element found"""
        driver = webdriver.Chrome()
        url = "http://the-internet.herokuapp.com/login"
        driver.get(url)

        
        try:
            # use the following Login steps we created previously
            print("loggin page started..")
            username = driver.find_element_by_xpath("//input[@id='username']")
            passwrod = driver.find_element_by_xpath("//input[@id='password']")
            login = driver.find_element_by_xpath("//i[@class='fa fa-2x fa-sign-in']")
            username.send_keys("tomsmith")
            passwrod.send_keys("SuperSecretPassword!")
            login.click()
            print("logged in, taking screenshot")
            sleep(10) 
            filepath = "POM/screenshots/"+ utils.get_timestamp() + ".png"
            driver.save_screenshot(filepath)
            print("test completed")
        except:
            print("Something went wrong!")
            filepath = "POM/screenshots/error-"+ utils.get_timestamp() + ".png"
            driver.save_screenshot(filepath)
            raise