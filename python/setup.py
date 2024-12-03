# Package meta-data.
NAME = 'mypackage'
DESCRIPTION = '填写你的项目简短描述.'
URL = 'https://github.com/你的github账户/mypackage'
EMAIL = 'me@example.com'    # 你的邮箱
AUTHOR = 'Awesome Soul'     # 你的名字
REQUIRES_PYTHON = '>=3.6.0' # 项目支持的python版本
VERSION = '0.1.0'           # 项目版本号

# What packages are required for this module to be executed?
REQUIRED = [
    # 'requests', 'maya', 'records',
]


setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],

    # entry_points={
    #     'console_scripts': ['mycli=mymodule:cli'],
    # },
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    # $ setup.py publish support.
    cmdclass={
        'upload': UploadCommand,
    },
)