import openai
import os
from datetime import datetime

from codebase_documenter.config import config


class CodebaseDocumenter:
    def __init__(self, openai_api_key, root_path, ignore_folders=["venv"], file_types=[".py"]):
        self.openai_api_key = openai_api_key
        self.root_path = root_path
        self.ignore_folders = ignore_folders
        self.file_types = file_types
        self.base_dir = root_path
        self.docs_dir = os.path.join(self.base_dir, "docs")

        openai.api_key = self.openai_api_key

        # Create the docs folder if it doesn't exist
        if not os.path.exists(self.docs_dir):
            os.makedirs(self.docs_dir)

    def get_completion(self, prompt, model="gpt-3.5-turbo"):
        messages = [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=0,  # this is the degree of randomness of the model's output
        )
        return response.choices[0].message["content"]

    def get_file_paths(self):
        file_paths = []
        for dirpath, dirnames, filenames in os.walk(self.root_path):
            for ignore_folder in self.ignore_folders:
                if ignore_folder in dirnames:
                    dirnames.remove(ignore_folder)
            file_paths.extend(
                [
                    os.path.join(dirpath, filename)
                    for filename in filenames
                    if any(filename.endswith(file_type) for file_type in self.file_types)
                ]
            )
        return file_paths

    def process_file(self, file_path):
        skip = False
        with open(file_path, "r") as file:
            prompt = file.read()

            if not prompt.strip():
                return False, "Skipping empty file"

            prompt = f"""{'. '.join(config['docs_intentions'])}.

            Please assess the following file:

            {prompt}
            """

            # Get the relative path of the file
            relative_path = os.path.relpath(file_path, self.base_dir)

            # Create the directory structure in the docs folder
            output_dir = os.path.dirname(os.path.join(self.docs_dir, relative_path))
            os.makedirs(output_dir, exist_ok=True)

            # Define the output file path
            file_name = os.path.basename(file_path)
            output_file = os.path.join(output_dir, f"{file_name}.md")

            # Check if the file already exists
            if os.path.exists(output_file):
                print(f"WARNING: Documentation file {output_file} already exists and will be overwritten.")

            with open(output_file, "w") as output:
                # Add timestamp at the top of the file
                print("# Auto generated documentation file\n", file=output)
                timestamp = datetime.now().strftime("%d %B %Y at %H:%M:%S")
                print(f"This documentation file was created on {timestamp}\n", file=output)

                print("## File path\n", file=output)
                print(file_path, file=output)
                response = self.get_completion(prompt)
                print(response, file=output)

                print(f"Wrote documentation file {output_file}")

            return True, "Processed file successfully"

    def process_all_files(self):
        file_paths = self.get_file_paths()
        total_files = len(file_paths)
        for i, file_path in enumerate(file_paths):
            print(f"Processing file {i+1}/{total_files}: {file_path}")
            success, message = self.process_file(file_path)
            if not success:
                print(f"{message} {i+1}/{total_files}: {file_path}")
