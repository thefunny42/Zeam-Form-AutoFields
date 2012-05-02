from setuptools import setup, find_packages
import os

version = '1.0.1'

tests_require = [
    'zope.app.wsgi',
    'zope.configuration',
    'zope.testing',
    'zope.publisher',
    'zeam.form.base [test]',
]


setup(name='zeam.form.autofields',
      version=version,
      description="Automatically collect fields for a Zeam Form.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Framework :: Zope3",
        "Programming Language :: Python",
        "Programming Language :: Zope",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='zeam form fields collect',
      author='Sylvain Viollon',
      author_email='thefunny@gmail.com',
      url='http://pypi.python.org/pypi/zeam.form.autofields',
      license='BSD',
      package_dir={'': 'src'},
      packages=find_packages('src'),
      namespace_packages=['zeam', 'zeam.form'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'martian',
          'zope.browser',
          'zope.interface',
          'zope.component',
          'grokcore.component >= 2.5',
          'grokcore.view',
          'zeam.form.base >= 1.2',
          'zeam.form.ztk >= 1.2',
          ],
      tests_require = tests_require,
      extras_require = {'test': tests_require},
      )
