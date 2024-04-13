from playwright.sync_api import Page
from autotests.config.url import Url


class IndexPage:
    # _BUTTON_GOOGLE_SEARCH = "//div[@class='FPdoLc lJ9FBc']//input[@name='btnK']"

    def open_index_page(self, page:Page) -> None:
        page.goto(Url.DOMAIN)
        page.wait_for_selector(".desktop-impact-items-F7T6E")
        counters = page.query_selector_all(".desktop-impact-item-eeQO3")
        filtered_counters = [counter for i, counter in enumerate(counters) if (i + 1) % 2 == 0]
        page.route("**/fetch-counter-data", lambda route, request: intercept_counter_data(route, counter))

        for i, counter in enumerate(filtered_counters):
            counter.screenshot(path=f"../../output/test1_counter_{i + 1}.png")
            print("Base screenshot saved")

        def intercept_counter_data(route, counter):
            # Set the desired value for the intercepted counter data
            counter_data = {"value": 1000}

            # Fulfill the intercepted request with the modified counter data
            route.fulfill(status=200, status_text="OK", content_type="application/json", body=json.dumps(counter_data))




