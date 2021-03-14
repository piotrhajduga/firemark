__itemtype__ = 'SimpleExit'

from locations.item_types import ItemType
from locations.models import LocationExit


class SimpleExit(ItemType):
    verbose_name = 'Simple Exit'
    config_schema = {
        'title': 'Simple Exit',
        'type': 'object',
        'properties': {
            'label': {
                'type': 'string',
            },
            'exit': {
                'type': 'string',
            }
        },
        'required': ['label']
    }

    def get_game_schema(self):
        return {}

    def get_data(self):
        return {'label': self.config['label']}

    def process(self, game, input_data):
        exit = LocationExit.objects.get(codename=self.config['exit'])
        game.location = exit.destination
        game.save()
