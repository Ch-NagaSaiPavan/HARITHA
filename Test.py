import unittest
from fluent.runtime import FluentBundle, FluentResource

# Define helper functions to test the core Fluent functionality
def create_bundle(locale):
    return FluentBundle([locale])

def load_translation(bundle, translation_text):
    resource = FluentResource(translation_text)
    bundle.add_resource(resource)

def format_output(bundle, message_id, variables):
    message = bundle.get_message(message_id)
    if message and message.value:
        return bundle.format_pattern(message.value, variables)
    else:
        return "Message not found."

# Unit test cases for FluentTranslator functionalities
class TestFluentTranslator(unittest.TestCase):

    def setUp(self):
        # Set up a default locale and bundle for testing
        self.bundle = create_bundle("en-US")
        translation_text = "hello = Hello, { $name }!\nbye = Goodbye, { $name }!"
        load_translation(self.bundle, translation_text)

    def test_translation_with_variable(self):
        # Test translation with variable
        variables = {"name": "Alice"}
        result = format_output(self.bundle, "hello", variables)
        self.assertEqual(result, "Hello, Alice!")

    def test_translation_missing_variable(self):
        # Test handling of missing variable (should output partial or placeholder)
        variables = {}
        result = format_output(self.bundle, "hello", variables)
        self.assertIn("Hello,", result)

    def test_invalid_message_id(self):
        # Test with an invalid message ID
        variables = {"name": "Alice"}
        result = format_output(self.bundle, "invalid_id", variables)
        self.assertEqual(result, "Message not found.")

    def test_translation_extra_variable(self):
        # Test with extra, unused variable
        variables = {"name": "Alice", "extra": "extra_value"}
        result = format_output(self.bundle, "hello", variables)
        self.assertEqual(result, "Hello, Alice!")

    def test_load_invalid_translation(self):
        # Test loading an invalid translation
        with self.assertRaises(Exception):
            invalid_translation = "invalid = Hello {"
            load_translation(self.bundle, invalid_translation)

if __name__ == "__main__":
    unittest.main()
