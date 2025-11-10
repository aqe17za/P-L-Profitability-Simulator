

"""
Database initialization based on the engine and PythonAccounting models.
"""
from python_accounting.database.engine import engine
from python_accounting import models


def database_init() -> None:
    """
    Initializes the database by setting up all tables that do not currently exist.

    Returns:
        None
    """

    models.Base.metadata.create_all(engine)
