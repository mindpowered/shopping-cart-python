import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='mindpowered-shoppingcart',
    version='0.0.13',
    author="Mind Powered Corporation",
    author_email="support@mindpowered.dev",
    license="MIT",
    url="https://mindpowered.dev/",
    description="Shopping Cart for Online Shopping",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=['shoppingcart'],
    packages=['mindpowered_shoppingcart'],
    package_dir={'mindpowered_shoppingcart': 'wrappers'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        'License :: OSI Approved :: MIT License',
    ],
    install_requires=[
        'mindpowered-maglev',
    ],
)
