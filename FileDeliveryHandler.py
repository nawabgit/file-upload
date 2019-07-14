import requests


class FileDeliveryHandler:

    def __init__(self, url='https://file.io'):
        self.post_url = url

    def post_file_to_api(self, path_to_file):
        file = {'file': (path_to_file, open(path_to_file, 'rb'))}
        r = requests.post(self.post_url, files={'file': file})

        return r.text
