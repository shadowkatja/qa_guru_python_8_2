from selene.support.shared import browser
from selene import be, have
import pytest

@pytest.fixture()
def browser_settings():
    browser.config.window_width = 1920
    browser.config.window_height = 1020

def test_google_should_have(browser_settings):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))