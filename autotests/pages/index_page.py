from playwright.sync_api import Page
from autotests.config.url import Url


class IndexPage:

    def open_index_page(self, page:Page) -> None:
        page.goto(Url.DOMAIN)