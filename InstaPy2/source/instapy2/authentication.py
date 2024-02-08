from .utilities import Comment, Follow, Like, Logging, Utility

from instagrapi import Client

from json import load
from os import getcwd, mkdir, sep
from os.path import exists
from pathlib import Path


class Authentication:
    def __init__(self, username: str, password: str):
        logging = Logging()
        self.__login(logging=logging, username=username, password=password)

    def __login(self, logging: Logging, username: str, password: str):
        dumped_files_directory = getcwd() + sep + "files"
        if not exists(dumped_files_directory):
            mkdir(path=dumped_files_directory)

        dumped_session_file = dumped_files_directory + sep + f"{username}.json"
        if exists(dumped_session_file):
            logging.info(string="Using previously dumped settings file")

            handle = open(file=dumped_session_file, mode="r")
            self.client = Client(settings=load(fp=handle))
            logged_in = self.client.login(username=username, password=password)
        else:
            self.client = Client()
            self.client.login(username=username, password=password)
            logged_in = self.client.dump_settings(path=Path(dumped_session_file))

        logging_def = logging.success if logged_in else logging.error
        logging_def(
            string=f"{f'Successfully logged in as {self.client.username}' if logged_in else 'Failed to log in'}"
        )

        self.utility = Utility(client=self.client, logging=logging)

        self.comment = Comment(utility=self.utility)
        self.follow = Follow(utility=self.utility)
        self.like = Like(utility=self.utility)
