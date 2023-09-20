import pytest
from selene.support.shared import browser
@pytest.fixture()
def browser_settings(scope='session', autouse=True):
    browser.config.window_width = 1920
    browser.config.window_height = 1020
    yield
    browser.quit()