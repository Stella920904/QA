import selenium.webdriver.support.ui as ui
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

#chromedriver 경로 설정
CHROMEDRIVER_PATH = 'chromedriver.exe'
chrome_options = Options()
chrome_options.add_argument('--start-maximized')

#URL info
path = ".\chromedriver.exe"
loginurl = "https://console.surffy.io/ko/signin"

driver = webdriver.Chrome(path)

#sleep 시간
sec = 1

#로그인 반복 수
loginCount = 50

numA = 0
numB = 0
numC = 0
ori = 0

eventori = 0
eventA = 0
eventB = 0
eventC = 0

# 그룹 ID
groupA = '165'
groupB = '166'
groupC = '167'

# 브라우저 실행 및 탭 추가
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options )

for dirver in range(loginCount):
    driver.execute_script('window.open("about:blank", "_blank");')
    tabs = driver.window_handles

for num in range(loginCount):
    driver.switch_to.window(tabs[num])
    driver.get(loginurl)                                                                                                          # 콘솔 url 회원가입 페이지 열기 
    time.sleep(sec)

    session_storage_data1 = driver.execute_script("return window.sessionStorage.getItem('ffflow-except-target')")
    session_storage_data2 = driver.execute_script("return window.sessionStorage.getItem('cm_current_group_id')")
    print(session_storage_data1, session_storage_data2)

    if num%2 == 0 :    
        #consoleid = f"stella{num+1}@stclab.com"         
        consoleid = "prod_stella1@stclab.com"   
        password = 'qwe123!!'

        #로그인
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/form/div/div[1]/div[2]/input').send_keys(consoleid)
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/form/div/div[2]/div[2]/input').send_keys(password)
        driver.find_element(By.CLASS_NAME, 'css-19rzuai').click()                                                                   # 로그인 버튼 클릭
        time.sleep(sec)
        if session_storage_data1 == 'true':                 #  테스트 그룹 제외 이벤트 값
            eventori = eventori + 1
        else :
            if session_storage_data2 == groupA :             #  A그룹 이벤트 값
                eventA = eventA + 1
            elif session_storage_data2 == groupB :           #  B그룹 이벤트 값
               eventB = eventB + 1
            elif session_storage_data2 == groupC :           #  C그룹 이벤트 값
                eventC = eventC + 1

    
    # 테스트 그룹 숫자 count
    if session_storage_data1 == 'true':                 #  테스트 그룹 제외
        ori = ori + 1
    else :
        if session_storage_data2 == groupA :             #  A그룹 전체 사용자 수
            numA = numA + 1
        elif session_storage_data2 == groupB :           #  B그룹 전체 사용자 수
            numB = numB + 1
        elif session_storage_data2 == groupC :           #  C그룹 전체 사용자 수
            numC = numC + 1


print('테스트 제외 {} / {}'.format(eventori,ori))
print('원본그룹A {} / {}'.format(eventA, numA))
print('그룹B {} / {}'.format(eventB, numB))
print('그룹C {} / {}'.format(eventC, numC))
print('테스트 완료')
time.sleep(1000)
driver.close