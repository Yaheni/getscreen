from faker import Faker
fake = Faker()

class TestProfile:

    def test_update_profile_names(self, auth_client, profile_client):
        names = (name, surname) = fake.name().split()
        token = auth_client.get_token('profile')

        profile_client.update_names(token, name, surname)
        info = profile_client.get_info(token)
        profile_client.check_profile_names(info, names)





