import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
import datetime

# Assuming the main code is saved in streamlit_app.py
from streamlit import get_hourly_quote, display_quote, custom_sidebar

# Mock data for testing
mock_quotes_df = pd.DataFrame({
    'Quote': ["Quote 1", "Quote 2", "Quote 3"],
    'Character': ["Character 1", "Character 2", "Character 3"]
})

class TestFluentTranslatorApp(unittest.TestCase):

    @patch('streamlit_app.quotes_df', mock_quotes_df)
    @patch('datetime.datetime')
    def test_get_hourly_quote(self, mock_datetime):
        # Mock the current hour to 1 for consistent results
        mock_datetime.now.return_value = datetime.datetime(2023, 10, 1, 1, 0, 0)
        
        # Test the quote retrieval based on the mocked hour
        quote, author, quote_index = get_hourly_quote()
        self.assertEqual(quote, "Quote 2")
        self.assertEqual(author, "Character 2")
        self.assertEqual(quote_index, 1)

    @patch('streamlit.sidebar.markdown')
    @patch('streamlit_app.get_hourly_quote')
    def test_display_quote(self, mock_get_hourly_quote, mock_sidebar_markdown):
        # Mock the get_hourly_quote function
        mock_get_hourly_quote.return_value = ("Test Quote", "Test Character", 1)
        
        # Call the display_quote function
        display_quote()
        
        # Check if sidebar markdown was called
        self.assertTrue(mock_sidebar_markdown.called)

    @patch('streamlit.sidebar.radio')
    def test_custom_sidebar(self, mock_radio):
        # Mock the sidebar radio to select "Text Translation"
        mock_radio.return_value = "Text Translation"
        
        # Call custom_sidebar and check the selected option
        choice = custom_sidebar()
        self.assertEqual(choice, "Text Translation")

if __name__ == "__main__":
    unittest.main()
