from setuptools import setup, find_packages

setup(
    name='PSTOCK',
    version='0.1.0',
    description='A machine learning project for stock prediction',
    author='Nikhil Varshney',
    author_email='nikhilvarshney92@gmail.com',
    url='https://github.com/NikhilVarshney92/PSTOCK',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'matplotlib'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
)