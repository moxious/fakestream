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
        id = Domain.id(Domain.ACCOUNTS)
        iban = fake.iban()
        bank_id = Domain.id(Domain.BANKS)
        account_holder = Domain.id(Domain.CUSTOMERS)

        return Account(id, iban, bank_id, account_holder)
