from faker import Faker
import random
import json
from streamentry import StreamEntry
import datetime
from domain import Domain

fake = Faker()

class Purchase(StreamEntry):
    def __init__(self, id, customer_id, product_id, company_id, date, quantity):
        StreamEntry.__init__(self)
        self.id = id
        self.customer_id = customer_id
        self.product_id = product_id
        self.company_id = company_id
        self.date = date
        self.quantity = quantity
        self.type = 'purchase'

    @staticmethod
    def create():
        id = Domain.id(Domain.PURCHASES)
        customer_id = Domain.id(Domain.CUSTOMERS)
        product_id = Domain.id(Domain.PRODUCTS)
        company_id = Domain.id(Domain.COMPANIES)
        date = datetime.datetime.now().isoformat()
        quantity = random.randint(1, 10)

        return Purchase(id, customer_id, product_id, company_id, date, quantity)
