import os
from selene import browser, have
from selenium.webdriver import Keys

def test_new_form_homework():

    browser.open_url('https://demoqa.com/automation-practice-form')

    ##Заполнение полей
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

    ##Загрузка фото
    browser.element('#uploadPicture').send_keys(os.getcwd() + '/Я.png')

    ##Выбор адреса
    browser.element('#currentAddress').click().type('Stachek 75')

    ##Выбор штата
    browser.element('#state').click()
    browser.element('#react-select-3-option-0').should(have.exact_text('NCR')).click()

    ##Выбор города
    browser.element('#city').click()
    browser.element('#react-select-4-option-0').should(have.exact_text('Delhi')).click()

    browser.element('#submit').click()

    ##Проверка
    browser.all('tbody tr').should(have.texts('Student Name Maksim Samoshin',
                                                           'Student Email boss.samoshin@mail.ru',
                                                           'Gender Male',
                                                           'Mobile 9819740196',
                                                           'Date of Birth 06 August,1997',
                                                           'Subjects Computer Science',
                                                           'Hobbies Music',
                                                           'Picture Я.png',
                                                           'Address Stachek 75',
                                                           'State and City NCR Delhi'))