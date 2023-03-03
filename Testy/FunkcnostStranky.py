from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# seznam ovladačů pro různé prohlížeče
drivers = [
    webdriver.Chrome(),
    webdriver.Firefox(),
    webdriver.Edge(),
    webdriver.Safari()
]

# adresa testované stránky
url = "https://www.example.com"

for driver in drivers:
    driver.get(url)
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        print(f"Stránka se načetla správně na prohlížeči {driver.name}!")
    except:
        print(f"Chyba: Stránka se nenachází na očekávané adrese nebo se nenachází načtená na prohlížeči {driver.name}.")
    finally:
        driver.quit()
