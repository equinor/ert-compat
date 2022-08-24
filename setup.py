from pathlib import Path

from setuptools import find_packages, setup

setup(
    name="ert-compat",
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    author="Equinor ASA",
    author_email="fg_sib-scout@equinor.com",
    url="https://github.com/equinor/ert-compat",
    description="ERT compatibility package",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    license="GPL-3.0",
    platforms="any",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Plugins",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",  # noqa
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
        "ert >= 2.37.0b8",
        "oil_reservoir_synthesizer"
    ],
)
