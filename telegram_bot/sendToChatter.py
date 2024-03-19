import xmlrpc.client
import logging.config
import config

logger = logging.getLogger(__name__)

async def send_to_chatter(lead_id, message):
    host = config.ODOO_HOST
    port = config.ODOO_PORT
    url = 'http://' + host + ':' + port
    db_name = config.ODOO_DB_NAME
    login = config.ODOO_LOGIN
    password = config.ODOO_PASSWORD

    common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
    uid = common.authenticate(db_name, login, password, {})

    models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')

    try:
        models.execute_kw(db_name, uid, password, 'mail.message', 'create', [{
            'model': 'crm.lead',
            'res_id': int(lead_id),
            'body': 'Сообщение от исполнителя:\n' + message
        }])

    except Exception as e:
        logger.error(e)