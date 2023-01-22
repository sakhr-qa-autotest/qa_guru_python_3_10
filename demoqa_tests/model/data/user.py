from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone: str
    birthday_year: str
    birthday_month: str
    birthday_day: int
    subject: str
    hobby: str
    image: str
    address: str
    state: str
    city: str

    def __int__(self):
        pass

    def name(self) -> str:
        return self.first_name + " " + self.last_name

    def geo(self) -> str:
        return self.state + " " + self.city

    def full_birthday(self) -> str:
        return str(self.birthday_day) + " " + self.birthday_month + ',' + self.birthday_year
