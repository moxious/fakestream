from faker import Faker
import random
import json
from streamentry import StreamEntry
import datetime
from domain import Domain

fake = Faker()

currencies = ['USD', 'USD', 'USD', 'USD', 'EUR', 'EUR', 'EUR', 'GBP', 'GBP', 'CHF', 'AUD', 'CNY', 'RUB']

class AccountTransfer(StreamEntry):
    def __init__(self, id, from_iban, to_iban, amount, currency, date):
        StreamEntry.__init__(self)
        self.id = id
        self.type = 'accounttransfer'
        self.from_iban = from_iban
        self.to_iban = to_iban
        self.amount = amount
        self.currency = currency
        self.date = date

    @staticmethod
    def create():
        id = random.randint(1, Domain.TRANSFERS)
        from_iban = fake.iban()
        to_iban = fake.iban()
        amount = random.randint(1, 10000000)
        currency = random.choice(currencies)
        date = datetime.datetime.now().isoformat()

        return AccountTransfer(id, from_iban, to_iban, amount, currency, date)
