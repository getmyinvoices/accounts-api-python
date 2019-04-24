import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='getmyinvoices',
    version='1.0.1',
    author="Ben Barten",
    author_email="bba@fino.digital",
    description="A python client for the GetMyInvoices API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/getmyinvoices/accounts-api-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        "urllib3==1.24.2"
    ]
)
