import pyshorteners

def shorten_url(long_url):
    # Create a Shortener object
    s = pyshorteners.Shortener()

    # Use the tinyurl service to shorten the URL
    short_url = s.tinyurl.short(long_url)
    return short_url

def main():
    print("URL Shortener")
    
    # Input the long URL
    long_url = input("Enter the long URL: ")

    # Get the shortened URL
    short_url = shorten_url(long_url)

    print(f"Shortened URL: {short_url}")

if __name__ == "__main__":
    main()
