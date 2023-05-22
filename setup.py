from setuptools import setup, find_packages

setup(
    name="auto-codebase-documenter",
    version="0.10",
    packages=find_packages(),
    install_requires=["openai", "python-dotenv", "PyYAML"],
    entry_points={
        "console_scripts": [
            "auto-codebase-documenter = auto_codebase_documenter.auto_documenter:main",
        ],
    },
    author="Alex Bryant",
    author_email="alexbryant710@gmail.com",
    description="Automatic codebase documentation tool using OpenAI GPT models",
    long_description="This tool utilizes OpenAI GPT models to automatically assess and document a codebase by generating written assessments for each file.",
    long_description_content_type="text/markdown",
    url="https://github.com/abryant710/auto-codebase-documenter",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license="MIT",
    platforms=["any"],
)
