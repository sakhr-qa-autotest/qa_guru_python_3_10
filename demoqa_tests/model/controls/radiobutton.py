from selene import have
from selene.support.shared import browser


class Radiobutton:
    @staticmethod
    def gender(selector, value):
        browser.all(selector).element_by(have.value(value)).element('..').click()
