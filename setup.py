from setuptools import setup, find_packages

__version__ = '0.0.1'

setup(
    name="pcdapi",
    description="PCIC's PCDS backend API",
    keywords="science climate meteorology weather",
    license = "GPL-3.0",
    packages=find_packages(),
    version=__version__,
    url="http://www.pacificclimate.org/",
    author="James Hiebert <hiebert@uvic.ca>, Basil Veerman <bveerman@uvic.ca>",
    author_email="climate@uvic.ca",
    url = "https://github.com/pacificclimate/pcdapi",
    # install_requires = [
    #     'flask',
    #     'Flask-SQLAlchemy',
    #     'modelmeta'
    # ],
    # scripts = ['scripts/devserver.py'],
    package_dir = {'pcdapi': 'pcdapi'},
    zip_safe=True
)
