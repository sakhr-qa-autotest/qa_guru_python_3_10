from selene import have
from selene.support.shared import browser

from demoqa_tests.model.controls import checkbox
from demoqa_tests.model.controls import datepicker
from demoqa_tests.model.controls import dropdown
from demoqa_tests.model.controls import radiobutton
from demoqa_tests.model.data.user import User
from demoqa_tests.utils import path_to_file
from demoqa_tests.utils.scroll import scroll_to


class UserForm:
    def fill(self, user: User):
        self.__given_opened('https://demoqa.com/automation-practice-form')
        self.__required_fields(user.first_name, user.last_name, user.email)
        self.__select_gender(user.gender)
        self.__type_phone_number(user.phone)
        self.__click_on_datepicker()
        self.__pick_month(user.birthday_month)
        self.__pick_year(user.birthday_year)
        self.__pick_day(user.birthday_day)
        self.__type_subject(user.subject)
        self.__select_hobby(user.hobby)
        self.__scroll_to_address()
        self.__type_address(user.address)
        self.__upload_picture(user.image)
        self.__select_state(user.state)
        self.__select_city(user.city)
        return self

    def should_have_registered(self, user: User):
        self.__assert_fields(
            user.name(),
            user.email,
            user.gender,
            user.phone,
            user.full_birthday(),
            user.subject,
            user.hobby,
            user.image.replace('resources/', ''),
            user.address,
            user.geo()
        )

    def submit(self):
        browser.element('#submit').press_enter()

    def __given_opened(self, open: str):
        browser.config.window_width = 1500
        browser.config.window_height = 1500
        browser.open(open)

    def __select_state(self, value):
        dropdown.Dropdown.select('#state', by_text=value)

    def __select_city(self, value):
        dropdown.Dropdown.select('#city', by_text=value)

    def __required_fields(self, firstname, lastname, email):
        browser.element('#firstName').type(firstname)
        browser.element('#lastName').type(lastname)
        browser.element('#userEmail').type(email)

    def __type_phone_number(self, text):
        browser.element('#userNumber').type(text)

    def __type_address(self, text):
        browser.element('#currentAddress').type(text)

    def __select_gender(self, gender):
        radiobutton.Radiobutton.gender('[name=gender]', gender)

    def __select_hobby(self, hobby):
        checkbox.Checkbox.hobby('[for^=hobbies-checkbox]', hobby)

    def __pick_month(self, month):
        browser.element('.react-datepicker__month-select').click()
        datepicker.Datepicker.date('.react-datepicker__month-select', month)

    def __pick_year(self, year):
        browser.element('.react-datepicker__year-select').click()
        datepicker.Datepicker.date('.react-datepicker__year-select', year)

    def __pick_day(self, day):
        browser.element(f'.react-datepicker__day--0{day}').click()

    def __click_on_datepicker(self):
        browser.element('#dateOfBirthInput').click()

    def __type_subject(self, subject):
        browser.element('#subjectsInput').type(subject).press_enter()

    def __upload_picture(self, path_to_picture):
        path_to_file.create_path('#uploadPicture', path_to_picture)

    def __assert_fields(self, *args):
        browser.element('.table').all('td').even.should(have.texts(args))

    def __scroll_to_address(self):
        scroll_to('#currentAddress')
