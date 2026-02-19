from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.Base_page import BasePage
from utils.config_reader import get_config


class HomePage(BasePage):



    SIGNUP_LOGIN_BUTTON = (By.CSS_SELECTOR, "a[href='/login']")
    PRODUCTS_BUTTON = (By.XPATH, "//a[@href='/products']")
    LOGOUT_BUTTON = (By.XPATH, "//a[normalize-space()='Logout']")
    DELETE_ACCOUNT_BUTTON = (By.LINK_TEXT, "Delete Account")
    ACCOUNT_DELETED_MESSAGE = (By.XPATH, "//b[normalize-space()='Account Deleted!']")


    # Open Application


    def open_application(self):
        try:
            base_url = get_config().get("base_url")

            assert base_url, "Base URL not found in config.yaml"

            self.driver.get(base_url)
            print("Application launched successfully")

        except Exception as e:
            raise Exception(f"Failed to open application: {str(e)}")


    # Navigate to Login Page


    def go_to_login_page(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.SIGNUP_LOGIN_BUTTON)
            )

            self.click(self.SIGNUP_LOGIN_BUTTON)
            print("Navigated to Login Page")

        except Exception as e:
            raise Exception(f"Failed to navigate to login page: {str(e)}")


    # Navigate to Products Page


    def go_to_products_page(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.PRODUCTS_BUTTON)
            )

            self.click(self.PRODUCTS_BUTTON)
            print("Navigated to Products Page")

        except Exception as e:
            raise Exception(f"Failed to navigate to Products page: {str(e)}")


    # Logout


    def logout(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.LOGOUT_BUTTON)
            )

            self.click(self.LOGOUT_BUTTON)
            print("Logout successful")

        except Exception as e:
            raise Exception(f"Logout failed: {str(e)}")


    # Delete Account


    def delete_account(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.DELETE_ACCOUNT_BUTTON)
            )

            self.click(self.DELETE_ACCOUNT_BUTTON)
            print("Delete Account clicked")

        except Exception as e:
            raise Exception(f"Delete account action failed: {str(e)}")


    # Validate Account Deletion

    def is_account_deleted(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.ACCOUNT_DELETED_MESSAGE)
            )

            message = self.get_text(self.ACCOUNT_DELETED_MESSAGE)

            assert message == "Account Deleted!", \
                f"Unexpected delete message: {message}"

            print("Account Deleted Successfully")

            return True

        except Exception as e:
            raise Exception(f"Account deletion validation failed: {str(e)}")
