from faker import Faker
import random
import json
from product.company import Company
import datetime
from domain import Domain

fake = Domain.faker()

class Bank(Company):
    def __init__(self, id, name, suffix, tagline, country):
        Company.__init__(self, id, name, suffix, tagline, country)
        self.type = 'bank'

    @staticmethod
    def create():
        co = Company.create()

        return Bank(co.id, co.name, co.suffix, co.tagline, co.country)
