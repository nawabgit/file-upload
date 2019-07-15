import requests
from pathlib import Path
from requests_toolbelt.multipart.encoder import MultipartEncoder


class FileDeliveryHandler:

    def __init__(self, url='https://file.io'):
        self.post_url = url

    def post_file_to_api(self, path):
        """
        Posts file to API using MultipartEncoder
            so progress can be monitored

            :param path path to file
            :returns status JSON
        """

        file = open(path, 'rb')
        name = Path(path).with_suffix('').stem

        encoder = MultipartEncoder({'file': (name, file)})
        r = requests.post(self.post_url, files={'file': encoder},
                          headers={'Content-Type': encoder.content_type})

        return r.text
