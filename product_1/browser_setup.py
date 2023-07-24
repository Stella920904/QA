import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="module")
def browser():
    # options = Options()
    # options = webdriver.ChromeOptions()
    # options.add_argument("--window-size=1920,1080")
    # options.add_argument("--headless")
    # driver = webdriver.Chrome(executable_path_='/Users/stclab/Documents/GitHub/STCLab_QA/drivers/chromedriver')
   # driver = webdriver.Chrome(ChromeDriverManager().install())
    # driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    # driver = webdriver.Chrome(ChromeDriverManager(version="114.0.5735.90").install())
    
    options = webdriver.ChromeOptions()
    options.add_argument("executable_path=/Users/stclab/Documents/GitHub/STCLab_QA/drivers/chromedriver")
    driver = webdriver.Chrome(options=options)
    
    yield driver


    driver.quit()
