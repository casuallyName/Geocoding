"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

# Get the long description from the README file
with open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    # name='GeocodingCHN',
    name='GeocodingCHN',
    version='1.0',
    author='ZhouHang',
    author_email='fjkl@vip.qq.com',
    description='地址标准化',
    long_description=long_description,
    # long_description_content_type='text/markdown',  # 文档格式
    packages=find_packages(),
    package_data={'GeocodingCHN': ['*.jar'],},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['jpype1'],
    zip_sfe=False

)