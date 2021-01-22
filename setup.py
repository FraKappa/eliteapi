from distutils.core import setup

setup(
    name='eliteapi',
    packages=['eliteapi'],
    version='0.1',
    license='MIT',
    description='eliteapi is a Python wrapper for Elite Creative allowing you to easly interact with the API.',
    author='Kappa',
    author_email='f.cappetti.05@gmail.com',
    url='https://github.com/KappaOnGit/eliteapi',   # Provide either the link to your github or to your website
    download_url='https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
    keywords=['eliteapi', 'elite'],   # Keywords that define your package best
    install_requires=[            # I get to this in a second
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
