from django.conf import settings as project_settings
from sslcommerz_lib import SSLCOMMERZ

from SubscriptionApp.utils import unique_transaction_id_generator


def sslcommerz_payment_gateway(request):
    store_id = project_settings.STORE_ID
    store_pass = project_settings.STORE_PASS

    settings = {
        'store_id': store_id,
        'store_pass': store_pass,
        'issandbox': True
    }

    sslcommerz = SSLCOMMERZ(settings)

    post_body = {
        'total_amount': 100.0,
        'currency': 'BDT',
        'tran_id': unique_transaction_id_generator(),
        'success_url': 'localhost:8000/success',
        'fail_url': 'localhost:8000/fail',
        'cancel_url': 'localhost:8000/cancel',
        'emi_option': 0,
        'cus_name': request.user.username,
        'cus_email': request.user.email,
        'cus_add1': 'Dhaka',
        'cus_city': 'Dhaka',
        'cus_country': 'Bangladesh',
        'shipping_method': 'NO',
        'multi_card_name': '',
        'num_of_item': 1,
        'product_name': 'Subscription Plan',
        'product_category': 'Subscription',
        'product_profile': 'general',
    }

    response = sslcommerz.createSession(post_body)

    return 'https://sandbox.sslcommerz.com/gwprocess/v4/gw.php?Q=pay&SESSIONKEY=' + response["sessionkey"]
