#!/usr/bin/env python
'''
generate .tar.gz using `python setup.py sdist`
install from unpacked folder using `python setup.py install`
'''
from setuptools import setup

def main():

	setup(
		name='bashcom',
		version='0.1',
		py_modules=['bashcom'],
		#install_requires=[''],
		
		author='',
		author_email='',
		description='',
		license='',
		keywords='',
		url='',
	)
if __name__ == '__main__':
	main()