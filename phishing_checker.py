import re
from urllib.parse import urlparse


def inspect_url(raw_url):
    """Check URL text for selected warning signs; does not visit the URL."""
    url = raw_url.strip()
    if not url:
        return ["No URL entered."]

    candidate = url if "://" in url else "http://" + url

    try:
        parsed = urlparse(candidate)
        host = (parsed.hostname or "").lower()
    except ValueError:
        return ["Invalid URL format."]

    if not host:
        return ["Could not identify a hostname."]

    findings = []

    if "@" in candidate:
        findings.append("Contains an @ symbol; inspect carefully.")

    if len(url) > 100:
        findings.append("Unusually long URL (over 100 characters).")

    # A simple IPv4-like hostname check, not a full IP validator.
    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", host):
        findings.append("Uses an IP-like hostname instead of a domain name.")

    labels = [part for part in host.split(".") if part]
    if len(labels) >= 5:
        findings.append("Contains many hostname segments/subdomains.")

    if "xn--" in host:
        findings.append("Contains a punycode marker (xn--).")

    if parsed.scheme.lower() == "http":
        findings.append("Uses HTTP; HTTPS alone does not prove trust.")

    if not findings:
        findings.append(
            "No listed warning signs found. This does NOT prove the URL is safe."
        )

    return findings


def main():
    print("=" * 48)
    print("       Phishing URL Awareness Checker")
    print("=" * 48)
    print("Text checks only: this program does not open URLs.")
    print("Type q to quit.")

    while True:
        raw_url = input("\nEnter a URL to check: ").strip()

        if raw_url.lower() in {"q", "quit", "exit"}:
            print("Goodbye! Stay alert online.")
            break

        findings = inspect_url(raw_url)
        print("\nResult:")
        for finding in findings:
            print(f"- {finding}")

        if findings and not findings[0].startswith(
            ("No URL entered.", "Invalid URL format.", "Could not identify a hostname.")
        ) and not findings[0].startswith("No listed warning signs"):
            print(f"\nReview carefully: {len(findings)} warning sign(s) found.")

        print("\nReminder: never enter passwords from unexpected links.")


if __name__ == "__main__":
    main()
