import pytest

from gradient_boosting_model.api.config import TestingConfig
from gradient_boosting_model.api.app import create_app


@pytest.fixture(scope='session')
def app():
    app = create_app(config_object=TestingConfig()).app
    with app.app_context():
        yield app


@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client  # Has to be yielded to access session cookies
