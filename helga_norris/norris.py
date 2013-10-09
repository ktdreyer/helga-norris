import random as _random

import pkg_resources

from helga.extensions.base import (CommandExtension,
                                   ContextualExtension)
from helga.log import setup_logger


logger = setup_logger(__name__)


_quips = [quip.rstrip().decode('utf-8') for quip in
    pkg_resources.resource_stream('helga_norris', 'quips.txt')
    if quip.rstrip()]


class NorrisExtension(CommandExtension):

    NAME = 'norris'

    usage = 'norris <username>'

    allow_many = True

    def __init__(self, *args, **kwargs):
        self._quips = _quips
        super(NorrisExtension, self).__init__(*args, **kwargs)

    def handle_message(self, opts, message):
        username = opts['<username>']
        message.response = self.norris(username=username)

    def should_handle_message(self, opts, message):
        if not opts:
            return False

        if opts.get('norris'):
            if opts.get('<username>'):
                return True

        logger.info('returning false :( :(')
        return False


    def norris(self, username=None):
        """
        Hook into giphypop to find a gif. If no search term, just
        return a random gif. If a search term is given, try to translate
        it and default back to a search
        """
        sentence = _random.choice(_quips)
        sentence = sentence.replace('Chuck Norris', username)
        return sentence
