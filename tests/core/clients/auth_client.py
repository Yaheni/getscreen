import requests
from tests.core.clients.base_client import BaseClient
from tests.data.accounts import accounts


class AuthClient(BaseClient):

    def get_token(self, login):
        payload = {'login': accounts[login]['email'], 'password': accounts[login]['password']}

        response = requests.post(url=f'{self.base_url}/login', data=payload, headers=self.headers)
        print(f'\nResponse /login: ${response.__dict__}')
        assert response.status_code == 200, f'Status code {response.status_code} != 200'

        return response.cookies