import tkinter                       # for developing guis (This module is part of the "core" python stack)


import nltk


from textblob import TextBlob


from newspaper import Article


url = "https://scroll.in/article/987415/rising-petrol-prices-shrinking-savings-don-t-matter-indias-middle-class-is-mesmerised-by-modi"


article = Article(url)


# "article" is a newspaper.newspaper.Article object (article is an instance of the Article class)


# The Article object "article" is "focused" on the url. (Is pointing towards the "url")




article.download()             # Download the article data. (Earlier the Article object was just pointing towards the "url")



article.parse()               # "Interpret" the downloaded data. (Extract some "meaning" (useful data) from the downloaded data)




article.nlp()                 # I am calling the nlp() method on our Article object.





print(f"Article Title : {article.title}")                       # I am using the "formatted string literal" here.


print(f"Authors : {article.authors}")



print(f"Publication Date : {article.publish_date}")


print()

print("f Summary : {article.summary}")

print()



# The "newspaper" library does "everything" for us.
