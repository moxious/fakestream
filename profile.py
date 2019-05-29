from faker import Faker
import random
import json
from streamentry import StreamEntry
from domain import Domain 

fake = Faker()

class Profile(StreamEntry):
    def __init__(self, id, first_name, last_name, gender, street, postal_code, 
        city=fake.city(), 
        country=fake.country(), 
        phone=fake.phone_number(), 
        ssn=fake.ssn()):
        StreamEntry.__init__(self)
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.street = street
        self.postal_code = postal_code
        self.city = city
        self.country = country
        self.phone = phone
        self.ssn = ssn

    @staticmethod
    def create():
        gender = "M" if random.random() >= 0.5 else "F"
        first_name = fake.first_name_male() if gender == "M" else fake.first_name_female()
        last_name = fake.last_name()
        state = fake.state_abbr()
        return Profile(random.randint(1, Domain.CUSTOMERS),
            first_name, last_name, gender,
            fake.street_address(),
            fake.zipcode_in_state(state))
