from distutils.core import setup, Extension 
module_spam = Extension('spam', 
    sources = ['spammodule.c'])

setup(
    name='toilet', 
    version='1.0',
    py_modules=['toilet'],
    packages=['image'], 
    package_data = {'image': ['*.gif']},
    
    ext_modules=[module_spam]
)
