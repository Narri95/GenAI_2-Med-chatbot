from setuptools import find_packages, setup

setup(
    name="medibot",
    version="0.1.0",
    author="Narendra Mucherla",
    author_email="narri2011@gmail.com",

    
    # Automatically looks for folders with an __init__.py (like your 'src' directory)
    packages=find_packages(), 
    
    # Tells setup to look inside the 'src' directory for the packages
    # packages=find_packages(where="src"),
    # package_dir={"": "src"},
    
    install_requires=[], # Dependencies can alternatively be managed here or via requirements.txt
    
)