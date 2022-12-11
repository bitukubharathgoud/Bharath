import requests
from bs4 import BeautifulSoup

def get_social_links(url):

    response = requests.get(url)
    html_content = response.text


    soup = BeautifulSoup(html_content, "html.parser")


    social_links = []
    for a_tag in soup.find_all("a", href=True):

        if "facebook" in a_tag["href"]:
            social_links.append(a_tag["href"])
        elif "linkedin" in a_tag["href"]:
            social_links.append(a_tag["href"])
        elif "twitter" in a_tag["href"]:
            social_links.append(a_tag["href"])
        elif "instagram" in a_tag["href"]:
            social_links.append(a_tag["href"])

    return social_links

def get_email(url):

    response = requests.get(url)
    html_content = response.text


    soup = BeautifulSoup(html_content, "html.parser")


    emails = []
    for a_tag in soup.find_all("a", href=True):

        if "mailto:" in a_tag["href"]:
            emails.append(a_tag["href"].replace("mailto:", ""))

    return emails

def get_contact(url):

    response = requests.get(url)
    html_content = response.text


    soup = BeautifulSoup(html_content, "html.parser")


    contact_numbers = []
    for p_tag in soup.find_all("p"):

        if any(char.isdigit() for char in p_tag.text):
            contact_numbers.append(p_tag.text)

    return contact_numbers


url = "https://ful.io"
social_links = get_social_links(url)
emails = get_email(url)
contacts = get_contact(url)

print("Social links:")
for social_link in social_links:
    print(social_link)

print("Email/s:")
for email in emails:
    print(email)

print("Contact:")
for contact in contacts:
    print(contact)
