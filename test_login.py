
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_valid_login():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com/")

        wait = WebDriverWait(driver, 10)

        # Enter username
        wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        ).send_keys("standard_user")

        # Enter password
        driver.find_element(By.ID, "password").send_keys("secret_sauce")

        # Click login
        driver.find_element(By.ID, "login-button").click()

        # Verify successful login
        wait.until(EC.url_contains("inventory.html"))

        assert "Products" in wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "title"))
        ).text

        print("PASS: Valid login successful!")
        print("Browser 30 seconds tak open rahega.")

        time.sleep(30)

    except Exception as error:
        print(f"FAIL: Login test failed: {error}")
        raise

    finally:
        driver.quit()


if __name__ == "__main__":
    test_valid_login()
