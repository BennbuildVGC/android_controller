from setuptools import setup

readme = ''
with open('README.md') as f:
    readme = f.read()

setup(name='android_controller',
      version='1.0',
      description='Module to control your android phone using code',
      long_description=readme,
      long_description_content_type='text/markdown',
      classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
      ],
      keywords='android automatization bot controller mobile phone wrapper',
      url='https://github.com/BennbuildVGC/android_controller',
      author='Bennbuild',
      author_email='bambrambam@gmail.com',
      license='MIT',
      packages=['android_controller'],
      zip_safe=False)
