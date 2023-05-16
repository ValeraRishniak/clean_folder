from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder_90012345009',
    version='0.0.3',
    description='Package for sorting files in folder by file extension',
    author='Rishniak Valerii',
    author_email='ya.mihelson@ukr.net',
    license='MIT',
    classifiers=['Programming Language :: Python :: 3'],
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean_folder=clean_folder.clean:sort']}
)