from setuptools import setup, find_packages

with open(README.rst) as f:
    LONG_DESC = f.read()
    
setup(name='Titan',
      version='0.0.1',
      url='https://github.com/RafaelSouza94/Project_Titan',
      description='CTI tool to analyze IoCs using machine learning',
      long_description=LONG_DESC,
      author='Rafael Souza',
      author_email='rafaelrochasouza@outlook.com.br',
      license='GnuGPLv3',
      classifiers=[
          'Development Status :: 3 - Alpha', 
          'License :: OSI Approved :: GNU GPLv3',
          'Programming Language :: Python :: 3'
      ]
      keywords=['flask', 'security', 'threat intelligence']
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      entry_points="""
      """,
      # install_requires
     )