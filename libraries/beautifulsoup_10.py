from bs4 import BeautifulSoup

html = "<html><body><h1>Hello</h1><p>World</p></body></html>"
soup = BeautifulSoup(html, "html.parser")

print("Heading:", soup.h1.text)
print("Paragraph:", soup.p.text)
