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
        fake = Domain.faker()
        tsl = TemplateStreamEntry(template)

        def fake_a_value(tmpl_val):
            try:
                fake_function = fake.__dict__[tmpl_val]
            except KeyError:
                fake_function = lambda: tmpl_val
            return fake_function()

        def substitute_template_entries(tmpl, place_into):
            for key in tmpl.keys():
                tmpl_val = tmpl[key]
                if type(tmpl_val) == dict:
                    # Descend and recurse
                    val = {}                        
                    substitute_template_entries(tmpl_val, val)
                else:
                    val = fake_a_value(tmpl_val)
                # Whatever value the above logic assigned, stick it in.
                place_into[key] = val
            return place_into

        return substitute_template_entries(template, tsl)
