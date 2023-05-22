# Auto Codebase Documenter

Auto Codebase Documenter is a Python-based tool that leverages the power of the OpenAI GPT-3.5-turbo or GPT-4 model to automatically assess and document a codebase.

This tool simplifies the process of documenting your project by walking through the directory of your codebase, selectively ignoring certain directories (such as virtual environments), and processing the Python files found. It harnesses the capabilities of the AI model to generate a comprehensive written assessment of each file. The assessments are then organized and stored in Markdown (`.md`) files within a dedicated `docs` directory.

By automatically analyzing your codebase and providing detailed explanations, suggestions, and insights, the Auto Codebase Documenter facilitates the understanding of your project's structure, purpose, and functionality. The generated documentation can serve as a
valuable resource for new developers joining the project or as an aid for code review and refactoring processes.

## Installation

You can install `auto-codebase-documenter` using `pip` from the Python Package Index (PyPI).

```bash
pip install auto-codebase-documenter
```

The package is hosted on PyPI and can be found at <https://pypi.org/project/auto-codebase-documenter>. You can visit the link for more information about the package and its available versions.

## Setup

Before you start using Auto Codebase Documenter, you need to set up a suitable Python environment. We recommend using a virtual environment (venv). Here's how you can set this up:

1. Install Python 3.9.16. You can download it from the official Python website. Make sure to allow the installer to set the PATH variables for you.

2. Check your Python version by running `python --version` or `python3 --version` from the command line. It should display `Python 3.9.16`.

3. Once you have the correct Python version, you can create a virtual environment. To do this, run the following command in the root directory of the project:

   ```bash
   python -m venv venv
   ```

   This command creates a new directory named `venv` in your project. This directory will contain the Python executable files and a copy of the pip library which you can use to install other packages within this environment.

4. To start using this environment, you have to activate it.

   On Unix or MacOS, run:

   ```bash
   source venv/bin/activate
   ```

   On Windows, run:

   ```bash
   venv\Scripts\activate
   ```

5. Once the virtual environment is activated, you can install the necessary dependencies. To do this, run the following command:

   ```bash
   pip install -r requirements.txt
   ```

6. Now you should be all set! Remember to activate the venv environment every time you work on the project.

7. Finally, ensure you have an OpenAI API key. The API key is necessary for making requests to the OpenAI service.

## Usage

### Importing the package

The easiest way to use the tool is to create a file called `documenter.py` and add the following code to run the app by importing the `AutoCodebaseDocumenter` class:

```python
import os
from dotenv import load_dotenv
from auto_codebase_documenter import AutoCodebaseDocumenter

load_dotenv()  # load .env file
openai_api_key = os.getenv("OPENAI_KEY")  # get OPENAI_KEY value from .env file{}

documenter = AutoCodebaseDocumenter(openai_api_key)
documenter.process_all_files()
```

The `process_all_files` method will start processing the files.

You can add the `config.yaml` into the same folder to customize the tool.

### CLI

TODO: Add CLI usage instructions

## Configuration

Edit the `config.yaml` file to configure the tool. The following parameters are available:

- `override_ai_prompt`: A list of intentions you want the AI model to follow when it writes the documentation. This should follow a decent list of prompt items that should get the best out of the AI model.

- `ignore_folders`: A list of directories that you want to exclude from the documentation process.

- `file_types`: A list of file types (by extension) that you want to include in the documentation process.

- `single_file`: A boolean indicating whether a single file should be processed. If True, provide the path to the file. Defaults to False.

- `output_docs_folder_name`: The name of the output docs folder. Defaults to "docs".

Alternatively, these parameters can be passed as command line arguments when running the tool. If command line arguments are provided, they will override the corresponding values in config.yaml.

Here's an example of how your config.yaml could look:

```yaml
output_docs_folder_name: "docs"
ignore_folders:
  - "venv"
file_types:
  - ".py"
single_file: False
override_ai_prompt:
  - "You are a highly skilled software engineer and software architect"
  - "You are analysing another person's code and writing a report on each file in a codebase"
  - "You will provide feedback for each file and suggest improvements where necessary"
  - "Please give a detailed account of how every Class, method, decorator, and important variable works in the code and its intention"
  - "Lay everything out so a new developer can really understand what the code is supposed to do"
```

## Output

This tool will create a `docs` directory at the root path of the project or to the location specified by the `output_docs_folder_name` parameter. The structure of the `docs` directory will mimic the structure of your codebase. For each processed file in your codebase, there will be a corresponding `.md` (Markdown) file in the `docs` directory, placed in the same relative location as the original file in the codebase.

The name of the Markdown file will be the same as the name of the processed file in the codebase, retaining the original file extension as part of the name. For example, if the original file was named `main.py`, the corresponding documentation file will be named `main.py.md`.

Each Markdown file will contain an AI-generated assessment of the code in the corresponding file. The assessment is created using the GPT-4 model from OpenAI and follows the intentions specified in the `override_ai_prompt` parameter in `config.yaml`. It will provide an analysis of the code, suggestions for improvements, and detailed explanations of classes, methods, decorators, and important variables in the file.

The assessment aims to provide comprehensive information that can help a new developer understand the purpose and functionality of the code, as well as areas that could potentially be refactored or optimized.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Support

This project is maintained by volunteers and funded by donations from the community. If you find this project useful and would like to support its continued development and maintenance, you can do so by sending a donation to one of the following addresses:

PayPal: Please send donations to <https://www.paypal.com/paypalme/alexbryant710>

Bitcoin (BTC): Please send Bitcoin donations to the following address: your-btc-address.

Ethereum (ETH): Please send Ethereum donations to the following address: your-eth-address.

Solana (SOL): Please send Solana donations to the following address: your-sol-address.

Donations are completely optional but greatly appreciated. They will be used to pay for server costs, development tools, and coffee for late-night coding sessions!

Thank you for your support!
