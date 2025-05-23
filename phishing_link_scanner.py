import requests
from bs4 import BeautifulSoup
import tldextract
import ssl
import socket
from urllib.parse import urlparse
import whois

def validate_url(url):
    try:
        result = urlparse(url)
        return result.scheme in ["http", "https"]
    except:
        return False

def check_ssl(url):
    try:
        cert = ssl.get_server_certificate((url, 443))
        return True
    except:
        return False

def check_blacklist(url):
    # You can integrate APIs like Google Safe Browsing or VirusTotal
    # Here, you can check a simple mock blacklist or integrate third-party APIs
    blacklisted_domains = ['malicioussite.com', 'phishingsite.net']
    domain = tldextract.extract(url).domain
    if domain in blacklisted_domains:
        return True
    return False

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Example: Check for login forms
    if soup.find('form') and ('login' in soup.text.lower() or 'password' in soup.text.lower()):
        return True
    return False

def phishing_link_scanner(url):
    if not validate_url(url):
        return "Invalid URL format."
    
    if check_blacklist(url):
        return "Phishing site detected (blacklisted)."
    
    if not check_ssl(url):
        return "Warning: No SSL certificate (HTTPS)."
    
    if scrape_website(url):
        return "Warning: This site might be trying to steal your credentials."
    
    return "The website appears safe."

# Example usage
url = input("Enter the URL to scan: ")
result = phishing_link_scanner(url)
print(result)
