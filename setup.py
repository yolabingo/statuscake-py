"""
    StatusCake API

    Copyright (c) 2022

    Permission is hereby granted, free of charge, to any person obtaining a
    copy of this software and associated documentation files (the "Software"),
    to deal in the Software without restriction, including without limitation
    the rights to use, copy, modify, merge, publish, distribute, sublicense,
    and/or  sell copies of the Software, and to permit persons to whom the
    Software is furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
    DEALINGS IN THE SOFTWARE.

    API Version: 1.0.0-beta.2
    Contact: support@statuscake.com

    Code generated by OpenAPI Generator (https://openapi-generator.tech); DO NOT EDIT.
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "statuscake_py"
VERSION = "1.0.0-beta.2"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "urllib3 >= 1.25.3",
    "python-dateutil",
]

setup(
    name=NAME,
    version=VERSION,
    description="StatusCake API",
    author="Support",
    author_email="support@statuscake.com",
    url="https://github.com/StatusCakeDev/statuscake-py",
    keywords=[
        "python",
        "sdk",
        "statuscake",
    ],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Apache-2.0",
    long_description="""\
    # Introduction  The StatusCake API is organised around the features that we offer, with each feature providing a set of endpoints to perform operations on resources associated with your account.  # Authentication  The StatusCake API uses API keys to authenticate requests. You can view and manage your API keys from [the StatusCake account panel](https://app.statuscake.com/User.php).  All API requests must be made over HTTPS. Calls made over plain HTTP will be redirected to the secure endpoint. API requests without authentication will fail unless otherwise stated in the documentation for the specific endpoint.  &lt;SecurityDefinitions /&gt;  For example an authenticated request must contain an HTTP header of the form &#x60;Authorization: Bearer &lt;API KEY&gt;&#x60;.  **NOTE**: API keys must be kept private. In the event that is it exposed a new one should be generated.  # Ratelimits  Ratelimits are applied to the API to prevent any one client degrading the overall system stability. StatusCake accounts without a subscription, or those on a free plan, can make a maximum of 10 requests per second. For accounts with a paid subscription this limit is increaed to 20 requests per second.  Authenticated requests are associated with the authenticated account, regardless of which API key was used. This means that all API clients share the same ratelimit quota per second when they authenticate with different API keys owned by the same StatusCake account.  When the ratelimit quota is exceeded all future requests will return an HTTP &#x60;429&#x60; status until the ratelimit window is reset.  # Cross-Origin Resource Sharing  The StatusCake API features Cross-Origin Resource Sharing (CORS) implemented in compliance with the W3C specification. This allows cross-domain communication from the browser. All responses have a wildcard same-origin which makes them completely public and accessible to everyone.  # Errors  StatusCake uses conventional HTTP response codes to indicate the success or failure of an API request. In general: Codes in the &#x60;2xx&#x60; range indicate success. Codes in the &#x60;4xx&#x60; range indicate an error that failed given the information provided (e.g. a required parameter was omitted or malformed). Codes in the &#x60;5xx&#x60; range indicate an error with StatusCake servers.  ## Handling Errors  Our client libraries raise exceptions, or return error types, depending on the control flow supported by the language. We recommend using these to write code that handles all possible API exceptions.   # noqa: E501
    """
)