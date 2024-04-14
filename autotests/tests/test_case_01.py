from playwright.sync_api import Page
from autotests.config.url import Url


class TestCase01:
    def test_case_01(self, page: Page) -> None:
        page.goto(Url.DOMAIN)
        page.wait_for_selector(".desktop-impact-items-F7T6E")
        counters = page.query_selector_all(".desktop-impact-item-eeQO3")
        filtered_counters = [counter for i, counter in enumerate(counters) if (i + 1) % 2 == 0]

        for i, counter in enumerate(filtered_counters):
            counter.screenshot(path=f"../../output/test_case_1_counter_{i + 1}.png")
