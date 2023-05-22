from setuptools import setup, find_packages

setup(
    name="auto-codebase-documenter",
    version="0.1",
    packages=find_packages(),
    install_requires=["openai", "python-dotenv"],
    entry_points={
        "console_scripts": [
            "auto-codebase-documenter = auto_codebase_documenter.run:main",
        ],
    },
)
