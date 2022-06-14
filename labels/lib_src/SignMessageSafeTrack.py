from web3 import Web3
from eth_account.messages import encode_defunct
from sgi.settings import EMPRESA
from logs.app_log import loggin


class SignMessageSafeTrack:
    """Clase encarga de firmar el menaje Str JSON"""
    def __init__(self):
        loggin('i', 'Seteando variables para firmado')
        self.address = EMPRESA['safetrack']['wallet']['networkAddress']
        self.private_key = EMPRESA['safetrack']['wallet']['networkPk']
        self.business_id = EMPRESA['safetrack']['wallet']['business_id']

    def sign(self, message):
        message = message.replace('{business_id}', self.business_id)
        web3 = Web3(Web3.HTTPProvider(self.address))
        msg = encode_defunct(text=message)
        sign = web3.eth.account.sign_message(
            msg,
            private_key=self.private_key
        )
        loggin('i', 'Mensaje firmado')
        return sign.signature.hex()
