from Modules import *

# #chromedriver 경로 설정
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--start-maximized')
driver = webdriver.Chrome(ChromeDriverManager().install())
print('로그인 테스트 시작!')

class TC_login_Class():
    def def_login(self):
        driver.get(settings.loginurl)
        try:
            driver.find_element(By.NAME, 'email').send_keys(settings.consoleid)
            driver.find_element(By.NAME, 'password').send_keys(settings.password)
            driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/form/button').click()
            time.sleep(settings.sec)

            if driver.current_url == 'https://qa-console.surffy-dev.io/ko/home':
                print('로그인 성공')
                settings.Passcount = settings.Passcount + 1
            else:
                print('로그인 실패')
                settings.FailCount = settings.FailCount + 1
        except:
            print('요소를 찾을 수 없어 로그인 실패')
        
        finally:
            print("PassCount :", settings.Passcount)
            print("FailCount :", settings.FailCount)
            driver.quit()
            print('로그인 테스트 종료!')


            


loginTest = TC_login_Class()
loginTest.def_login()



