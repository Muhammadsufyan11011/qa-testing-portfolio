
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"


def test_valid_login():
    driver = webdriver.Chrome()

    try:
        wait = WebDriverWait(driver, 10)
        driver.get(URL)

        wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        ).send_keys(USERNAME)

        driver.find_element(By.ID, "password").send_keys(PASSWORD)
        driver.find_element(By.ID, "login-button").click()

        wait.until(EC.url_contains("inventory.html"))

        assert wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "title"))
        ).text == "Products"

        print("PASS: Valid Login")

    finally:
        driver.quit()


def test_invalid_login():
    driver = webdriver.Chrome()

    try:
        wait = WebDriverWait(driver, 10)
        driver.get(URL)

        wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        ).send_keys(USERNAME)

        driver.find_element("id", "password").send_keys(
            "WrongPassword123"
        )
        driver.find_element(By.ID, "login-button").click()

        error = wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "[data-test='error']")
            )
        )

        assert error.is_displayed()
        print("PASS: Invalid Login Rejected")

    finally:
        driver.quit()


def test_add_to_cart():
    driver = webdriver.Chrome()

    try:
        wait = WebDriverWait(driver, 10)
        driver.get(URL)

        wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        ).send_keys(USERNAME)

        driver.find_element(By.ID, "password").send_keys(PASSWORD)
        driver.find_element(By.ID, "login-button").click()

        wait.until(
            EC.element_to_be_clickable(
                (By.ID, "add-to-cart-sauce-labs-backpack")
            )
        ).click()

        badge = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "shopping_cart_badge")
            )
        )

        assert badge.text == "1"
        print("PASS: Add to Cart")

    finally:
        driver.quit()

def test_checkout():
    driver = webdriver.Chrome()

    try:
        wait = WebDriverWait(driver, 10)
        driver.get(URL)

        wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        ).send_keys(USERNAME)

        driver.find_element(By.ID, "password").send_keys(PASSWORD)
        driver.find_element(By.ID, "login-button").click()

        wait.until(
            EC.element_to_be_clickable(
                (By.ID, "add-to-cart-sauce-labs-backpack")
            )
        ).click()

        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        ).click()

        wait.until(
            EC.visibility_of_element_located((By.ID, "first-name"))
        ).send_keys("Sufyan")

        driver.find_element(By.ID, "last-name").send_keys("Ahmed")
        driver.find_element(By.ID, "postal-code").send_keys("75500")
        driver.find_element(By.ID, "continue").click()

        wait.until(EC.url_contains("checkout-step-two.html"))

        assert driver.find_element(
            By.CLASS_NAME, "title"
        ).text == "Checkout: Overview"

        print("PASS: Checkout test")

    finally:
        driver.quit()


if __name__ == "__main__":
    tests = [
        test_valid_login,
        test_invalid_login,
        test_add_to_cart,
         test_checkout,
    ]

    passed = 0
    failed = 0

    for test in tests:
        try:
            test()
            passed += 1
        except Exception as error:
            failed += 1
            print(f"FAIL: {test.__name__}: {error}")

    print("\n===== TEST SUMMARY =====")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    print(f"Total:  {passed + failed}")
