import pytest

from tests.core.clients.auth_client import AuthClient
from tests.core.clients.profile_client import ProfileClient


@pytest.fixture
def auth_client():
    yield AuthClient()

@pytest.fixture
def profile_client():
    yield ProfileClient()