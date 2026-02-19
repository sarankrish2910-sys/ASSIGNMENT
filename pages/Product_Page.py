from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.Base_page import BasePage


class ProductsPage(BasePage):

    # Product Detail Page Locators
    PRODUCT_NAME = (By.XPATH, "//div[@class='product-information']/h2")
    PRODUCT_PRICE = (By.XPATH, "//div[@class='product-information']/span/span")
    PRODUCT_CATEGORY = (By.XPATH, "//div[@class='product-information']/p[1]")

    VIEW_PRODUCTS = (By.LINK_TEXT, "View Product")

    MEN_EXPAND = (By.XPATH, "//a[normalize-space()='Men']")
    TSHIRT = (By.XPATH, "//a[normalize-space()='Tshirts']")

    WOMEN_EXPAND = (By.XPATH, "//a[normalize-space()='Women']")
    SAREE = (By.XPATH, "//a[normalize-space()='Saree']")
    CART =(By.XPATH, "//a[normalize-space()='Cart']")

    VIEW_PRODUCTS = (By.LINK_TEXT, "View Product")
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[normalize-space()='Add to cart']")
    CONTINUE_SHOPPING_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Continue Shopping']"
    )


    # API USE CASE METHODS



    def open_product_by_name(self, product_name):

        product_locator = (
            By.XPATH,
            f"//p[text()='{product_name}']/ancestor::div[@class='product-image-wrapper']//a[text()='View Product']"
        )

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(product_locator)
        )

        self.click(product_locator)
        print(f"Opened product in UI: {product_name}")


    # Get Product Details From UI


    def get_product_details(self):

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.PRODUCT_NAME)
        )

        name = self.get_text(self.PRODUCT_NAME)
        price = self.get_text(self.PRODUCT_PRICE)
        category = self.get_text(self.PRODUCT_CATEGORY)

        print("\nUI Product Details:")
        print("Name:", name)
        print("Price:", price)
        print("Category:", category)

        return {
            "name": name,
            "price": price,
            "category": category
        }
    def add_men_and_women_products(self):

        try:

            #  MEN FLOW

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.MEN_EXPAND)
            )
            self.click(self.MEN_EXPAND)
            print("Clicked Men category")

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.TSHIRT)
            )
            self.click(self.TSHIRT)
            print("Selected Tshirts under Men")

            first_product = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.VIEW_PRODUCTS)
            )
            first_product.click()
            print("Opened first Men product")

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON)
            )
            self.click(self.ADD_TO_CART_BUTTON)
            print("Added Men product to cart")

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.CONTINUE_SHOPPING_BUTTON)
            )
            self.click(self.CONTINUE_SHOPPING_BUTTON)
            print("Clicked Continue Shopping")


            #  WOMEN FLOW


            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.WOMEN_EXPAND)
            )
            self.click(self.WOMEN_EXPAND)
            print("Clicked Women category")

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.SAREE)
            )
            self.click(self.SAREE)
            print("Selected Saree under Women")

            first_product = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.VIEW_PRODUCTS)
            )
            first_product.click()
            print("Opened first Women product")

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON)
            )
            self.click(self.ADD_TO_CART_BUTTON)
            print("Added Women product to cart")

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.CONTINUE_SHOPPING_BUTTON)
            )
            self.click(self.CONTINUE_SHOPPING_BUTTON)
            print("Clicked Continue Shopping")

            print("Successfully added Men and Women products")

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.CART)
            )
            self.click(self.CART)
            print("Navigated to Cart")

        except Exception as e:
            raise Exception(f"Adding Men & Women products failed: {str(e)}")

        # def go_to_cart(self):
        #     WebDriverWait(self.driver, 10).until(
        #         EC.element_to_be_clickable(self.CART)
        #     )
        #     self.click(self.CART)
        #     print("Navigated to Cart")

