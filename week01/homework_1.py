import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

cookies = '__mta=146748043.1593096826593.1593096826593.1593101206097.2; uuid_n_v=v1; uuid=AAF39620B6F311EA974289B279A7041DE1E2867CC1894438A266E003B6F6D7FD; _csrf=3b4acaadea17369401fc7266a65f399d9828d0f491c8794dcfa9569f4d0b302b; mojo-uuid=56cf790bcf39dbca432a2c96776bf631; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593096826; _lxsdk_cuid=172ebf86e7dc8-09a85107811ce9-31637403-13c680-172ebf86e7dc8; _lxsdk=AAF39620B6F311EA974289B279A7041DE1E2867CC1894438A266E003B6F6D7FD; __mta=146748043.1593096826593.1593096826593.1593096826593.1; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593101206; _lxsdk_s=172f0ea0549-651-07d-470%7C%7C1'

header = {'user-agent':user_agent, 'Cookie':cookies}

myurl = 'https://maoyan.com/films?showType=3'

response = requests.get(myurl,headers=header)

bs_info = bs(response.text, 'html.parser')

movieList = []

for tags in bs_info.find_all('div', attrs={'class': 'channel-detail movie-item-title'}):
    movieList.append((tags.find('a',).get('href')))

myMovies = []
for movieIndex in range(0,10):
    movieUrl = 'https://maoyan.com' + movieList[movieIndex]
    response = requests.get(movieUrl,headers=header)
    bs_info = bs(response.text, 'html.parser')
    for tags in bs_info.find_all('div', attrs={'class': 'movie-brief-container'}):
        name = tags.find('h1',).text
        types = []
        for movieTypes in tags.find_all('a',attrs={'class': 'text-link'}):
            types.append(movieTypes.text)
        i = 0
        for movieTime in tags.find_all('li',attrs={'class': 'ellipsis'}):
            i+=1
            if i == 3:
                upTime = movieTime.text
        myMovies.append({'name':name,'types':types,'time':upTime}) 

moviePd = pd.DataFrame(data=myMovies)
moviePd.to_csv('maoyan_movie.csv', encoding='utf-8', index=False, header=False)

