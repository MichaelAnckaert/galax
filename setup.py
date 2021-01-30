import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="galax",
    version="0.0.1",
    author="Michael Anckaert",
    author_email="michael.anckaert@sinax.be",
    description="Galax is a static site generator targetting both HTML and Gemini",
    keywords='static site generator gemini html',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    url="https://github.com/MichaelAnckaert/galax",
    scripts=['bin/galax'],
    python_requires='>=3.6',
    install_requires=[
        "Markdown==3.3.3",
        "Jinja2==2.11.2"
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Operating System :: OS Independent",
    ],
)
