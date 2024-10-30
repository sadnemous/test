import unittest
from unittest.mock import patch, MagicMock
from main import len_joke, get_joke

class TestJoke(unittest.TestCase):
    @patch('main.get_joke')
    def test_len_joke(self, mock_get_joke):
        mock_get_joke.return_value = 'One'
        self.assertEqual(len_joke(), 3)

    @patch('main.requests')
    def test_get_joke(self, mock_request):
        #ques='Did you hear about the crime in the parking garage?'
        #ans='It was wrong on so many levels.'
        ques = 'setup'
        ans ='pl'
        assert_str = f"Setup: {ques}\nAns  : {ans}"
        #assert_str = f"{ques}{ans}"
        mock_response = MagicMock(status_code = 200)
        mock_response.json.return_value = {'setup':ques, 'punchline':ans}
        mock_request.get.return_value = mock_response
        self.assertEqual(get_joke(), assert_str)
        
    @patch('main.requests')
    def test_failed_get_joke(self, mock_request):
        assert_str = f"No jokes"
        mock_response = MagicMock(status_code = 403)
        mock_response.json.return_value = {'setup':'ques', 'punchline':'ans'}
        mock_request.get.return_value = mock_response
        self.assertEqual(get_joke(), assert_str)

if __name__ == '__main__':
    unittest.main()