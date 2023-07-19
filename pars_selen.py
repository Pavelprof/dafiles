import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config import PARS_LINK_PT1, PARS_LINK_PT2

driver_path = 'C:\PyProjects\data_analysis\dafiles\chromedriver\chromedriver'

def parse_element(url):

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get(url)
        if driver.current_url != url:
            print(f"Редирект на новую страницу: {driver.current_url}")
            driver.quit()
            return '0'
        else:
            wait = WebDriverWait(driver, 5)
            element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span.page-title-count-wQ7pG')))
            text = element.text
            driver.quit()
            return text

    except TimeoutException:
        print(f"TimeoutException")
        driver.quit()
        return '0'
    except Exception as e:
        print(f"Ошибка при обработке URL: {url}")
        print(f"Ошибка: {str(e)}")
        driver.quit()
        return '0'

def process_csv(input_file, output_file):
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

        for row in rows:
            url = f'{PARS_LINK_PT1}{row[2]}{PARS_LINK_PT2}'
            parsed_value = parse_element(url)
            row.append(parsed_value)

    try:
        with open(output_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

    except Exception as e:
        print(f"Ошибка при записи данных: {str(e)}")
        print(rows)

input_file = r'C:\Users\Павел\Desktop\input.csv'
output_file = r'C:\Users\Павел\Desktop\output.csv'

process_csv(input_file, output_file)