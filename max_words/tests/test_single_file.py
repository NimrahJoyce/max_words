from unittest import mock
from unittest.mock import mock_open
from max_words.max_words.app.words_in_file import words_in_file

#test function for the main function
@mock.patch('builtins.open', new_callable=mock_open, create=True)
def test_single_file(mock_open):
    mock_open.return_value.__enter__ = mock_open
    mock_open.return_value.__iter__ = mock.Mock(
        return_value=iter(['alef', 'bet']))
    words_dict = words_in_file('foo')
    assert len(words_dict) == 2
    assert not words_dict['alef'] == 1
