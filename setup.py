from distutils.core import setup

f=open("README")

setup(
    name='genname',
    version='0.1',
    description="Generate quirky names",
    long_description="\n".join(f),
    classifiers=[
        ],
    keywords='random name',
    author='Michael Bauer',
    author_email='michael.bauer@okfn.org',
    url='http://github.com/mihi-tr/gennames',
    license='AGPLv3',
    packages=['genname'],
    zip_safe=False,
    tests_require=[],
    entry_points=\
    """ """,
)
