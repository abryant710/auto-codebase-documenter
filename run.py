import os
import argparse
from dotenv import load_dotenv
from codebase_documenter import CodebaseDocumenter
from codebase_documenter.config import config


def document_code(codebase_path):
    load_dotenv()  # load .env file
    openai_api_key = os.getenv("OPENAI_KEY")  # get OPENAI_KEY value from .env file

    documenter = CodebaseDocumenter(openai_api_key, codebase_path, config["ignore_folders"], config["file_types"])
    documenter.process_all_files()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Codebase Documenter.")
    parser.add_argument("codebase_path", type=str, help="The path to the codebase to document.")
    args = parser.parse_args()

    document_code(args.codebase_path)
