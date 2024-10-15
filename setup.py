from setuptools import setup, find_packages

setup(
    name='qflexProject',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Django>=3.2,<4.0',  # specify your Django version
        # Add other dependencies here, e.g.:
        # 'djangorestframework',
        # 'requests',
    ],
    entry_points={
        'console_scripts': [
            'manage.py = manage:main',  # Make sure this matches your manage.py entry
        ],
    },
)
