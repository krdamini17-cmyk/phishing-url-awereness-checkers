# Phishing URL Awareness Checker

## Project overview
This beginner-friendly Python mini project checks URL text for selected phishing warning signs. It does **not** open websites, send URLs to a service, or prove that a URL is safe.

## Objectives
- Learn basic phishing awareness.
- Identify selected suspicious URL characteristics.
- Practice Python functions, conditions, loops, and URL parsing.

## Technologies
- Python 3.10 or later
- Visual Studio Code
- GitHub

## Features
- Checks for an `@` symbol.
- Flags URLs longer than 100 characters.
- Checks for an IPv4-like hostname.
- Flags hostnames with five or more segments.
- Checks for the `xn--` punycode marker.
- Flags URLs using HTTP.
- Lets you check multiple URLs in one run.

## How to run on Windows
1. Install Python 3.10 or later.
2. Open this folder in VS Code.
3. Open **Terminal → New Terminal**.
4. Run:

   ```bash
   python phishing_checker.py
   ```

   If that command is not recognized, try:

   ```bash
   py phishing_checker.py
   ```

5. Enter a sample URL when prompted. Type `q` to quit.

## Example
Input:

`http://192.0.2.10/account`

Expected warning signs include:
- Uses an IP-like hostname instead of a domain name.
- Uses HTTP; HTTPS alone does not prove trust.

## Testing
Run the tests with:

```bash
python -m unittest discover -s tests -v
```

See `tests/test_samples.md` for a manual test checklist.

## Screenshots
Save your own real program screenshots in the `screenshots` folder after running the project. Suggested names:
- `sample_run.png`
- `test_results.png`

## Limitations
These are simple text-based heuristics. They can produce false positives and false negatives. A URL with no listed warning signs may still be malicious. HTTPS does not guarantee that a website is trustworthy.

## Ethical use
Use this project for defensive learning and awareness. Do not enter passwords or other sensitive information into unknown websites.

## Author
Name: Damini K R
Course: BCA
