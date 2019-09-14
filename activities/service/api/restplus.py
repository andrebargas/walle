import logging
from flask_restplus import Api 
import settings
from pymongo import MongoClient

log = logging.getLogger(__name__)
api = Api(version='1.0', title='Documentação do serviço de atividades do projeto WALLE',
            description='')


client = MongoClient('mongo', 27017)
db = client['activities-database']
deposit_collection = db['deposit-collection']
colector_collection = db['colector-collection']


@api.errorhandler
def default_error_handler(error):
    message = 'Um erro aconteceu'
    log.exception(message)

    if not settings.FLASK_DEBUG:
        return{'message': message}, 500