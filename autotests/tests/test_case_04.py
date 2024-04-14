from playwright.sync_api import Page
from autotests.config.url import Url, API


class TestCase04:
    def test_case_04(self, page: Page) -> None:
        def create_route_function(path):
            return lambda route: route.fulfill(path=path)
        page.route(API.HTTP_REQUEST, create_route_function("../data/json/test_case_4.json"))
        page.goto(Url.DOMAIN)
        page.wait_for_selector(".desktop-impact-items-F7T6E")
        counters = page.query_selector_all(".desktop-impact-item-eeQO3")
        filtered_counters = [counter for i, counter in enumerate(counters) if (i + 1) % 2 == 0]

        for i, counter in enumerate(filtered_counters):
            counter.screenshot(path=f"../../output/test_case_4_counter_{i + 1}.png")
