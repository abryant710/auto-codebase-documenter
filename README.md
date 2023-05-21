# Codebase Documenter

Codebase Documenter is a Python-based tool that uses the OpenAI GPT-3.5-turbo or GPT-4 model to assess and document a given codebase.

The tool walks through the directory of your project, ignoring certain directories (like virtual environments), and processes Python files. For each file, it uses the AI model to generate a written assessment of the file and writes the assessment into a `.md` file in a docs directory.

## Configuration

Edit the file `config.py` to configure the tool. The following parameters are available:

- `docs_intentions`: A list of intentions you want the AI model to follow when theity writes the documentation. This should follow a decent list of prompt items that should get the best out of the AI model.
- `ignore_folders`: A list of directories that you want to exclude from the documentation process.
- `file_types`: A list of file types (by extension) that you want to include in the documentation process.

## Setup

Before you start using Codebase Documenter, you need to set up a suitable Python environment. We recommend using a virtual environment (venv). Here's how you can set this up:

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

The easiest way to configure the app using the `config.py` file. Once you have configured the app, you can run it by executing the following command with an argument for the path to the root directory of the codebase you want to document:

```bash
python run.py /home/alex/projects/test_project
```

Alternatively, you can use the following code to run the app by importing the CodebaseDocumenter class:

```bash
from codebase_documenter import CodebaseDocumenter

documenter = CodebaseDocumenter(
  'your_openai_api_key',
  '/home/alex/projects/test_project',
  ['venv', 'another_folder'],
  ['.py', '.yaml']
)
documenter.process_all_files()
```

In the above code:

- Replace `your_openai_api_key` with your actual OpenAI API key.
- `/home/alex/projects/test_project` is the path of the root directory of the codebase that you want to document.
- ['venv', 'another_folder'] is a list of directories that you want to exclude from the documentation process.
- ['.py', '.yaml'] is a list of file types that you want to include in the documentation process.
  The process_all_files method will start processing the files.

## Output

This tool will create a `docs` directory in the root path of the project. Each processed file will have a corresponding `.md` file in the `docs` directory. The name of the text file is the same as the name of the processed file.

Each text file contains an assessment of the code in the file. The assessment is written by the OpenAI model.

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
