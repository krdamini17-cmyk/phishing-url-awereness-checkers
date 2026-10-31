import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from phishing_checker import inspect_url


class TestInspectURL(unittest.TestCase):
    def test_http_ip_hostname(self):
        result = inspect_url("http://192.0.2.10/account")
        joined = " ".join(result)
        self.assertIn("IP-like hostname", joined)
        self.assertIn("Uses HTTP", joined)

    def test_https_example_no_listed_warnings(self):
        result = inspect_url("https://www.example.com/login")
        self.assertTrue(any("No listed warning signs" in item for item in result))

    def test_at_symbol(self):
        result = inspect_url("http://example.com@sample.invalid/login")
        self.assertTrue(any("@ symbol" in item for item in result))

    def test_punycode_marker(self):
        result = inspect_url("https://xn--example.invalid/")
        self.assertTrue(any("punycode marker" in item for item in result))

    def test_empty_input(self):
        self.assertEqual(inspect_url("   "), ["No URL entered."])


if __name__ == "__main__":
    unittest.main()
