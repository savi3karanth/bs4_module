from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print()
print(f"which prints the title tag\n{soup.title}\n")#
print(f"which prints the name of tag\n {soup.title.name}\n")  #
print(f"which prints the string in the title \n{soup.title.string}\n")
print(f"which prints the code with no indentation\n{soup}\n")
print(f"which will be formatted to indent \n{soup.prettify()}\n")
print("which prints the first anchor tag \n{soup.a}\n")
print(f"which prints the first list tag\n{soup.li}\n")
print(f"which prints only the first paragraph tag \n{soup.p}\n")

print()
