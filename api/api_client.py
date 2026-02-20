import requests


class APIClient:

    BASE_URL = "https://automationexercise.com/api"

    @staticmethod
    def get_products():

        # Fetch products list from API.
        # Returns list of products.
        #

        url = f"{APIClient.BASE_URL}/productsList"

        response = requests.get(url)

        if response.status_code != 200:
            raise Exception(
                f"API request failed. Status Code: {response.status_code}"
            )

        data = response.json()

        if data.get("responseCode") != 200:
            raise Exception(
                f"Unexpected API response code: {data.get('responseCode')}"
            )

        products = data.get("products")

        if not products:
            raise Exception("No products found in API response")

        return products
