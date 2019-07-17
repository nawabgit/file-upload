import requests
import os
from requests_toolbelt.multipart.encoder import MultipartEncoder, MultipartEncoderMonitor


class FileDeliveryHandler:

    def __init__(self, url='https://file.io'):
        self.post_url = url

    def post_file_to_api(self, path):
        """
        Posts file to API using MultipartEncoder
        so progress can be monitored by using a callback

            :param path path to file
            :returns status JSON
        """

        name = os.path.basename(path)
        encoder = MultipartEncoder(
            fields={
                'file': (name, open(path, 'rb'), 'application/octet-stream')
            }
        )
        monitor = MultipartEncoderMonitor(encoder, progress)
        r = requests.post(self.post_url, data=monitor, headers={'Content-Type': monitor.content_type})

        return r.text


def progress(monitor):
    print(round(monitor.bytes_read / monitor.len, 4) * 100)
