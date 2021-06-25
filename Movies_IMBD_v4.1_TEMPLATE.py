#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter


# In[281]:


data = pd.read_csv('movie_bd_v5.csv')
data.sample(5)


# In[5]:


data.describe()


# # Предобработка

# In[314]:


answers = {'1':'723. Pirates of the Caribbean: On Stranger Tides (tt1298650)',
           '2':'1157. Gods and Generals (tt0279111)',
           '3':'768. Winnie the Pooh (tt1449283)',
           '4':'110',
           '5':'107',
           '6':'239. Avatar (tt0499549)',
           '7':'1245. The Lone Ranger (tt1210819)',
           '8':'1478',
           '9':'599. The Dark Knight (tt0468569)',
           '10':'1245. The Lone Ranger (tt1210819)',
           '11':'Drama',
           '12':'Drama',
           '13':'Peter Jackson',
           '14':'Robert Rodriguez',
           '15':'Chris Hemsworth',
           '16':'Matt Damon',
           '17':'Action',
           '18':'925. K-19: The Widowmaker (tt0267626)',
           '19':'2015',
           '20':'2014',
           '21':'Сентябрь',
           '22':'450',
           '23':'Peter Jackson',
           '24':'Four By Two Productions',
           '25':'Universal Pictures',
           '26':'Inside Out, The Dark Knight, 12 Years a Slave',
           '27':'Daniel Radcliffe, Rupert Grint'
          } 
           
           # создадим словарь для ответов
answers
# тут другие ваши предобработки колонок например:

#the time given in the dataset is in string format.
#So we need to change this in datetime format
# ...

# определяем функцию для новой колонки расчета выручки по каждому фильму
def profit(row):
    profits = row['revenue'] - row['budget']
    return profits

data1['profit'] = data.apply(profit, axis = 1)


# # 1. У какого фильма из списка самый большой бюджет?

# Использовать варианты ответов в коде решения запрещено.    
# Вы думаете и в жизни у вас будут варианты ответов?)

# In[24]:


# в словарь вставляем номер вопроса и ваш ответ на него
# Пример: 
answers['1'] = '2. Spider-Man 3 (tt0413300)'
# запишите свой вариант ответа
answers['1'] = '723. Pirates of the Caribbean: On Stranger Tides (tt1298650)'
# если ответили верно, можете добавить комментарий со значком "+"


# In[9]:


# тут пишем ваш код для решения данного вопроса:
answer1 = data[data['budget'] == data['budget'].max()]
answer1


# ВАРИАНТ 2

# In[ ]:


# можно добавлять разные варианты решения


# # 2. Какой из фильмов самый длительный (в минутах)?

# In[25]:


# думаю логику работы с этим словарем вы уже поняли, 
# по этому не буду больше его дублировать
answers['2'] = '1157. Gods and Generals (tt0279111)'


# In[31]:


answer2 = data[data['runtime'] == data['runtime'].max()]
answer2


# In[33]:


# еще один вариант ответа
answer = data[(data['imdb_id'] == 'tt0167260')|(data['imdb_id'] == 'tt0279111')|(data['imdb_id'] == 'tt0360717')
              |(data['imdb_id'] == 'tt0213149')|(data['imdb_id'] == 'tt0346491')]
answer2 = answer[answer['runtime'] == answer['runtime'].max()]
answer2


# # 3. Какой из фильмов самый короткий (в минутах)?
# 
# 
# 
# 

# In[32]:


answers['3'] = '768. Winnie the Pooh (tt1449283)'


# In[34]:


answer3 = data[data['runtime'] == data['runtime'].min()]
answer3


# # 4. Какова средняя длительность фильмов?
# 

# In[ ]:


answers['4'] = '110'


# In[35]:


answer4 = data['runtime'].mean()
answer4


# # 5. Каково медианное значение длительности фильмов? 

# In[ ]:


answers['5'] = '107'


# In[36]:


answer5 = data['runtime'].median()
answer5


# # 6. Какой самый прибыльный фильм?
# #### Внимание! Здесь и далее под «прибылью» или «убытками» понимается разность между сборами и бюджетом фильма. (прибыль = сборы - бюджет) в нашем датасете это будет (profit = revenue - budget) 

# In[ ]:


answers['6'] = '239. Avatar (tt0499549)'


# In[41]:


def profit(row):
    profits = row['revenue'] - row['budget']
    return profits

data1['profit'] = data.apply(profit, axis = 1)
answer6 = data1[data1['profit'] == data1['profit'].max()]
answer6


# # 7. Какой фильм самый убыточный? 

# In[ ]:


answers['7'] = '1245. The Lone Ranger (tt1210819)'


# In[42]:


answer7 = data1[data1['profit'] == data1['profit'].min()]
answer7


# # 8. У скольких фильмов из датасета объем сборов оказался выше бюджета?

# In[ ]:


answers['8'] = '1478'


# In[48]:


answer8 = data1[data1['profit'] > 0]
answer8


# # 9. Какой фильм оказался самым кассовым в 2008 году?

# In[ ]:


answers['9'] = '599. The Dark Knight (tt0468569)'


# In[55]:


release_year_2008 = data1[data1['release_year'] == 2008] # сначала создаем базу данных с выпуском фильмов 2008г.
answer9 = release_year_2008[release_year_2008['profit'] == release_year_2008['profit'].max()]
answer9


# # 10. Самый убыточный фильм за период с 2012 по 2014 г. (включительно)?
# 

# In[ ]:


answers['10'] = '1245. The Lone Ranger (tt1210819)'


# In[60]:


release_year_2012_2014 = data1[(data1['release_year'] >= 2012)&(data1['release_year'] <= 2014)]
answer10 = release_year_2012_2014[release_year_2012_2014['profit'] == release_year_2012_2014['profit'].min()]
answer10


# # 11. Какого жанра фильмов больше всего?

# In[ ]:


answers['11'] = 'Drama'
# эту задачу тоже можно решать разными подходами, попробуй реализовать разные варианты
# если будешь добавлять функцию - выноси ее в предобработку что в начале


# In[111]:


df2 = data.genres.str.split('|') # делаем series из столбца 'genres' 
df3 = df2.explode('genres') # применяем explode к столбцу 'genres', чтобы в каждой ячейке было по одному жанру
df3.value_counts() # выводим количество жанров


# ВАРИАНТ 2

# In[84]:


action = data[data.genres.str.contains("Action", na=False)]
action
adventure = data[data.genres.str.contains("Adventure", na=False)]
adventure
drama = data[data.genres.str.contains("Drama", na=False)]
drama
comedy = data[data.genres.str.contains("Comedy", na=False)]
comedy
thriller = data[data.genres.str.contains("Thriller", na=False)]
thriller


# # 12. Фильмы какого жанра чаще всего становятся прибыльными? 

# In[ ]:


answers['12'] = 'Drama'


# In[113]:


# выше я уже создал DataFrame data1 со столбцом profit 
profit_film = data1[data1.profit > 0]
df2 = profit_film.genres.str.split('|') # делаем series из столбца 'genres' 
df3 = df2.explode('genres') # применяем explode к столбцу 'genres', чтобы в каждой ячейке было по одному жанру
df3.value_counts() # выводим количество жанров


# # 13. У какого режиссера самые большие суммарные кассовые сборы?

# In[ ]:


answers['13'] = 'Peter Jackson'


# In[124]:


data.groupby('director').revenue.sum().sort_values(ascending=False)


# # 14. Какой режисер снял больше всего фильмов в стиле Action?

# In[ ]:


answers['14'] = 'Robert Rodriguez'


# In[138]:


data_action = data[data.genres.str.contains("Action", na=False)].copy() # выделяем фильмы в жанре Action
data_action.director = data_action.director.str.split('|') 
data_action = data_action.explode('director') # разбиваем колонку режиссеров, если у фильма их несколько
data_action.groupby(['director']).director.count().sort_values(ascending=False) # определяем режиссера, 
                    # снявшего больше всего фильмов в жанре Action


# # 15. Фильмы с каким актером принесли самые высокие кассовые сборы в 2012 году? 

# In[ ]:


answers['15'] = 'Chris Hemsworth'


# In[164]:


data_2012 = data[data['release_year'] == 2012].copy() # формируем базу данных фильмов 2012 года выпуска
data_2012.cast = data_2012.cast.str.split('|')
data_actors = data_2012.explode('cast') # разбиваем колонку актеров
data_actors.groupby(['cast']).revenue.sum().sort_values(ascending=False) # определяем актера, фильмы с которым 
                     # принесли самые высокие кассовые сборы


# # 16. Какой актер снялся в большем количестве высокобюджетных фильмов?

# In[ ]:


answers['16'] = 'Matt Damon'


# In[167]:


data_high_budget = data[data['budget'] >= data['budget'].mean()].copy() # формируем базу высокобюджетных фильмов
data_high_budget.cast = data_high_budget.cast.str.split('|')
data_actors = data_high_budget.explode('cast') # разбиваем колонку актеров
data_actors.groupby(['cast']).cast.count().sort_values(ascending=False).sort_values(ascending=False) # определяем  
                   # актера, снявшегося в большем количестве высокобюджетных фильмов


# # 17. В фильмах какого жанра больше всего снимался Nicolas Cage? 

# In[ ]:


answers['17'] = 'Action'


# In[247]:


data_Nicolas_Cage = data[data.cast.str.contains("Nicolas Cage", na=False)].copy() # формируем базу актёра
df2 = data_Nicolas_Cage.genres.str.split('|') # делаем series из столбца 'genres' 
df3 = df2.explode('genres') # применяем explode к столбцу 'genres', чтобы в каждой ячейке было по одному жанру
df3.value_counts() # выводим количество жанров


# # 18. Самый убыточный фильм от Paramount Pictures

# In[ ]:


answers['18'] = '925. K-19: The Widowmaker (tt0267626)'


# In[176]:


# выше я уже создал DataFrame data1 со столбцом profit 
data_Paramount = data1[data1.production_companies.str.contains("Paramount Pictures", na=False)].copy() 
              # формируем базу фильмов производства Paramount Pictures
data_Paramount_min = data_Paramount[data_Paramount.profit == data_Paramount.profit.min()] 
data_Paramount_min


# # 19. Какой год стал самым успешным по суммарным кассовым сборам?

# In[ ]:


answers['19'] = '2015'


# In[178]:


data.groupby(['release_year']).revenue.sum().sort_values(ascending=False)


# # 20. Какой самый прибыльный год для студии Warner Bros?

# In[ ]:


answers['20'] = '2014'


# In[181]:


# выше я уже создал DataFrame data1 со столбцом profit 
data_Warner = data1[data1.production_companies.str.contains("Warner Bros", na=False)].copy() 
              # формируем базу фильмов производства Warner Bros
data_Warner.groupby(['release_year']).profit.sum().sort_values(ascending=False)


# # 21. В каком месяце за все годы суммарно вышло больше всего фильмов?

# In[ ]:


answers['21'] = 'Сентябрь'


# In[184]:


data['month'] = pd.to_datetime(data.release_date).dt.month #преобразуем дату в год-месяц-число
data['month'].value_counts()


# # 22. Сколько суммарно вышло фильмов летом? (за июнь, июль, август)

# In[ ]:


answers['22'] = '450'


# In[189]:


data['month'] = pd.to_datetime(data.release_date).dt.month #преобразуем дату в год-месяц-число
data_summer = data[(data['month'] == 6) | (data['month'] == 7) | (data['month'] == 8)] # создаем базу летних фильмов
data_summer['month'].count()


# # 23. Для какого режиссера зима – самое продуктивное время года? 

# In[ ]:


answers['23'] = 'Peter Jackson'


# In[194]:


data['month'] = pd.to_datetime(data.release_date).dt.month #преобразуем дату в год-месяц-число
data_winter = data[(data['month'] == 12) | (data['month'] == 1) | (data['month'] == 2)].copy() 
                    # создаем базу зимних фильмов
data_winter.director = data_winter.director.str.split('|')
data_winter_directors = data_winter.explode('director') # разбиваем колонку режиссеров
data_winter_directors.groupby(['director']).cast.count().sort_values(ascending=False) # определяем  
                   # режиссера, выпустившего зимой наибольшее количество фильмов


# # 24. Какая студия дает самые длинные названия своим фильмам по количеству символов?

# In[ ]:


answers['24'] = 'Four By Two Productions'


# In[285]:


data = pd.read_csv('movie_bd_v5.csv')
data.production_companies = data.production_companies.str.split('|')
data_companies = data.explode('production_companies') # разбиваем колонку компаний
data_companies['length'] = data_companies['original_title'].str.len() # дополняем базу колонкой с количеством 
               # символов в названиях фильмов
data_companies.groupby(['production_companies']).length.mean().sort_values(ascending=False) # определяем  
                   # студию с самыми длинными названиями фильмов, исходя из среднего количества символов


# # 25. Описание фильмов какой студии в среднем самые длинные по количеству слов?

# In[ ]:


answers['25'] = 'Universal Pictures'


# In[313]:


from collections import Counter
import itertools as it
from itertools import combinations

data = pd.read_csv('movie_bd_v5.csv')
data.production_companies = data.production_companies.str.split('|')
data_companies = data.explode('production_companies') # разбиваем колонку компаний

data_companies['overview'] = data_companies['overview'].str.split(' ') # разбиваем колонку на отдельные слова 

data_companies.groupby(['production_companies']).overview.count().sort_values(ascending=False).head(20) # определяем  
                   # студию с наибольшим количеством слов в описании фильмов


# # 26. Какие фильмы входят в 1 процент лучших по рейтингу? 
# по vote_average

# In[ ]:


answers['26'] = 'Inside Out, The Dark Knight, 12 Years a Slave'


# In[307]:


data['vote_average'].quantile([.99]) # сначала определим, какой рейтинг входит в 1 процент самых высоких оценок
                          # эта оценка составляет не менее 7.8
data_best_films = data[data.vote_average >= 7.8] # для удобства создадим базу данных лучших фильмов
data_best_films.groupby(['original_title']).vote_average.sum().sort_values(ascending=False) 
            # смотрим рейтинг лучших фильмов


# # 27. Какие актеры чаще всего снимаются в одном фильме вместе?
# 

# In[ ]:


answers['27'] = 'Daniel Radcliffe, Rupert Grint'


# In[296]:


from collections import Counter
import itertools as it
from itertools import combinations

data = pd.read_csv('movie_bd_v5.csv')
data_cast = data.copy()  
data_cast['cast'] = data_cast['cast'].str.split('|') # разбиваем колонку актеров на отдельные имена 
data_cast['cast'] = data_cast['cast'].apply(lambda x: tuple(it.combinations(sorted(x),2))) # ищем повторяющиеся 
            # сочетания двух актеров  
data_cast['cast'].explode().value_counts() # 


# ВАРИАНТ 2

# # Submission

# In[315]:


# в конце можно посмотреть свои ответы к каждому вопросу
answers


# In[316]:


# и убедиться что ни чего не пропустил)
len(answers)


# In[ ]:





# In[ ]:




