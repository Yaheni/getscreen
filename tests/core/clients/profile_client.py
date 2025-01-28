import pytest
import requests

from tests.core.clients.base_client import BaseClient

class ProfileClient(BaseClient):

    def update_names(self, token, first_name, last_name):
        response = requests.post(url=f'{self.base_url}/dashboard/settings/account/update', json={
                "name": first_name,
                "surname": last_name,
            }, headers=self.headers, cookies=token)
        print(f'Response /update: ${response.__dict__}')

        assert response.status_code == 200, f'Status code {response.status_code} != 200'
        return response


    def get_info(self, token):
        response = requests.get(url=f'{self.base_url}/dashboard/account/info', cookies=token)
        print(f'Response /info: ${response.__dict__}')

        assert response.status_code == 200, f'Status code {response.status_code} != 200'
        return response.json()


    def check_profile_names(self, response, names):
        name, surname = names

        if response['name'] != name:
            pytest.fail(f'Фактическое имя {response.name} не соответствует ожидаемому {name}')

        if response['surname'] != surname:
            pytest.fail(f'Фактическое имя {response.surname} не соответствует ожидаемому {surname}')






