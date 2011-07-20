from setuptools import setup, find_packages
import os

version = '1.1dev'

tests_require = [
    'zope.app.wsgi',
    'zope.testing',
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
      url='',
      license='BSD',
      package_dir={'': 'src'},
      packages=find_packages('src'),
      namespace_packages=['zeam', 'zeam.form'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'martian',
          'zope.interface',
          'zope.component',
          'grokcore.component',
          'grokcore.view',
          'zeam.form.base',
          ],
      tests_require = tests_require,
      extras_require = {'test': tests_require},
      )
