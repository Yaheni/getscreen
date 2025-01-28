from faker import Faker
fake = Faker()

class TestProfile:

    def test_update_profile_names(self, auth_client, profile_client):
        names = (name, surname) = fake.name(), fake.name()
        token = auth_client.get_token('nurkehofyo@gufum.com', '6M7K9Xt9DB')

        profile_client.update_names( token, name, surname)
        info = profile_client.get_info(token)
        profile_client.check_profile_names(info, names)





