from setuptools import find_packages, setup

import os


def read(file: str) -> str:
    return open(os.path.join(os.path.dirname(__file__), file)).read()


setup(
    author="Jarrod Norwell",
    author_email="official.antique@gmail.com",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Topic :: Software Development",
        "Topic :: Utilities",
    ],
    description="Instagram automation tool for farming comments, follows and likes, written in Python",
    install_requires=["emoji", "instagrapi", "Pillow", "python-dotenv"],
    keywords=[
        "automation",
        "bot",
        "ig",
        "insta",
        "instagram",
        "instagrapi",
        "instapy",
        "instapy2",
        "python",
        "python3",
    ],
    license_file="..\LICENSE.md",
    long_description=read(file="..\README.md"),
    long_description_content_type="text/markdown",
    name="instapy2",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    url="https://github.com/jarrodnorwell/instapy2",
    version="1.0.0",
)
