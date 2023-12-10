"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path as os_path
this_directory = os_path.abspath(os_path.dirname(__file__))

# 读取文件内容
def read_file(filename):
    with open(os_path.join(this_directory, filename), encoding='utf-8') as f:
        long_description = f.read()
    return long_description

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    # name='GeocodingCHN',
    name='GeocodingCHN',
    version='1.4.5',
    author='ZhouHang',
    author_email='fjkl@vip.qq.com',
    description='地址标准化',
    long_description=read_file('README.md'),  # 读取的Readme文档内容
    long_description_content_type="text/markdown",  # 指定包文档格式为markdown
    license="MIT Licence",
    url='https://github.com/casuallyName/Geocoding',
    packages=find_packages(),
    package_data={'GeocodingCHN': ['geocoding.jar'],},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=['jpype1'],
    zip_sfe=False

)