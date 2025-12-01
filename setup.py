from setuptools import setup, find_packages

setup(name='HD_BET-minimal',
      version='1.1',
      description='Tool for brain extraction',
      url='https://github.com/dafne-imaging/dafne-HD-BET-minimal',
      python_requires='>=3.5',
      author='Fabian Isensee, Francesco Santini',
      author_email='francesco.santini@unibas.ch',
      license='Apache 2.0',
      zip_safe=False,
      install_requires=[
      'numpy',
      'torch>=0.4.1',
      'scikit-image',
      'appdirs',
      'requests',
      ],
      packages=find_packages(include=['HD_BET_minimal', 'HD_BET_minimal.models']),
      classifiers=[
          'Intended Audience :: Science/Research',
          'Programming Language :: Python',
          'Topic :: Scientific/Engineering',
          'Operating System :: Unix'
      ],
      package_data= {
          'HD_BET_minimal': ['models/*.model']
      },
      include_package_data=True
      )

