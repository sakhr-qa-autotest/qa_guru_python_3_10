from selene import command
from selene.support.shared import browser


def scroll_to(selector):
    browser.element(selector).perform(command.js.scroll_into_view)
