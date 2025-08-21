import requests
import hashlib
from bs4 import BeautifulSoup

# Website you want to check
URL = "https://www.randomnumberapi.com/api/v1.0/random?min=1&max=1000&count=1"

def get_page_hash(url):
    response = requests.get(url)          # download the webpage
    soup = BeautifulSoup(response.text, "html.parser")  
    content = soup.get_text()             # extract only text (ignore HTML tags)
    return hashlib.md5(content.encode("utf-8")).hexdigest()
#collect curent and present hash




hash1=get_page_hash(URL)
# Open a file in write mode ("w")
file = open("hash.txt", "w")

# Write text into it
file.write(hash1)
# Always close the file to save changes
file.close()
with open("hash.txt","r") as file:
    hash1=file.read().strip()
hash2=get_page_hash(URL)
if hash1==hash2:
    print("no change")
else:
    print("change detected")


print("website:",URL)
print("hash:",hash1)
print("hash2:",hash2)

# if hash1==hash2:
#     print("no change")
#     #print("hash:",hash1)
# else:
#     print("change detected")
    #print("hash1:",hash1)
    #print("hash2:",hash2)
#print("Website:", URL)
#print("Hash value:", page_hash)
