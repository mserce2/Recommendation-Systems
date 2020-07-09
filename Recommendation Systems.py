# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 21:39:37 2020

@author: Mete
"""

import pandas as pd
import numpy as np

movie=pd.read_csv("movie.csv")
print(movie.columns)
movie=movie.loc[:,["movieId","title"]]
print(movie.head(10))
print("*"*50)
#%%import raiting dat and look at columsn
rating=pd.read_csv("rating.csv")
print(rating.columns)
print(rating.head(10))
print("*"*30)

#what we need is that user id, movie id, and rating(siz farklı birşey analiz etmek istiyorsanız istediğiniz sütünları alabilirsiniz)
rating=rating.loc[:,["userId","movieId","rating"]]
#then merge movie and rating data
data=pd.merge(movie,rating)
print(data.head(10))
#data uzunluğu
print(data.shape) #20 milyon data çıkacak ve bilgisayarı aşırı zorlayacağı için şimdilik ilk 1 milyon data alalım
data=data.iloc[:1000000,:]

#%%lets make a pivot table in order to make rows are users and columns are movies.And values are rating
#satır ve sütünları kendimize göre ayarladıktan sonra benzer olan filmler arasında ilişki kurup tavsiye vermesi açısından karşılaştırma yacapacağız

pivot_table=data.pivot_table(index=["userId"],columns=["title"],values="rating")
print(pivot_table.head(10))

#örnek olarak bad boy filimini ele alalım.Bad boy filmini izleyenlere tavsiye olarak hangi filmi önereceğimize bakalım
movie_watched=pivot_table["Bad Boys (1995)"]
similarity_with_other_movies=pivot_table.corrwith(movie_watched) #bad boy filmini diğer tüm film sütünları ile karşılaştırıp izlenme bezerliği arıyoruz
similarity_with_other_movies=similarity_with_other_movies.sort_values(ascending=False) #en büyük benzerlikten en düşük benzerliğe göre tavsiye et
print(similarity_with_other_movies.head)








