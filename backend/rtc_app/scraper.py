# backend/scraper.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def fetch_rtc(year):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)
    driver.get("https://landrecords.karnataka.gov.in/Service2/")

    try:
        # Wait and click RTC
        time.sleep(2)
        driver.find_element(By.LINK_TEXT, "View RTC (Pahani)").click()
        time.sleep(2)

        # Select Old Year (Archive RTC)
        driver.find_element(By.ID, "chkOldYear").click()

        # Fill form
        Select(driver.find_element(By.ID, "ddlDistrict")).select_by_visible_text("Bangalore Rural")
        time.sleep(1)
        Select(driver.find_element(By.ID, "ddlTaluk")).select_by_visible_text("Devanahalli")
        time.sleep(1)
        Select(driver.find_element(By.ID, "ddlHobli")).select_by_visible_text("Kasaba")
        time.sleep(1)
        Select(driver.find_element(By.ID, "ddlVillage")).select_by_visible_text("Devanahalli")
        time.sleep(1)

        # Set survey details
        driver.find_element(By.ID, "txtSurveyNo").send_keys("22")
        driver.find_element(By.ID, "txtSurnoc").clear()
        driver.find_element(By.ID, "txtHissaNo").send_keys("1")

        # Select Year
        Select(driver.find_element(By.ID, "ddlOldYears")).select_by_visible_text(year)
        time.sleep(1)

        # Submit
        driver.find_element(By.ID, "btnFetch").click()
        time.sleep(5)

        # Optionally take screenshot
        driver.save_screenshot(f"media/screenshots/rtc_{year}.png")
        print(f"RTC for {year} fetched successfully!")

    except Exception as e:
        print("Error during scraping:", e)

    finally:
        driver.quit()
