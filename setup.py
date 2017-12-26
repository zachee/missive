from setuptools import setup

setup(
    name='missive',
    packages=['missive'],
    include_package_data=True,
    install_requires=[
        'flask',
	'bcrypt',
	'passlib',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)
