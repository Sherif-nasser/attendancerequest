from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in attendancerequest/__init__.py
from attendancerequest import __version__ as version

setup(
	name="attendancerequest",
	version=version,
	description="modyfication on the attendance request doctype",
	author="sherif sultan",
	author_email="sheriffnasserr@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
