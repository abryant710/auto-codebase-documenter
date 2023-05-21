from datetime import datetime
import os
import yaml
import openai
from os.path import dirname, abspath
from .default_ai_prompt import default_ai_prompt


class CodebaseDocumenter:
    def __init__(
        self,
        openai_api_key,
        root_path=".",
        output_docs_folder_name="docs",
        ignore_folders=["venv"],
        file_types=[".py"],
        single_file=False,
    ):
        self.openai_api_key = openai_api_key
        self.root_path = root_path
        self.output_docs_folder_name = output_docs_folder_name
        self.ignore_folders = ignore_folders
        self.file_types = file_types
        self.base_dir = root_path
        self.docs_dir = os.path.join(self.base_dir, self.output_docs_folder_name)

        openai.api_key = self.openai_api_key

        # Create the docs folder if it doesn't exist
        if not os.path.exists(self.docs_dir):
            os.makedirs(self.docs_dir)

        # Load config from file
        self._load_config()

    def _load_config(self):
        # Check for config.yaml in the application's root directory
        parent_dir = dirname(abspath(__file__))  # directory of the current script
        root_dir = dirname(parent_dir)  # root directory of the application

        try:
            with open(os.path.join(root_dir, "config.yaml"), "r") as stream:
                config_data = yaml.safe_load(stream)
                self.ai_prompt_text = config_data.get("override_ai_prompt", default_ai_prompt)
                self.ignore_folders = config_data.get("ignore_folders", self.ignore_folders)
                self.file_types = config_data.get("file_types", self.file_types)
                # self.single_file = config_data.get("single_file", self.single_file)
                print("Using the prompt override from 'config.yaml'.")
                print("Custom prompt is set to the following:")
                print(self.ai_prompt_text)
        except FileNotFoundError:
            print("Warning: 'config.yaml' file not found. Using default doc intentions.")

            self.ai_prompt_text = default_ai_prompt
        except KeyError:
            print("Warning: 'override_ai_prompt' key not found in 'config.yaml'. Using default doc intentions.")

            self.ai_prompt_text = default_ai_prompt
        except Exception as e:
            print(f"Warning: Error reading 'config.yaml'. Using default doc intentions. Error: {str(e)}")

            self.ai_prompt_text = default_ai_prompt

    def _get_completion(self, prompt, model="gpt-3.5-turbo"):
        messages = [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=0,  # this is the degree of randomness of the model's output
        )
        return response.choices[0].message["content"]

    def _get_file_paths(self):
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

    def _process_file(self, file_path):
        with open(file_path, "r") as file:
            prompt = file.read()

            if not prompt.strip():
                return False, "Skipping empty file"

            prompt = f"""{'. '.join(self.ai_prompt_text)}.

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
                print("# Auto generated documentation file from codebase-documenter\n", file=output)
                timestamp = datetime.now().strftime("%d %B %Y at %H:%M:%S")
                print(f"This documentation file was created on {timestamp}\n", file=output)

                print("## File path\n", file=output)
                print(file_path, file=output)
                print("\n", file=output)
                response = self._get_completion(prompt)
                print(response, file=output)

                print(f"Wrote documentation file {output_file}")

            return True, "Processed file successfully"

    def process_all_files(self):
        file_paths = self._get_file_paths()
        total_files = len(file_paths)
        for i, file_path in enumerate(file_paths):
            print(f"Processing file {i+1}/{total_files}: {file_path}")
            success, message = self._process_file(file_path)
            if not success:
                print(f"{message} {i+1}/{total_files}: {file_path}")

    def process_single_file(self, file_path):
        print("TODO: Function not implemented yet")
        exit(1)
        # success, message = self._process_file(file_path)
        # if not success:
        #     print(f"{message}: {file_path}")
