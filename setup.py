import sys
from setuptools import setup

setup(
    name="awshammer",
    version="0.0.1",
    author="Arun",
    author_email="arunsinghkce@gmail.com",
    description="Packaging boto3 aws scripts",
    url="https://github.com/ArunSinghJ123/aws-python-boto3",
    install_requires=['boto3', 'awscli'],
    packages=['iam', 's3_bucketpolicy'],
    classifiers=(
        "Programming Language :: Python :: 2.7",
        "Operating System :: Mac/Linux",
    ),
    entry_points={
    'console_scripts': ['iam = iam.roles:main',
                        'bucket = s3_bucketpolicy.s3_bucket_policy:main']}
)
