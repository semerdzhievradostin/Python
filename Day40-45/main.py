from bs4 import BeautifulSoup
import requests
import textwrap

web_response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
web_response.raise_for_status()
movies_page = web_response.text
movies_soup = BeautifulSoup(movies_page, "html.parser")
movies = movies_soup.find_all("h3", class_="title")
movies_description = movies_soup.find_all("p", class_="description")
movies_list = []
movies_description_list = []
for movie in movies:
    movies_list.append(movie.getText())

for movie_description in movies_description:
    movies_description_list.append(movie_description.getText())

movies_list = movies_list[::-1]
movies_description_list = movies_description_list[::-1]
with open("Top100 Movies.txt", "w", encoding="utf-8") as file:
    for movie, description in zip(movies_list, movies_description_list):
        file.write(movie+f"\n"+f"{description[:4]}"+f"\n"+f"\n".join(textwrap.wrap(description[4:], width=100))+f"\n")

