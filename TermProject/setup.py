from distutils.core import setup

setup(
    name='toilet', 
    version='1.0',
    py_modules=['toilet'],
    packages=['image'], 
    package_data = {'image': ['*.gif']},
)
