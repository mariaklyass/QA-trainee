import time

from autotests.pages import index_page


class TestIndexPage:

    def test_index_page_opens(self, page):
        index_page.open_index_page(page)
