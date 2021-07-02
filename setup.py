import io
from setuptools import setup, find_packages

def readme():
    with io.open('README.md', encoding='utf-8') as f:
        return f.read()

setup(name='tensordata',
      version='0.4.1',
      install_requires=['linora>=1.0.0', 'rarfile', 'requests'],
      description='CV, NLP, DM datasets Toolkit for Machine Learning.',
      long_description=readme(),
      long_description_content_type='text/markdown',
      url='https://github.com/Hourout/tensordata',
      author='JinQing Lee',
      author_email='hourout@163.com',
      keywords=['computer-vision', 'natural-language-processing', 'data-mining', 'Machine-Learning', 'datasets'],
      license='Apache License Version 2.0',
      classifiers=[
          'Intended Audience :: Developers',
          'Intended Audience :: Education',
          'Intended Audience :: Science/Research',
          'Topic :: Scientific/Engineering',
          'Topic :: Scientific/Engineering :: Artificial Intelligence',
          'Topic :: Scientific/Engineering :: Visualization',
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
      ],
      packages=find_packages(),
      zip_safe=False)
