import os

from selene.support.shared import browser
from selenium.webdriver import Keys

def test_new_form_homework():
    browser.config.browser_name = 'firefox'
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('[id="firstName"]').type('Maksim')
    browser.element('[id="lastName"]').type('Samoshin')
    browser.element('[id="userEmail"]').type('boss.samoshin@mail.ru')
    browser.element('[for="gender-radio-1"').click()
    browser.element('[id="userNumber"]').type(9819740196)

    ##Выбор даты рождения
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('.react-datepicker__month-select').click().element('[value="7"]').click()
    browser.element('.react-datepicker__year-select').click().element('[value="1997"]').click()
    browser.element('.react-datepicker__month-container').element('.react-datepicker__day--006').click()

    browser.element('#subjectsInput').type('Computer Science').press_enter()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').send_keys(os.getcwd() + '\Desktop\я.jpg')
