# setup.py
from setuptools import setup, find_packages

setup(
    name='VideoCutInShorts',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'moviepy',
    ],
    author='TCodingHub',
    description='Une bibliothèque pour découper des vidéos en plusieurs parties.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/codinghubytb/VideoCutInShorts',  # Lien vers ton dépôt GitHub
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
