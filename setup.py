import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="galax",
    version="0.0.1",
    author="Michael Anckaert",
    author_email="michael.anckaert@sinax.be",
    description="Galax is a static site generator targetting both HTML and Gemini",
    long_description=long_description,
    url="https://github.com/MichaelAnckaert/galax",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
