import setuptools
import os
from _version import __version__ as version

with open("README.md", "r", encoding="utf-8") as fh:
    longDescription = fh.read()

requirements = ""
with open("NameComparator/requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

requirements = requirements.split("\n")

def listFolders(directory: str) -> list:
    """Creates a list of all the folders in a directory.

    Args:
        directory (str): the directory to search

    Returns:
        list: A list of all the folders in the directory
    """
    folders = []
    for item in os.listdir(directory):
        itemPath = os.path.join(directory, item)
        if os.path.isdir(itemPath) and item != "__pycache__":
            folders.append(itemPath)
    otherFolders = [listFolders(itemPath) for itemPath in folders]
    for folder in otherFolders:
        folders.extend(folder)
    return folders

folderPath = "NameComparator"
folders = listFolders(folderPath)
folders.append("NameComparator")
print(folders)

setuptools.setup(
    name='NameComparator',
    version=version,
    author='Record Linking Lab',
    author_email='recordlinkinglab@gmail.com',
    description='This is a library used to make fuzzy name comparisons across census records.',
    long_description=longDescription,
    long_description_content_type="text/markdown",
    url='https://github.com/byuawsfhtl/NameComparator.git',
    project_urls = {
        "Bug Tracker": "https://github.com/byuawsfhtl/NameComparator/issues"
    },
    packages=folders,
    install_requires=requirements,
    package_data={"": ["*.json", "*.txt"]},
)