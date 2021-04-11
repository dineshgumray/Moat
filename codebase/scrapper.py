from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time


class Scrapper:
    def __init__(self, path):
        self.browser = webdriver.Chrome(path)

    def close_website(self):
        self.browser.quit()

    def open_website(self, home_address):
        self.browser.maximize_window()
        self.browser.implicitly_wait(5)
        self.browser.get(home_address)

    def search(self, by_type, by_element):
        """

        :param by_type:
        :param by_element:
        :return:
        """
        if by_type == "id":
            return self.browser.find_element_by_id(by_element)
        elif by_type == "xpath":
            return self.browser.find_element_by_xpath(by_element)
        elif by_type == "class":
            return self.browser.find_element_by_class_name(by_element)
        else:
            return "Need to Figure Out!"

    def verify_autocomplete(self, product):
        # 1. Verify the search bar autocomplete drop down text.
        """
        We well valiadte that the search bar is autocomplete by
        checking the number of elements present in drop_down box.

        :param product:
            It is the product element whose details we need to capture.

        :return:
            It returns a string statement which states autocomplete is
            done or not.

        """
        try:
            result = "Autocomplete is not done."
            search_element = self.search("id", "adsearch-input")
            search_element.send_keys(product)
            time.sleep(2)
            search_element = self.search("id", "adsearch-dropdown")
            drop_down_list = search_element.text
            if len(drop_down_list) > 0:
                result = "Autocomplete is done."
            return result

        except Exception:
            self.browser.quit()

    def verify_creative(self, creative):
        # 2. Verify the creative count on the search results page is correct for
        # these 3 search terms: Saturn, Saturday’s Market, and Krux.
        """
        Will compare the creative count elements present on search results
        page by comparing the available "creative count" details on page
        with sum of ad/creative present on the page.

        :param creative:
            It is the product element whose details we need to capture.

        :return:
            It returns a string statement which gives the creative count
            result to be correct or not when compare with loaded ads.

        """
        try:
            result = "Creative count looks to be not correct."
            search_element = self.search("id", "adsearch-input")
            search_element.send_keys(creative)
            select = self.search(
                'xpath',
                '//*[@id="adsearch-dropdown"]/div/div[1]/a/div/span/div/span')
            select.click()

            creative_count = self.search("class", "creative-count")
            creative_count = creative_count.text
            creative_count = int(creative_count.split()[0])
            try:
                for i in range(6):
                    load_more = self.search("class", "er-load-more")
                    load_more.click()
                    time.sleep(10)

            except Exception:
                pass

            finally:
                creative_elements1 = len(self.browser.find_elements_by_class_name(
                    "er-creative-container"))
                creative_elements2 = len(self.browser.find_elements_by_class_name(
                    "er-combined-creative-container"))
                creative_elements = creative_elements1 + creative_elements2
                if creative_count == creative_elements:
                    result = "Creative count are correct for {}.".format(creative)
                return result

        except Exception:
            self.browser.quit()

    def verify_random_brand(self):
        # 3. Verify the “Random Brand” link on the search results
        # page is random.
        """

        Capturing the Brand name of current search results page to compare it
        with Brand name getting after clicking Random Brand button.

        :return:
            It returns a string statement which states random logic for
            "Random Brand" button is working fine or not.

        """
        try:
            result = "Random Brand links are not random."
            brand_name1 = self.search("class", "entity-label")
            random_brand_button = self.search(
                "xpath",
                '//*[@id="main-nav"]/div[1]/div[1]/a[2]')
            random_brand_button.click()
            brand_name2 = self.search("class", "entity-label")
            if brand_name1 != brand_name2:
                result = "Random Brand links are random."
            return result

        except Exception:
            self.browser.quit()

    def verify_share_button(self):
        # 4. Verify the “Share” ad feature (it appears on overlay when
        # hovering over an ad).
        """

        Creating a dictionary to capture the status of Share ad appear/not.
        "Key" is the ad/creative number on the page.
        "Value" is the status of appearance of Share ad.

        :return:
            It returns a dictionary of elements stating Share button
            appeared or not by "Yes/No" values with ad position on page.

        """
        try:
            share_ad_status = {}
            count = 0
            creative_list = self.browser.find_elements_by_class_name(
                "er-creative-container")
            for creative in creative_list:
                creative.click()
                try:
                    element = self.search(
                        "xpath",
                        '//*[@id="er-app"]/div/div[4]/div[1]/div[1]/div[4]/div/div/a')
                    element.click()
                    close = self.browser.find_elements_by_class_name(
                        "close-button")
                    close[1].click()
                    count += 1
                    share_ad_status[count] = "Yes"
                except Exception:
                    share_ad_status[count] = "No"

            return share_ad_status

        except Exception:
            self.browser.quit()