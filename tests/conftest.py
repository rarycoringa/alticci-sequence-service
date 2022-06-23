import pytest

from alticci.app import app


@pytest.fixture()
def client():
    app.testing = True

    with app.test_client() as client:
        yield client
