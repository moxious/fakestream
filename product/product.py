from faker import Faker
import random
import json
from streamentry import StreamEntry

fake = Faker()

class Product(StreamEntry):
    def __init__(self, id=random.randint(1, 1000000),
        name=' '.join(list(map(lambda e: e.capitalize(), fake.words(nb=2, ext_word_list=None, unique=False)))),
        version=1, 
        color=fake.color_name(), 
        url=fake.url(), 
        product_code=fake.ean8()):
        self.id = id
        self.name = name
        self.version = version
        self.color = color
        self.url = url
        self.product_code = product_code
        self.type = 'product'

    @staticmethod
    def create():
        id = random.randint(1, 1000000)
        name = ' '.join(list(map(lambda e: e.capitalize(), fake.words(nb=2, ext_word_list=None, unique=False))))
        version = 1
        color = fake.color_name()
        url = fake.url()
        product_code = fake.ean8()

        return Product(id, name, version, color, url, product_code)
