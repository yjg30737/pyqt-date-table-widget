from setuptools import setup, find_packages

setup(
    name='pyqt-date-table-widget',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt Date Table Widget',
    url='https://github.com/yjg30737/pyqt-date-table-widget.git',
    install_requires=[
        'PyQt5>=5.8'
    ]
)