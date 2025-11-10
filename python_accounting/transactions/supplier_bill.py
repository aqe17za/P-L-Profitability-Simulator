

"""
Represents a Supplier Bill Transaction.

"""
from typing import Any
from python_accounting.models import Transaction
from python_accounting.mixins import BuyingMixin, ClearingMixin


class SupplierBill(  # pylint: disable=too-many-ancestors
    BuyingMixin, ClearingMixin, Transaction
):
    """Class for the Supplier Bill Transaction."""

    __tablename__ = None
    __mapper_args__ = {
        "polymorphic_identity": Transaction.TransactionType.SUPPLIER_BILL,
    }

    def __init__(self, **kw: Any) -> None:
        from python_accounting.models import (  # pylint: disable=import-outside-toplevel
            Account,
        )

        self.main_account_types: list = [
            Account.AccountType.PAYABLE,
        ]
        self.credited = True
        self.transaction_type = Transaction.TransactionType.SUPPLIER_BILL
        super().__init__(**kw)
