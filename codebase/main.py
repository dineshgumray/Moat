import scrapper
import driver_config


def addNewLine(string):
    return "{}\n".format(string)


if __name__ == '__main__':

    url = "https://moat.com/"
    obj = scrapper.Scrapper(driver_config.DRIVER_PATH)

    with open(driver_config.OUTPUT_PATH, "w") as file_write:

        # 1. Verify the search bar autocomplete drop down text.
        obj.open_website(url)
        autocomplete_result = obj.verify_autocomplete("Saturn")
        file_write.write(addNewLine(autocomplete_result))

        # 2. Verify the creative count on the search results page is
        # correct for these 3 search terms: Saturn, Saturday’s Market,
        # and Krux.
        products_list = ["Saturn", "Saturday’s Market", "Krux"]
        for product in products_list:
            obj.open_website(url)
            creative_check_result = obj.verify_creative(product)
            file_write.write(addNewLine(creative_check_result))

        # 3. Verify the “Random Brand” link on the search results
        # page is random.
        obj.open_website("{}advertiser/marketbeat".format(url))
        random_brand_result = obj.verify_random_brand()
        file_write.write(addNewLine(random_brand_result))

        # 4. Verify the “Share” ad feature (it appears on overlay when
        # hovering over an ad).
        obj.open_website("{}advertiser/marketbeat".format(url))
        share_button_result = obj.verify_share_button()
        file_write.write(addNewLine(share_button_result))

        # For closing the website.
        obj.close_website()
