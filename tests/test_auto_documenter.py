import unittest
from unittest.mock import patch, Mock, mock_open
from auto_codebase_documenter.auto_documenter import AutoCodebaseDocumenter


class TestAutoCodebaseDocumenter(unittest.TestCase):
    def setUp(self):
        self.documenter = AutoCodebaseDocumenter(
            openai_api_key="fake_key",
            root_path=".",
            output_docs_folder_name="test_docs",
        )

    @patch("openai.ChatCompletion.create")
    def test_get_completion(self, mock_openai_chat_completion_create):
        mock_choice = Mock()
        mock_choice.message = {"role": "assistant", "content": "Test content"}

        mock_response = Mock()
        mock_response.choices = [mock_choice]

        mock_openai_chat_completion_create.return_value = mock_response

        prompt = "Test prompt"
        result = self.documenter._get_completion(prompt)
        self.assertEqual(result, "Test content")

    def test_get_file_paths(self):
        result = self.documenter._get_file_paths()
        self.assertTrue(isinstance(result, list))

    @patch("os.path.exists")
    @patch("builtins.open", new_callable=mock_open, read_data="test file content")
    @patch("openai.ChatCompletion.create")
    def test_process_file(
        self, mock_openai_chat_completion_create, mock_file, mock_exists
    ):
        mock_choice = Mock()
        mock_choice.message = {"role": "assistant", "content": "Test content"}

        mock_response = Mock()
        mock_response.choices = [mock_choice]

        mock_openai_chat_completion_create.return_value = mock_response

        mock_exists.return_value = False
        success, message = self.documenter._process_file("test_file_path")
        self.assertTrue(success)
        self.assertEqual(message, "Processed file successfully")


if __name__ == "__main__":
    unittest.main()
