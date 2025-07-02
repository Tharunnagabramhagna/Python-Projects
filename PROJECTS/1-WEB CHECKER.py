print("🔍WEBSITE URL CHECKER🔍")
url = input("\nEnter a website URL: ")

if url.startswith("https://"):
    print("✅This  website uses HTTPS (secure)")  # eg:-https://google.com
elif url.startswith("http://"):
    print("❌This website uses HTTP (not secure)")  # eg:-http://google.com
else:
    print("🤔This doesn't look like a complete url")
