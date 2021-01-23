from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='eliteapi',
    packages=[''],
    version='0.2',
    license='MIT',
    description='eliteapi is a Python wrapper for Elite Creative allowing you to easly interact with the API.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Kappa',
    author_email='f.cappetti.05@gmail.com',
    url='https://github.com/KappaOnGit/eliteapi',
    download_url='https://github.com/FraKappa/eliteapi/archive/v_02.tar.gz',
    keywords=['eliteapi', 'elite'],
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
