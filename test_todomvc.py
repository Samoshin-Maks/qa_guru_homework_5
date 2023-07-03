from selene import browser, have, be


def test_complete_todo():
    browser.config.driver_name = "Firefox"
    browser.config.window_width = 1600
    browser.config.window_height = 1600
    browser.config.base_url = 'https://todomvc.com/examples/emberjs'

    browser.open('/')
    browser.should(have.title('Ember TodoMVC'))

    browser.element('[id="new-todo"]').type('a').press_enter()
    browser.element('#new-todo').type('b').press_enter()
    browser.element('#new-todo').type('c').press_enter()

    ...