""" Erin Orbits
The first function, get_data, downloads the data if it is not present locally; if the data are already present,
then it takes no action. The second function, delete_data, removes the data if it is present locally.
The grading rubric is:
- Correctly implement get_data with an exception if the URL does not exist. (Hint: Try downloading the file using urllib3 instead of wget.) (2 pt)
- Correctly implement remove_data (1/2 pt)
- Implement tests for get_data that consider the following cases:
 > (a) file is present locally;
 > (b) file is not present locally, and the URL points to a file that exists; and
 > (c) URL does not point to a file that exists. (2 pt)
- Correctly implement tests for remove_data (1/2 pt)
Tests should be in a separate file from the functions get_data and remove_data.
"""
from getData_removeData import get_data
from getData_removeData import remove_data
import os
import requests
import unittest

class MyTestCase(unittest.TestCase):
    # test that file is present locally;
    def test_file_present(self):
        print("test_file_present")
        test_url = 'https://data.seattle.gov/resource/4xy5-26gy.csv'
        get_data(test_url)
        result = get_data(url=test_url)
        expected_result = "File already exists"
        self.assertEquals(result, expected_result)

    # test if file is not present locally
    def test_file_not_present(self):
        print("test_file_not_present")
        test_url = "http://www.spl.org/library-collection/articles-and-research/databases-a-z"
        # test_filename = "Imaginary_File"
        remove_data(test_url)
        result = get_data(url=test_url)
        self.assertEquals(result, "File downloaded")
        # test that the URL points to a file that exists
        # self.assertTrue(requests.get(test_url), msg = 'The url is valid')

    # test that the URL does not point to a file that exists
    def test_url_file(self):
        print("test_url_file")
        test_url = 'https://seattle.gov/resource/4xy5-26gy'
        result = get_data(test_url)
        self.assertEquals(result, "Invalid url")

    # remove_data test that file is present locally
    def remove_data_test_file_present(self):
        print("remove_data_test_file_present")
        test_url = 'https://data.seattle.gov/resource/4xy5-26gy.csv'
        get_data(test_url)
        result = remove_data(test_url)
        self.assertEquals(result, "File removed")

    # remove_data test that the file is removed
    def test_file_removed(self):
        print("test_file_removed")
        test_url = 'https://data.seattle.gov/resource/4xy5-26gy.csv'
        get_data(test_url)
        result = remove_data(test_url)
        self.assertEquals(result, "File removed")

    # remove_data test that the file doesn't exist
    def remove_data_test_file_not_present(self):
        print("remove_data_test_file_not_presen")
        test_url = 'https://data.seattle.gov/resource/4xy5-26gy.csv'
        remove_data(test_url)
        result = remove_data(test_url)
        expected_result = "File doesn't exist"
        self.assertEquals(result, expected_result)

    # remove-Data test with bad url
    def remove_data_test_bad_url(self):
        print("remove_data_test_bad_url")
        bad_url = "www.imaginary.en"
        result = remove_data(bad_url)
        self.assertEquals(result, "File doesn't exist")

if __name__ == '__main__':
    unittest.main()
