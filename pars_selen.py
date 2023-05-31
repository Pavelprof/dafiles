from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Путь к драйверу Chrome WebDriver
driver_path = 'C:\PyProjects\data_analysis\dafiles\chromedriver\chromedriver'

# Создание экземпляра сервиса ChromeDriver
service = Service(driver_path)

# Создание экземпляра драйвера Chrome
driver = webdriver.Chrome(service=service)

# Открытие страницы
driver.get('https://www.avito.ru/moskva/noutbuki?f=ASgCAQECAUCo5A1E0Nlm1NlmwNlmttlmAUXGmgwZeyJmcm9tIjoxMjgwMCwidG8iOjMzNzAwfQ&geoCoords=55.715297%2C37.564529&q=8250u+-%D0%B7%D0%B0%D0%BF%D1%87%D0%B0%D1%81%D1%82%D0%B8+-%2215.6%22+-ddr3&radius=25&searchRadius=25&user=1')

# Поиск элемента
wait = WebDriverWait(driver, 5)
element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span.page-title-count-wQ7pG')))

# Извлечение текста из элемента
text = element.text

print(text)

# Закрытие браузера
driver.quit()
