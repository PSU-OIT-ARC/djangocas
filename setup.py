#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    author='mdj2',
    author_email='mdj2@pdx.edu',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
    ],
    description='CAS 1.0/2.0 authentication backend for Django',
    keywords='django cas cas2 authentication middleware backend',
    license='MIT',
    long_description="""
``django_cas2`` is a `CAS`_ 1.0 and CAS 2.0 authentication backend for
`Django`_. It allows you to use Django's built-in authentication mechanisms
and ``User`` model while adding support for CAS.

It also includes a middleware that intercepts calls to the original login and
logout pages and forwards them to the CASified versions, and adds CAS support
to the admin interface.

.. _CAS: http://www.ja-sig.org/products/cas/
.. _Django: http://www.djangoproject.com/
""",
    name='django_cas2',
    packages=['django_cas2'],
    url='https://github.com/mdj2/django-cas',
    version='1.0.0',
)
