import requests
from bs4 import BeautifulSoup

# Step 1: Choose a news website (example: BBC News)
url = "https://www.bbc.com/news"

# Step 2: Fetch the webpage content
response = requests.get(url)
if response.status_code != 200:
    print("Failed to retrieve the page")
    exit()

# Step 3: Parse the HTML
soup = BeautifulSoup(response.text, "html.parser")

# Step 4: Extract headlines (BBC uses <h2> for headlines)
headlines = []
for h2 in soup.find_all("h2"):
    headline = h2.get_text(strip=True)
    if headline:  # ensure it's not empty
        headlines.append(headline)

# Step 5: Save to a text file
with open("headlines.txt", "w", encoding="utf-8") as f:
    for line in headlines:
        f.write(line + "\n")

print("✅ Headlines saved to headlines.txt")
