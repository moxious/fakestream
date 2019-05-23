from faker import Faker
import random
import json
from streamentry import StreamEntry
import datetime

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
        bank_id = random.randint(1, 1000000)
        account_holder = random.randint(1, 1000000)

        return Account(id, iban, bank_id, account_holder)
