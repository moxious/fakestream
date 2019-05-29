import json
from faker import Faker
import random
from domain import Domain 

class StreamEntry:
    def __init__(self):
        pass
    
    def __str__(self):
        # Don't include keys starting with _ this lets us store object data
        # without it ending up polluting the final hash.
        d = self.__dict__
        final_dict = {i:d[i] for i in d if not i.startswith('_')}
        return json.dumps(final_dict, indent=3)

class TemplateStreamEntry(StreamEntry):
    def __init__(self, template):
        StreamEntry.__init__(self)
        self.__tmpl = template
    
    def __setitem__(self, key, value):
        self.__dict__[key] = value

    @staticmethod
    def create(template):
        fake = Faker()
        tsl = TemplateStreamEntry(template)
        def make_entry(key):
            if key == 'id':
                val = Domain.id()
            else:
                try:
                    fake_function = fake.__dict__[template[key]]
                except KeyError:
                    raise Exception("Template refers to %s: %s which is not a valid fake function" % (key, template[key]))
                val = fake_function()
            tsl[key] = val

        for key in template.keys():
            make_entry(key)

        return tsl