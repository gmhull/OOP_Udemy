from filestack import Client
import storage

class FileSharer:
    def __init__(self, filepath):
        self.filepath = filepath
        self.api_key = storage.api_key
    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url

print(storage.api_key)
