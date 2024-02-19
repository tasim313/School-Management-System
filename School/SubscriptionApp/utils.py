import string
import secrets


def unique_transaction_id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(secrets.choice(chars) for _ in range(size))
