from selene import have
from selene.support.shared import browser


class Checkbox:
    @staticmethod
    def hobby(selector, value):
        browser.all(selector).element_by(have.text(value)).click()
