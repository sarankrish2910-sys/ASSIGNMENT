
# Required Selenium Imports


from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


# Config Reader


from utils.config_reader import get_config


class DriverFactory:

    # Creates and returns WebDriver instance
    # based on browser mentioned in config.yaml.


    @staticmethod
    def get_driver():

        config = get_config()
        browser = config.get("browser", "chrome").lower()
        headless = config.get("headless", True)

        # ===============================
        # CHROME SETUP
        # ===============================

        if browser == "chrome":

            options = ChromeOptions()

            # Run in headless mode if enabled
            if headless:
                options.add_argument("--headless=new")

            # Start browser maximized
            options.add_argument("--start-maximized")

            driver = webdriver.Chrome(options=options)

        # ===============================
        # FIREFOX SETUP
        # ===============================

        elif browser == "firefox":

            options = FirefoxOptions()

            if headless:
                options.add_argument("--headless")

            driver = webdriver.Firefox(options=options)

        else:
            raise Exception(f"Browser '{browser}' is not supported.")

        # Clear cookies before starting
        driver.delete_all_cookies()

        return driver
