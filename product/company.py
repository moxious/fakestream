from faker import Faker
import random
import json
from streamentry import StreamEntry
from domain import Domain 

fake = Faker()

class Company(StreamEntry):
    def __init__(self, id, name, suffix, tagline, country):
        self.id = id
        self.name = name
        self.suffix = suffix
        self.tagline = tagline
        self.country = country
        self.type = 'company'

    @staticmethod
    def create():
        return Company(
            random.randint(1, Domain.COMPANIES),
            fake.company(),
            fake.company_suffix(),
            fake.catch_phrase() + ' / ' + fake.bs(),
            fake.country())