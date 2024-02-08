from os.path import dirname, join
from setuptools import find_packages, setup


def read(file: str) -> str:
    return open(join(dirname(__file__), file)).read()


setup(
    author="Jarrod Norwell",
    author_email="official.antique@gmail.com",
    classifiers=[],
    description="Instagram automation tool for farming comments, follows and likes, written in Python",
    install_requires=[
        "emoji",
        "instagrapi @ git+https://github.com/jarrodnorwell/instagrapi",
        "Pillow",
        "python-dotenv",
    ],
    keywords=[],
    license_file="../LICENSE.md",
    long_description=read(file="../README.md"),
    long_description_content_type="text/markdown",
    name="instapy2",
    package_dir={"": "source"},
    packages=find_packages(where="source"),
    url="https://github.com/jarrodnorwell/instapy2",
    version="1.0.0",
)
