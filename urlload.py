from bs4 import BeautifulSoup
import ssl
import codecs

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

file = input("Enter file- ")
html = open(file).read()
soup = BeautifulSoup(html, "html.parser")

fhand = codecs.open('list.data', 'w', "utf-8")

tags=soup('a')
for tag in tags :
	check = tag.get('href', None)
	if check.startswith("/reviews/") :
		entry = tag.text
		output = entry+"\n"
		fhand.write(output)
		print(output)