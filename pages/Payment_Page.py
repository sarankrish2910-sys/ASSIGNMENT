import random
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.Base_page import BasePage


class PaymentPage(BasePage):




    PLACE_ORDER = (By.LINK_TEXT, "Place Order")
    NAME_ON_CARD = (By.NAME, "name_on_card")
    CARD_NUMBER = (By.NAME, "card_number")
    CVC = (By.NAME, "cvc")
    EXPIRY_MONTH = (By.NAME, "expiry_month")
    EXPIRY_YEAR = (By.NAME, "expiry_year")
    PAY_BUTTON = (By.ID, "submit")

    SUCCESS_MESSAGE = (
        By.XPATH,
        "//p[normalize-space()='Congratulations! Your order has been confirmed!']"
    )


    # Helper Method


    def generate_random_digits(self, length):
        return ''.join(random.choices(string.digits, k=length))


    # Payment Flow


    def make_payment_and_validate(self):
        """
        Fill payment form, submit, and validate success message.
        """

        try:
            # Wait and click Place Order
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.PLACE_ORDER)
            )
            self.click(self.PLACE_ORDER)
            print("Clicked Place Order")

            # Wait for payment form to be visible
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.NAME_ON_CARD)
            )

            # Fill payment details
            self.enter_text(self.NAME_ON_CARD, "Test User")
            self.enter_text(self.CARD_NUMBER, self.generate_random_digits(15))
            self.enter_text(self.CVC, self.generate_random_digits(4))
            self.enter_text(self.EXPIRY_MONTH, "12")
            self.enter_text(self.EXPIRY_YEAR, "2028")

            print("Entered payment details")

            # Click Pay
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.PAY_BUTTON)
            )
            self.click(self.PAY_BUTTON)

            # Wait for success message
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
            )

            success_text = self.get_text(self.SUCCESS_MESSAGE)

            print("Payment Confirmation Message:", success_text)

            assert success_text == \
                "Congratulations! Your order has been confirmed!", \
                f"Unexpected confirmation message: '{success_text}'"

            print("Payment Successful")

        except Exception as e:
            raise Exception(f"Payment process failed: {str(e)}")
