import allure

from demoqa_tests.model.data.user import User
from demoqa_tests.model.pages import practice_form


@allure.title("Test student registration form")
def test_student_registration_form():
    user = User(
        first_name='Pavel',
        last_name='Durov',
        email='durov@mail.ru',
        gender="Male",
        phone='9998887755',
        birthday_month='May',
        birthday_year='1985',
        birthday_day=13,
        subject='English',
        hobby='Sports',
        address='Some address',
        image='resources/durov.jpg',
        state='NCR',
        city='Delhi'
    )
    with allure.step("Filling out the form"):
        userForm.fill(user).submit()
    with allure.step("Form verification"):
        userForm.should_have_registered(user)


userForm = practice_form.UserForm()
