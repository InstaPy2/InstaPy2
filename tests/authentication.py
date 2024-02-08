from instapy2 import InstaPy2

from dotenv import load_dotenv
from os import getenv

load_dotenv()

if __name__ == "__main__":
    username = getenv("USERNAME")
    password = getenv("PASSWORD")

    if username and password:
        instapy2 = InstaPy2(username=username, password=password)
