import os
import argparse
from dotenv import load_dotenv
from codebase_documenter import CodebaseDocumenter


def document_code(codebase_path, ignore_folders, file_types, single_file=None):
    load_dotenv()  # load .env file
    openai_api_key = os.getenv("OPENAI_KEY")  # get OPENAI_KEY value from .env file

    if openai_api_key is None:
        raise ValueError("The OPENAI_KEY environment variable is required to proceed.")

    documenter = CodebaseDocumenter(openai_api_key, codebase_path, ignore_folders, file_types)

    if single_file:
        documenter.process_single_file(single_file)
    else:
        documenter.process_all_files()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Codebase Documenter.")
    parser.add_argument("codebase_path", type=str, help="The path to the codebase to document.")
    parser.add_argument("--ignore_folders", nargs="+", default=["venv"], help="List of folders to ignore.")
    parser.add_argument("--file_types", nargs="+", default=[".py"], help="List of file types to document.")
    parser.add_argument("--single_file", type=str, help="The path to a single file to document.")
    args = parser.parse_args()

    document_code(args.codebase_path, args.ignore_folders, args.file_types, args.single_file)
