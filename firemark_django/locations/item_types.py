import importlib
import json
from . import settings

destination_schema = {'type': 'string'}

def get_type_choices():
    def get_type_name(codename):
        cls = ItemType.get_class(codename)
        return cls.verbose_name or codename

    return [
        (item[0], get_type_name(item[0])) for item in settings.INSTALLED_TYPES
    ]


class ItemType(object):
    verbose_name = None
    config_schema = None

    @staticmethod
    def get_class(codename):
        module_name = next((
            item[1] for item in settings.INSTALLED_TYPES
            if item[0] == codename
        ))
        module = importlib.import_module(module_name)
        return getattr(module, module.__itemtype__)

    @staticmethod
    def get_instance(item):
        cls = ItemType.get_class(item.type)
        return cls(item)

    def __init__(self, item):
        self.config = json.loads(item.config)

    def get_game_schema(self):
        raise NotImplementedError()

    def get_data(self):
        raise NotImplementedError()

    def process(self, game, input_data):
        raise NotImplementedError()