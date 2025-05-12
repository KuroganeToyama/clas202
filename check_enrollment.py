import requests
from bs4 import BeautifulSoup
import sys

url = "https://classes.uwaterloo.ca/cgi-bin/cgiwrap/infocour/salook.pl?level=under&sess=1255&subject=CLAS&cournum=202"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the first data row with enrollment data
for row in soup.find_all('tr'):
    cols = row.find_all('td')
    if len(cols) >= 12:
        try:
            cap = int(cols[8].text.strip())
            tot = int(cols[9].text.strip())
            if cap != tot:
                print(f"Alert: Space is available!")
                raise SystemExit("Enrollment check failed: Space is available!")
            else:
                print(f"Success: No space available.")
                raise SystemExit("Enrollment check passed: No space available.")
        except ValueError:
            continue  # Skip rows where conversion to int fails