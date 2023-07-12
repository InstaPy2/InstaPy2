from .utilities import Comment, Like

from instagrapi import Client

from os import getcwd, mkdir, sep
from os.path import exists
from pathlib import Path

class Authentication:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def login(self):
        self.client = Client()

        file_folder = getcwd() + sep + "files"
        if not exists(path=file_folder):
            mkdir(path=file_folder)

        session_file = file_folder + sep + f"{self.username}.json"
        try:
            if not exists(path=session_file):
                logged_in = self.client.login(username=self.username, password=self.password)
                self.client.dump_settings(path=Path(session_file))
            else:
                self.client.load_settings(path=Path(session_file))
                logged_in = self.client.login(username=self.username, password=self.password)
        except:
            print("Error logging in")

        print(f"Successfully logged {self.username} in." if logged_in else f"Error logging {self.username} in.")

        self.comment = Comment(client=self.client)
        self.like = Like(client=self.client)