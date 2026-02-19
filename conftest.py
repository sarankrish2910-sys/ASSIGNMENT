import pytest
import os
import allure
from datetime import datetime
from Drivers.Driver_Factory import DriverFactory



# Driver Fixture


@pytest.fixture(scope="function")
def driver():
    """
    Pytest fixture for browser setup and teardown.
    """

    driver = DriverFactory.get_driver()
    driver.maximize_window()

    yield driver

    driver.quit()


# Screenshot on Failure Hook


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    ##Capture screenshot on test failure
    ##and attach it to Allure report.


    outcome = yield
    report = outcome.get_result()

    # Capture screenshot for setup or test failure
    if report.when in ["call", "setup"] and report.failed:

        driver = item.funcargs.get("driver", None)

        if driver:

            # create ss folder
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_name = f"{item.name}_{timestamp}.png"
            screenshot_path = os.path.join(screenshots_dir, screenshot_name)

            driver.save_screenshot(screenshot_path)

            # Attach screenshot to Allure
            allure.attach.file(
                screenshot_path,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )
