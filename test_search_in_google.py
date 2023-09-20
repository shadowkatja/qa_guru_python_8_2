from selene.support.shared import browser
from selene import be, have
def test_google_should_have():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))

def test_google_should_not_have():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('axkbxabcnocanpc').press_enter()
    browser.element('#result-stats').should(have.text('Результатов: примерно 0'))