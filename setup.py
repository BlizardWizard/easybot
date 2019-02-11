from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='easybot',
    version='0.0.2',
    description='Easy Discord bot library with Python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/BlizardWizard/Easybot',
    author='Blizard_Wizard',
    author_email='email@robloxcom.me',
    license='MIT',
    packages=['easybot'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    zip_safe=False
)