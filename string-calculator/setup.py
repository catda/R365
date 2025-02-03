from setuptools import setup, find_packages

setup(
    name="string-calculator",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    python_requires=">=3.8",
    author="Catherine Digua",
    description="A string calculator implementation supporting various delimiter formats",
    keywords="calculator, string, tdd",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
)