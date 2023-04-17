from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in masar_ksa/__init__.py
from masar_ksa import __version__ as version

setup(
	name="masar_ksa",
	version=version,
	description="MASAR KSA",
	author="KCSC",
	author_email="inf@kcsc.com.jo",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
