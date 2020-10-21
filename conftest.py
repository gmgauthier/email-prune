import pytest
from email_pruner import spawn


@pytest.fixture(scope="session", autouse=True)
def emails():
    return spawn(100)
