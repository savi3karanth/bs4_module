import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
html_website = response.text

soup = BeautifulSoup(html_website, "html.parser")
all_movies = soup.find_all("h3", class_="title")
movie_list = [movie.getText() for movie in all_movies]
for n in range(len(movie_list)-1, -1, -1):
    print(movie_list[n])

with open("movie.txt", "w") as file:
    for movie in movie_list:
        file.write(f"{movie}\n")