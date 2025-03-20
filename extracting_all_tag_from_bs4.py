from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents)
all_anchor_tag =soup.findAll(name="a")
print(f"which prints all the anchor tag from the code \n{all_anchor_tag}\n")

print(f"which prints all the string in the anchor tag")
for tag in all_anchor_tag:
    print(tag.getText())
print()

print(f"prints all the link from that anchor tag")
for tag in all_anchor_tag:
    print(tag.get('href'))
print()

#If there is one more h1 with different value it won't print Here it prints the h1 only if the id is name
heading = soup.find(name="h1", id="name")
print(f"finds the first attribute and value prints the output\n{heading}\n")

section_heading = soup.find(name="h3", class_="heading")
print(f"finds the attribute but since the attribute is class we need to write _after class attribute that fixes the error\n{section_heading}\n")
print(f"if we want to print the text 'Books and Teaching' that contains h3 \n{section_heading.getText()}\n")
print(f"if we want to knw the name 'h3' of that particular tag h3 \n{section_heading.name}\n")
print(f"if we want to get the value ['heading'] of that class tag h3 \n{section_heading.get('class')}\n")

company_url = soup.select(selector='p a')
print(f"selects all the p , a in the company_url {company_url}")

name = soup.select_one(selector="#name")
print(f"selects first id name in the h1 {name}")
print()

heading = soup.select(selector=".heading")
print(f"prints all the selector if had one or more class with the name heading ie \n{heading}")
