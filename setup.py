
import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()  # Read the file content inside the block


__version__ = "0.0.0"  # Replace with your actual version

REPO_NAME = "Kidney_Disease_Classification_-Deep_Learning-"
AUTHOR_USER_NAME = "Poojitha_Natarajan"
SRC_REPO = "cnn_classifier"
AUTHOR_EMAIL = "n.poojitha75@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)