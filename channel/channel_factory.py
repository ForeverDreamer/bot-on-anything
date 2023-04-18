"""
channel factory
"""
import importlib
import inspect


def create_channel(channel_type):
    """
    create a channel instance
    :param channel_type: channel type code
    :return: channel instance
    """
    for name, cls in inspect.getmembers(
            importlib.import_module(f'channel.{channel_type}.{channel_type}_channel'),
            inspect.isclass
    ):
        if name == f'{channel_type.capitalize()}Channel':
            return cls()
    raise RuntimeError("unknown channel_type in config.json: " + channel_type)
