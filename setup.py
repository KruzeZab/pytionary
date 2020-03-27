import setuptools

def readme():
    with open('README.md') as f:
        README = f.read()
    return README

setuptools.setup(
    name="pytionary", 
    version="1",
    keywords = 'dictionary pytionary glossary',
    author="Kruze Zab",
    author_email="kruzezab4@gmail.com",
    description="Python Dictionary (meaning, synonyms, antonyms, pos)",
    long_description= readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/KruzeZab/pytionary",
    install_requires = ['requests', 'beautifulsoup4'], 
    packages=setuptools.find_packages(exclude=['tests*']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)
