from bs4 import BeautifulSoup
import requests

"""with open("website.html" ,'r' ) as file:
    contents = file.read()
    
    
    
soup = BeautifulSoup(contents,"html.parser")


for link in soup.find_all('li'):
    print(link.get("href"))"""
    
    
    
    
response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

response = response.text
 

#print(response)



soup = BeautifulSoup(response , "html.parser")



        
    



movie_list = []

for titles in soup.find_all(name="h3", class_="listicleItem_listicle-item__title__hW_Kn"):
    movie_list.append(titles.getText())







with open("movie_list.txt" , "a") as file:
    num = -1

    iteration = 1
    while iteration < 101:
        print(movie_list[num])
        file.write(f"{movie_list[num]} \n")
        num = num -1
        iteration = iteration + 1

























"""for link in soup.find_all(name="span" , class_="titleline"):
    print(link.getText())
    print(link.get("href"))"""
    
    
"""upvote = soup.find(name="span", class_="score")
print(upvote.getText())


for upvotes in soup.find_all(name="span", class_= "score"):
    print(upvote.getText())"""
    
    
"""# Find the anchor tag within the span with class "titleline"
link = soup.find('span', class_='titleline').find('a')

# Extract the 'href' attribute from the anchor tag
href = link.get('href')

print("Link:", href)"""


