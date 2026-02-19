import random
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.Base_page import BasePage


class AuthPage(BasePage):

    # Signup Section
    NAME_INPUT = (By.XPATH, "//input[@placeholder='Name']")
    EMAIL_INPUT = (By.XPATH, "//input[@data-qa='signup-email']")
    SIGNUP_BUTTON = (By.XPATH, "//button[@data-qa='signup-button']")

    #  Registration Form
    GENDER_MR = (By.ID, "id_gender1")
    GENDER_MRS = (By.ID, "id_gender2")
    PASSWORD = (By.ID, "password")
    DAYS = (By.ID, "days")
    MONTHS = (By.ID, "months")
    YEARS = (By.ID, "years")

    FIRST_NAME = (By.ID, "first_name")
    LAST_NAME = (By.ID, "last_name")
    COMPANY = (By.ID, "company")
    COUNTRY = (By.ID, "country")
    ADDRESS = (By.ID, "address1")
    STATE = (By.ID, "state")
    CITY = (By.ID, "city")
    ZIPCODE = (By.ID, "zipcode")
    MOBILE_NUMBER = (By.ID, "mobile_number")

    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[@data-qa='create-account']")
    ACCOUNT_CREATED_MESSAGE = (By.XPATH, "//b[normalize-space()='Account Created!']")
    CONTINUE_BUTTON = (By.LINK_TEXT, "Continue")

    #  Login Section
    LOGIN_EMAIL = (By.XPATH, "//input[@data-qa='login-email']")
    LOGIN_PASSWORD = (By.XPATH, "//input[@placeholder='Password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@data-qa='login-button']")
    LOGOUT_BUTTON = (By.XPATH, "//a[normalize-space()='Logout']")





    def random_string(self, length=5):
        return ''.join(random.choices(string.ascii_letters, k=length)) # IT will generate random letters like AbcDe LIMIT givena as 5 so only 5 characters

    def random_digits(self, length=5):
        return ''.join(random.choices(string.digits, k=length))  # it will This will generate random number like 12345 limit here also give 5


    # Signup Flow


    def signup(self):
        try:
            name = self.random_string(5)  ## it will create random name and email so every run new user is created
            email = f"{name}@test.com"

            self.enter_text(self.NAME_INPUT, name)
            self.enter_text(self.EMAIL_INPUT, email)
            self.click(self.SIGNUP_BUTTON)

            print(f"Signup initiated for: {email}")

            return name, email

        except Exception as e:
            raise Exception(f"Signup failed: {str(e)}")


    # Registration Form


    def complete_registration(self, name):
        try:
            self.click(random.choice([self.GENDER_MR, self.GENDER_MRS]))  ## randomly it will click between 2 radio button

            password = self.random_digits(5)  ## here random 5 digit password will be generated
            self.enter_text(self.PASSWORD, password)

            Select(self.driver.find_element(*self.DAYS)).select_by_index(5)
            Select(self.driver.find_element(*self.MONTHS)).select_by_index(5)
            Select(self.driver.find_element(*self.YEARS)).select_by_visible_text("1997")

            self.enter_text(self.FIRST_NAME, name)
            self.enter_text(self.LAST_NAME, name)
            self.enter_text(self.COMPANY, self.random_string(10))

            random_address = f"{self.random_digits(3)} {self.random_string(6)} Street"
            self.enter_text(self.ADDRESS, random_address)

            Select(self.driver.find_element(*self.COUNTRY)).select_by_visible_text("India")

            self.enter_text(self.STATE, "TamilNadu")
            self.enter_text(self.CITY, "Chennai")
            self.enter_text(self.ZIPCODE, self.random_digits(6))
            self.enter_text(self.MOBILE_NUMBER, self.random_digits(10))

            self.click(self.CREATE_ACCOUNT_BUTTON)

            print("Registration form submitted successfully")

            return password

        except Exception as e:
            raise Exception(f"Registration form submission failed: {str(e)}")

    def is_account_created(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.ACCOUNT_CREATED_MESSAGE)
            )  ## waits untill account is created message appears

            message = self.get_text(self.ACCOUNT_CREATED_MESSAGE)
            assert message == "Account Created!", "Account creation failed"

            print("Account Created Successfully")

            return True

        except Exception as e:
            raise Exception(f"Account creation validation failed: {str(e)}")

    def click_continue(self):
        try:
            self.click(self.CONTINUE_BUTTON)
            print("Clicked Continue button")
        except Exception as e:
            raise Exception(f"Continue button click failed: {str(e)}")


    # Login


    def login(self, email, password):
        try:
            self.enter_text(self.LOGIN_EMAIL, email)
            self.enter_text(self.LOGIN_PASSWORD, password)
            self.click(self.LOGIN_BUTTON)

            # Assert login success by checking Logout button
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.LOGOUT_BUTTON)
            )

            print("Login Successful")
            assert True

        except Exception as e:
            raise Exception(f"Login failed: {str(e)}")
