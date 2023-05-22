import os
import argparse
import yaml
from dotenv import load_dotenv
from auto_codebase_documenter.AutoCodebaseDocumenter import AutoCodebaseDocumenter


def load_config():
    config_file = os.path.join(os.getcwd(), "documenter_config.yaml")

    try:
        with open(config_file, "r") as stream:
            return yaml.safe_load(stream)
    except FileNotFoundError:
        print("Warning: 'documenter_config.yaml' file not found. Using defaults.")
        return {}
    except Exception as e:
        print(f"Warning: Error reading 'documenter_config.yaml'. Using defaults. Error: {str(e)}")
        return {}


def document_code(
    codebase_path, output_docs_folder_name, ignore_folders, file_types, single_file, skip_existing, debug, gpt_model
):
    load_dotenv()  # load .env file
    openai_api_key = os.getenv("OPENAI_KEY")  # get OPENAI_KEY value from .env file

    if openai_api_key is None:
        raise ValueError("The OPENAI_KEY environment variable is required to proceed.")

    documenter = AutoCodebaseDocumenter(
        openai_api_key,
        codebase_path,
        output_docs_folder_name,
        ignore_folders,
        file_types,
        single_file,
        skip_existing,
        debug,
        gpt_model,
    )

    if single_file:
        documenter.process_single_file(single_file)
    else:
        documenter.process_all_files()


def main():
    config = load_config()

    parser = argparse.ArgumentParser(description="Auto Codebase Documenter.")
    parser.add_argument("--codebase_path", type=str, help="The path to the codebase to document.")
    parser.add_argument(
        "--output_docs_folder_name",
        type=str,
        help="The name of the output docs folder.",
    )
    parser.add_argument("--ignore_folders", nargs="+", help="List of folders to ignore.")
    parser.add_argument("--file_types", nargs="+", help="List of file types to document.")
    parser.add_argument(
        "--skip_existing",
        action="store_true",
        help="Skip existing documentation files.",
    )
    parser.add_argument("--debug", action="store_true", help="Enable debug logging.")
    parser.add_argument(
        "--gpt_model",
        type=str,
        help="The GPT model to use. E.g., gpt-3.5-turbo gpt-4",
    )
    # parser.add_argument("--single_file", type=str, help="The path to a single file to document.")
    args = parser.parse_args()

    codebase_path = args.codebase_path if args.codebase_path else config.get("codebase_path", ".")
    ignore_folders = args.ignore_folders if args.ignore_folders else config.get("ignore_folders", ["venv"])
    file_types = args.file_types if args.file_types else config.get("file_types", [".py"])
    # single_file = args.single_file if args.single_file else config.get("single_file", False)
    output_docs_folder_name = (
        args.output_docs_folder_name if args.output_docs_folder_name else config.get("output_docs_folder_name", "docs")
    )
    skip_existing = args.skip_existing if args.skip_existing else config.get("skip_existing", False)
    debug = args.debug if args.debug else config.get("debug", False)
    gpt_model = args.gpt_model if args.gpt_model else config.get("gpt_model", "gpt-3.5-turbo")
    document_code(
        codebase_path, output_docs_folder_name, ignore_folders, file_types, False, skip_existing, debug, gpt_model
    )


if __name__ == "__main__":
    main()
