import requests
from tests.core.clients.base_client import BaseClient



class AuthClient(BaseClient):

    def get_token(self, email, password):
        payload = {'login': email, 'password': password}


        response = requests.post(url=f'{self.base_url}/login', data=payload, headers=self.headers)
        print(f'\nResponse /login: ${response.__dict__}')
        assert response.status_code == 200, f'Status code {response.status_code} != 200'

        return response.cookies