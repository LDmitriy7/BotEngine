import os
import logging

DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_NAME = os.environ.get('DB_NAME', 'TemplateBot')

logging.info(f'{DB_HOST = }')
