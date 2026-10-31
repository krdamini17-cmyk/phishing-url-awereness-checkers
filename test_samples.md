# Manual Test Checklist

Run `python phishing_checker.py`, test each input, and record the actual result.

| # | Sample input | Expected check |
|---|---|---|
| 1 | `https://www.example.com/login` | No listed warning signs (does not prove safety) |
| 2 | `http://192.0.2.10/account` | IP-like hostname and HTTP |
| 3 | `http://example.com@sample.invalid/login` | `@` symbol and HTTP |
| 4 | `https://a.b.c.d.e.example.invalid/path` | Many hostname segments |
| 5 | `https://xn--example.invalid/` | Punycode marker |

Fill in your date, Python version, actual result, and PASS/FAIL after testing. Do not claim a test passed unless you ran it.
