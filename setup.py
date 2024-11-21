from setuptools import setup, find_packages

setup(
    name='PayrollScheduler',
    author='Adrian Bayona',
    description='A python library to create payroll schedules',
    author_email='ahbayona@canadianshieldhealth.com',
    version='0.0.1',
    packages= find_packages(),
    install_requires = [
        'pandas==2.2.2',
    ],
    extras_require= {
        'dev': ['nose2>=0.14.1']
    }
)