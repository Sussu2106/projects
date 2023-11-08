import requests
from bs4 import BeautifulSoup as bs

github_user = input('User do GitHub: ')
url = 'https://github.com/' + github_user
r = requests.get(url)
soup = bs(r.content, 'html.parser')
profile_image = soup.find('img', class_= ['avatar', 'avatar_user'])
if profile_image:
    profile_image = profile_image.get('src')
    print(profile_image)
else:
    print("Nenhuma imagem de perfil encontrada.")

