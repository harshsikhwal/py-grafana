# MIT LICENSE
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import os
import sys
import time
from setuptools import setup


base_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(base_dir, '../README.md')) as fid:
    long_description = fid.read()

with open(os.path.join(base_dir, '../version.txt')) as fid:
    version_number = fid.read()


setup(
    name='py-grafana-sdk',
    version=version_number,
    description='A Library to Configure Grafana Using Rest',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/harshsikhwal/py-grafana',
    author='Vibaswan Roychowdhury & Harsh Sikhwal',
    author_email='vroychowdhury@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    keywords='grafana grafana-api grafana-sdk sdk api automation',
    packages=['py_grafana'],
    include_package_data=True,
    python_requires='>=3.7, <4',
    install_requires=['requests'],
    tests_require=['pytest'],
)
