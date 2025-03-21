from setuptools import setup, find_packages

setup(
    name="jinxify",
    version="0.1.5",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'jinxify = jinxify.cli:main',
        ],
    },
    python_requires='>=3.6',
    author="thenlko",
    author_email="vs1946213@email.com",
    description="Jinxify - Python with JavaScript like syntax adaptations.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language Python",
        "License :: OSI Approved :: MIT License",
    ],
)