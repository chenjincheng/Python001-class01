#encoding:utf-8
import requests
from bs4 import BeautifulSoup
import pandas

url = 'https://maoyan.com/films?showType=3'
user_agent =  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
cookie = 'uuid_n_v=v1; uuid=1F401820B95E11EA8E55532676AF0F4AF41FE8F97E5C4729B0B94E46AD3FA877; mojo-uuid=20f3a7cc12fb2a06f2a5000a5ab96acc; _lxsdk_cuid=172fbcd87e3c8-089042fd9b8e51-b791b36-144000-172fbcd87e3c8; _lxsdk=1F401820B95E11EA8E55532676AF0F4AF41FE8F97E5C4729B0B94E46AD3FA877; _csrf=9168db558e10cf4c19acd18727733fd8ffd838d449c56e3fe9b2cc2cb563d49e; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593445785,1593448430,1593448447,1593526128; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593527029; __mta=217488681.1593362450474.1593527025803.1593527029357.26; _lxsdk_s=17305c1ca68-56b-5d2-236%7C%7C1'
headers = {'user-agent' : user_agent, 'cookie' : cookie}

reponse = requests.get(url,headers = headers)

html = BeautifulSoup(reponse.text, 'html.parser')

movies = html.find('dl', attrs={'class' : 'movie-list'}).find_all('dd')

count = 0
data = {'名称' : [], '类型' : [], '上映时间' : []}
for movie in movies :
    movie_infos = movie.find_all('div', attrs={'class' : 'movie-hover-title'})
    # print(f"名称：{movie_infos[0].find('span').text}")
    # print(f"类型：{movie_infos[1].text.replace('类型:', '').strip()}")
    # print(f"上映时间：{movie_infos[3].text.replace('上映时间:', '').strip()}")
    # print(f"--------------------------------------------------------")

    data['名称'].append(movie_infos[0].find('span').text)
    data['类型'].append(movie_infos[1].text.replace('类型:', '').strip())
    data['上映时间'].append(movie_infos[3].text.replace('上映时间:', '').strip())

    count += 1
    if count >= 10 :
        break

movie_df = pandas.DataFrame(data)
movie_df.to_csv('top10_movies.csv', encoding='GBK', index=False, header=True)
