from django.db import models


class TransactionStatus(models.TextChoices):
    """
    A class representing the possible status of a transaction.

    The `TransactionStatus` class provides a set of predefined choices for the status of a transaction,
    including 'SUCCESS', and 'FAILED'.
    """
    SUCCESS = "success", "Success"
    FAILED = "failed", "Failed"
