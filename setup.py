from setuptools import setup, find_packages

setup(
    name="Darwin Utilities",
    version="0.1",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    entry_points={
        'console_scripts': [
            'create_notebook=utilities.notebook.create:main',
        ],
    },
)
