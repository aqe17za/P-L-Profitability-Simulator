
"""
Represents a Debit Note Transaction.

"""
from typing import Any
from python_accounting.models import Transaction
from python_accounting.mixins import BuyingMixin, AssigningMixin


class DebitNote(  # pylint: disable=too-many-ancestors
    BuyingMixin, AssigningMixin, Transaction
):
    """Class for the Debit Note Transaction."""

    __tablename__ = None
    __mapper_args__ = {
        "polymorphic_identity": Transaction.TransactionType.DEBIT_NOTE,
    }

    def __init__(self, **kw: Any) -> None:
        from python_accounting.models import (  # pylint: disable=import-outside-toplevel
            Account,
        )

        self.main_account_types: list = [
            Account.AccountType.PAYABLE,
        ]
        self.credited = False
        self.transaction_type = Transaction.TransactionType.DEBIT_NOTE
        super().__init__(**kw)
