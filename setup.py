import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fileG", # Replace with your own username
<<<<<<< HEAD
    version="0.0.3.dev1",
=======
    version="0.0.1.dev1",
>>>>>>> 48b95196e1fc5efb1ac6a746763fdb651927283f
    author="Abishek Sriram",
    author_email="abisheksriram2001@gmail.com",
    description="File organiser with many ways",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/abisheksriram/fileG",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: Microsoft :: Windows",
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        
    ],
    python_requires='>=3.6',
)