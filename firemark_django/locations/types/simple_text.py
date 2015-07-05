__itemtype__ = 'SimpleText'

from locations.item_types import ItemType


class SimpleText(ItemType):
    verbose_name = 'Simple Text'
    config_schema = {
        'title': 'Simple Text',
        'type': 'object',
        'properties': {
            'content': {
                'type': 'string'
            }
        },
        'required': ['content']
    }

    def get_game_schema(self):
        return {}

    def get_data(self):
        return {
            'content': self.config['content']
        }

    def process(self, game, input_data):
        pass
