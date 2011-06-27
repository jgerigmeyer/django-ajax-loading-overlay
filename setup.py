

from os.path import join, dirname

from setuptools import setup

here = dirname(__file__)

long_description = (open(join(here, "README.rst")).read() + "\n\n" +
                    open(join(here, "CHANGES.rst")).read() + "\n\n" +
                    open(join(here, "TODO.rst")).read())

def get_version():
    fh = open(join(here, "ajax_loading_overlay", "__init__.py"))
    try:
        for line in fh.readlines():
            if line.startswith("__version__ ="):
                return line.split("=")[1].strip().strip('"')
    finally:
        fh.close()

setup(
    name="django-ajax-loading-overlay",
    version=get_version(),
    description="Uses JS to add/remove a loading overlay during Ajax calls",
    long_description=long_description,
    author="Jonny Gerig Meyer",
    author_email="jonny@oddbird.net",
    url="https://github.com/jgerigmeyer/django-ajax-loading-overlay/",
    packages=["ajax_loading_overlay"],
    package_data={
        "ajax_loading_overlay": [
            "static/ajax_loading_overlay/*.*",
            ]
        },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Framework :: Django",
    ],
    zip_safe=False,
)
