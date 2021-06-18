import setuptools


setuptools.setup(
    name="dietitian",
    version="0.0.1",
    description="A diet optimizer",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
    ],
    keywords="diet optimization",
    url="https://github.com/thoughteer/dietitian",
    author="Iskander Sitdikov",
    author_email="thoughteer@gmail.com",
    license="MIT",
    packages=setuptools.find_packages(),
    include_package_data=True,
    zip_safe=False)
