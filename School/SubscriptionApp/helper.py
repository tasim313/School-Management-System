import uuid
from django.utils import timezone


def generate_invoice_number(prefix="INV", length=8, date_format="%Y%m%d"):
    """
    Generate a unique invoice number based on the current date and a unique identifier.

    Returns:
    str: The generated invoice number.
    """
    # Format the current date (e.g., YYYYMMDD)
    date_part = timezone.now().strftime(date_format)

    # Generate a random string as a unique identifier
    unique_part = str(uuid.uuid4().hex)[:length]

    # Combine date and unique parts to form the invoice number
    invoice_number = f'{prefix}-{date_part}-{unique_part}'

    return invoice_number
