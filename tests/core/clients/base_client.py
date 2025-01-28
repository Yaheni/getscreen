

class BaseClient:

    __host__ = 'https://getscreen.dev'
    headers = {
        "x-requested-with": "XMLHttpRequest"
    }

    def __init__(self):
        self.base_url = f'{self.__host__}/api'




