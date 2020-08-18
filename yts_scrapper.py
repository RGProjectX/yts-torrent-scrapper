'''
Script Developed By : RGProjectX
Github : https://github.com/RGProjectX/yts-torrent-scrapper
Telegram : https://telegram.dog/RandomGuyRG69
'''
from bs4 import BeautifulSoup
import requests

name = input("Enter Movie Name : ")
print("")
for page in range(1,2):
			    #Returns Movies Based On Seeds
			    url = "https://yts.mx/browse-movies/"+str(name)+"/all/all/0/seeds/0/all"
			    r = requests.get(url).text
			    soup = BeautifulSoup(r, "lxml")
			    for name in soup.findAll(
			        "div", class_="browse-movie-wrap col-xs-10 col-sm-4 col-md-5 col-lg-4"
			    ):
			        mov_name = name.find("div", class_="browse-movie-bottom")
			        movie_name = mov_name.a.text
			        movie_year = mov_name.div.text
			        movie_name = movie_name + " " + movie_year
			        rating = name.find("h4", class_="rating",text=True)
			        if rating is not None:
			        	rating = rating.text
			        	rating = rating[:3]
			        else:
			        	rating = "0.0"
			        if rating[2] == "/":
			            rating = rating[0:2]
			        try:
			            #Handles Movie Name Containing [xx]
			            if movie_name[0] == "[" and movie_name[3] == "]":
			            	movie_name = movie_name[5:]
			            movie_name = movie_name.replace(" ", "-")
			            index = 0
			            for char in movie_name:  #Handles Special Character In Url
			                if char.isalnum() == False and char != "-":
			                    movie_name = movie_name.replace(char, "")
			            for char in movie_name:
			                if char == "-" and movie_name[index + 1] == "-":
			                    movie_name = movie_name[:index] + movie_name[index + 1 :]    
			                if index < len(movie_name) - 1:
			                    index = index + 1
			            if "--" in movie_name: #Handles Movie Url Containing "--"
			            	movie_name = movie_name.replace("--","-")  					
			            movie_url = "https://yts.mx/movie/" + movie_name
			            movie_url = movie_url.lower()
			            request = requests.get(movie_url).text
			            n_soup = BeautifulSoup(request, "lxml")
			            info = n_soup.find("div", class_="bottom-info")
			            torrent_info = n_soup.find("p", class_="hidden-xs hidden-sm")
			            genre = n_soup.findAll("h2")[1].text
			            likes = info.find("span", id="movie-likes").text
			            imdb_link = info.find("a", title="IMDb Rating")["href"]
			            for torrent in torrent_info.findAll("a"):
			                if (
			                    torrent.text[:3] == "720"
			                ): 
			                    torrent_720 = torrent["href"]
			                if torrent.text[:4] == "1080":
			                    torrent_1080 = torrent["href"]
			        except Exception as e:
			            likes = None
			            genre = None
			            num_downloads = None
			            imdb_link = None
			            torrent_720 = None
			            torrent_1080 = None
			            pass
			        movie_name = mov_name.a.text
			        print("YTS Link :",movie_url)
			        print("Name :",movie_name)
			        print("Year :",movie_year)
			        print("IMDb Links :", imdb_link)
			        print("Genre :", genre)
			        print("IMDb Ratings :", rating)
			        print("Likes :", likes)
			        print("720p Torrent :", torrent_720)
			        print("1080p Torrent :", torrent_1080)
			        print("")

print("Done Scrapping...!!")
			
			