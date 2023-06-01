import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Путь к драйверу Chrome WebDriver
driver_path = 'C:\PyProjects\data_analysis\dafiles\chromedriver\chromedriver'

# Функция для спарсинга элемента на странице
def parse_element(url):
    # Создание экземпляра сервиса ChromeDriver
    service = Service(driver_path)

    # Создание экземпляра драйвера Chrome
    driver = webdriver.Chrome(service=service)

    try:
        # Открытие страницы
        driver.get(url)

        # Нахождение элемента на странице
        wait = WebDriverWait(driver, 5)
        element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span.page-title-count-wQ7pG')))

        # Извлечение текста из элемента
        text = element.text

        # Закрытие браузера
        driver.quit()

        return text
    except Exception as e:
        print(f"Ошибка при обработке URL: {url}")
        print(f"Ошибка: {str(e)}")
        driver.quit()
        return '0'  # Возвращаем '0' в случае ошибки

# Функция для обработки CSV файла
def process_csv(input_file, output_file):
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

        for row in rows:
            url = f'https://www.{row[2]}+-%D0%B7%D0%B0%D0%BF%D1%87%D0%B0%D1%81%D1%82%D0%B8+-ddr3+-%2215.6%22&user=1'

            # Парсинг элемента на странице
            parsed_value = parse_element(url)

            row.append(parsed_value)  # Добавление спаршенного значения в список row

    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

# Пример использования
input_file = r'C:\Users\Павел\Desktop\input.csv'  # Входной CSV файл
output_file = r'C:\Users\Павел\Desktop\output.csv'  # Выходной CSV файл

try:
    process_csv(input_file, output_file)
except Exception as e:
    print(f"Ошибка при обработке CSV файла: {str(e)}")
