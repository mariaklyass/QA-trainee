import time
from autotests import pages


class TestIndexPage:

    def test_index_page(self, page):
        pages.index_page.open_index_page(page)
        time.sleep(5)