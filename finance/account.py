from faker import Faker
import random
import json
from streamentry import StreamEntry
import datetime
from domain import Domain

fake = Faker()

class Account(StreamEntry):
    def __init__(self, id, iban, bank_id, account_holder):
        StreamEntry.__init__(self)
        self.type = 'account'
        self.id = id
        self.iban = iban
        self.bank_id = bank_id
        self.account_holder = account_holder

    @staticmethod
    def create():
        id = fake.iban()
        iban = id
        bank_id = random.randint(1, Domain.BANKS)
        account_holder = random.randint(1, Domain.CUSTOMERS)

        return Account(id, iban, bank_id, account_holder)
