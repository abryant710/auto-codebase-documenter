import os
from dotenv import load_dotenv
from auto_codebase_documenter import AutoCodebaseDocumenter

load_dotenv()  # load .env file
openai_api_key = os.getenv("OPENAI_KEY")  # get OPENAI_KEY value from .env file{}

documenter = AutoCodebaseDocumenter(openai_api_key)
documenter.process_all_files()
