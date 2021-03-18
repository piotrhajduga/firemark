__itemtype__ = 'SimpleExit'

from locations.item_types import ItemType, destination_schema
from locations.models import Location


class SimpleExit(ItemType):
    verbose_name = 'Simple Exit'
    config_schema = {
        'title': 'Simple Exit',
        'type': 'object',
        'properties': {
            'label': {
                'type': 'string',
            },
            'destination': destination_schema
        },
        'required': ['label']
    }

    def get_game_schema(self):
        return {}

    def get_data(self):
        return {'label': self.config['label']}

    def process(self, game, input_data):
        location = Location.objects.get(id=self.config['destination'])
        game.location = location
        game.save()
