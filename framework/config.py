import ConfigParser
from md5 import md5

CONFIG_FILENAME_TEMPLATE = 'config/{name}.ini'
_config_singleton = None


def get_salt(salt=''):
    return md5(salt).hexdigest()


def get_config(name):
    if _config_singleton is not None:
        return _config_singleton
    config = ConfigParser.ConfigParser()
    filename = CONFIG_FILENAME_TEMPLATE.format(name=name)
    with open(filename) as fp:
        config.readfp(fp)
        return config
    raise RuntimeError(
        'Cannot load configuration from file: {0}'.format(filename)
    )
