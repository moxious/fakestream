from faker import Faker
import random
import json
from streamentry import StreamEntry
import datetime
from domain import Domain
from uuid import uuid4

fake = Faker()

currencies = ['USD', 'USD', 'USD', 'USD', 'EUR', 'EUR', 'EUR', 'GBP', 'GBP', 'CHF', 'AUD', 'CNY', 'RUB']

class AccountTransfer(StreamEntry):
    def __init__(self, id, from_id, to_id, amount, currency, date):
        StreamEntry.__init__(self)
        self.id = id
        self.type = 'accounttransfer'
        self.from_id = from_id
        self.to_id = to_id
        self.amount = amount
        self.currency = currency
        self.date = date

    @staticmethod
    def create():
        id = str(uuid4())
        from_id = Domain.id(Domain.ACCOUNTS)
        to_id = Domain.id(Domain.ACCOUNTS)
        amount = random.randint(1, 10000000)
        currency = random.choice(currencies)
        date = datetime.datetime.now().isoformat()

        return AccountTransfer(id, from_id, to_id, amount, currency, date)
