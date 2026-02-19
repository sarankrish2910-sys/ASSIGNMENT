from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.Base_page import BasePage


class CartPage(BasePage):

    CART_ROWS = (By.XPATH, "//tr[contains(@id,'product')]")
    GRAND_TOTAL = (By.XPATH, "//p[@class='cart_total_price']")
    CHECK_OUT = (By.XPATH, "//a[normalize-space()='Proceed To Checkout']")

    def proceed_and_validate_cart(self):

        # 1. Click Proceed To Checkout
        # 2. Validate cart row totals
        # 3. Compare with grand total
        #

        try:

            # Step 1: Click Proceed To Checkout

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.CHECK_OUT)
            )

            self.click(self.CHECK_OUT)


            # Step 2: Validate Cart Details

            rows = self.find_elements(self.CART_ROWS)

            if not rows:  # If no products found, something is wrong
                raise Exception("No products found in cart.")

            row_totals = []  # We will store each product total here

            for row in rows:

                # Product Name
                name = row.find_element(
                    By.XPATH, ".//td[@class='cart_description']//h4/a"
                ).text

                # Price
                price = row.find_element(
                    By.XPATH, ".//td[@class='cart_price']/p"
                ).text

                # Quantity
                quantity = row.find_element(
                    By.XPATH, ".//td[@class='cart_quantity']/button"
                ).text

                # Row Total
                total_text = row.find_element(
                    By.XPATH, ".//td[@class='cart_total']/p"
                ).text

                total = int(total_text.replace("Rs. ", ""))  #Convert total from string to integer

                row_totals.append(total)

                print("Product Name:", name)
                print("Price:", price)
                print("Quantity:", quantity)
                print("Row Total:", total_text)
                print("----------------------------")


            # Step 3: Validate Grand Total

            calculated_total = sum(row_totals)

            grand_total_elements = self.find_elements(self.GRAND_TOTAL)

            if not grand_total_elements:
                raise Exception("Grand total element not found.")

            grand_total_text = grand_total_elements[-1].text
            displayed_total = int(grand_total_text.replace("Rs. ", ""))

            print("Calculated Grand Total:", calculated_total)
            print("Displayed Grand Total:", displayed_total)

            if calculated_total != displayed_total:
                raise Exception(
                    f"Cart total mismatch. Calculated: {calculated_total}, Displayed: {displayed_total}"
                )

        except Exception as e:
            raise Exception(f"Checkout and cart validation failed: {str(e)}")