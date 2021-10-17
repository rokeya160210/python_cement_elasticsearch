
from cement import App, TestApp, init_defaults
from cement.core.exc import CaughtSignal
from .core.exc import TodoError
from .controllers.base import Base
from elasticsearch import Elasticsearch
from config import settings
import os
from cement.utils import fs

import os
from tinydb import TinyDB
from cement.utils import fs
from .controllers.items import Items


# configuration defaults

CONFIG = init_defaults('todo')
CONFIG['todo']['db_file'] = 'localhost:9200'
CONFIG['todo']['email'] = 'rokeya160210@gmail.com'
def extend_elasticsearchDB(app):
    app.log.info('extending todo application with elasticsearch')    
    db_file = app.config.get('todo','db_file' )    
    app.log.info('extending todo application with elasticsearch')
    app.extend('db', Elasticsearch(db_file))
    app.log.info(app.db)




class Todo(App):
    """My Application primary application."""
    

    class Meta:
        label = 'todo'
        hooks = [('post_setup', extend_elasticsearchDB)]
        

        # configuration defaults
        config_defaults = CONFIG

        # call sys.exit() on close
        exit_on_close = True

        # load additional framework extensions
        extensions = [
            'yaml',
            'colorlog',
            'jinja2',
        ]

        # configuration handler
        config_handler = 'yaml'

        # configuration file suffix
        config_file_suffix = '.yml'

        # set the log handler
        log_handler = 'colorlog'

        # set the output handler
        output_handler = 'jinja2'

        # register handlers
        handlers = [
            Base,
            Items,
        ]


class TodoTest(TestApp,Todo):
    """A sub-class of Todo that is better suited for testing."""

    class Meta:
        label = 'todo'


def main():
    with Todo() as app:
        try:
            app.run()

        except AssertionError as e:
            print('AssertionError > %s' % e.args[0])
            app.exit_code = 1

            if app.debug is True:
                import traceback
                traceback.print_exc()

        except TodoError as e:
            print('TodoError > %s' % e.args[0])
            app.exit_code = 1

            if app.debug is True:
                import traceback
                traceback.print_exc()

        except CaughtSignal as e:
            # Default Cement signals are SIGINT and SIGTERM, exit 0 (non-error)
            print('\n%s' % e)
            app.exit_code = 0


if __name__ == '__main__':
    main()
