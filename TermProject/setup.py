from distutils.core import setup, Extension 
module_spam = Extension('spam', 
    sources = ['spammodule.c'])

setup(
    name='toilet', 
    version='1.0',
    py_modules=['toilet'],
    packages=['image', 'Telegram'], 
    package_data = {'image': ['*.gif'], 'Telegram' : ['*.py']},
    
    ext_modules=[module_spam]
)
