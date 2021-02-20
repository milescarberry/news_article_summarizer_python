import tkinter as tk                      # for developing guis (This module is part of the "core" python stack)


import nltk

nltk.download('punkt')            # Download the 'punkt' module of the "nltk" library.


from textblob import TextBlob


from newspaper import Article




def summarize():





    url = article_url.get("1.0", "end").strip()



    def create_article(address):



        return Article(address)




    article = create_article(url)


    # "article" is a newspaper.newspaper.Article object (article is an instance of the Article class)


    # The Article object "article" is "focused" on the url. (Is pointing towards the "url")




    article.download()             # Download the article data. (Earlier the Article object was just pointing towards the "url")



    article.parse()               # "Interpret" the downloaded data. (Extract some "meaning" (useful data) from the downloaded data)




    article.nlp()                 # I am calling the nlp() method on our Article object.




    title.config(state = "normal")

    author.config(state = "normal")

    publication_date.config(state = "normal")

    summary.config(state = "normal")

    sentiment.config(state = "normal")


    title.delete("1.0", "end")

    title.insert("1.0", article.title)

    author.delete("1.0", "end")

    author.insert("1.0", article.authors)

    publication_date.delete("1.0", "end")

    publication_date.insert("1.0", article.publish_date)

    summary.delete("1.0", "end")

    summary.insert("1.0", article.summary)


    analysis = TextBlob(article.text)


    sentiment.delete("1.0", "end")


    sentiment.insert("1.0", f'Polarity: {analysis.polarity}, Sentiment: {"Positive" if analysis.polarity > 7.0 else "Negative" if analysis.polarity <= 7.0 else "Neutral"}')



    title.config(state = "disabled")

    author.config(state = "disabled")

    publication_date.config(state = "disabled")

    summary.config(state = "disabled")

    sentiment.config(state = "disabled")




    print()

    print(len(article.authors))

    print()

    print(article.publish_date)


# GUI Part :-



# Let's create a tkinter object named "root":-



root = tk.Tk()                            # Therefore, "root" is an instance of the tk.Tk class.



root.title("News Summarizer")


root.geometry("1200x720")                        # pass in the pixel height and width as parameters (in the form of a string)





tlabel = tk.Label(root, text = "\nTitle")                           # "tlabel" variable stands for "title label"


tlabel.pack()


title = tk.Text(root, height = 1, width = 140)

title.config(state = "disabled", bg = "#dddddd")                     # The title bar cannot take an input from the user (state = "disabled")


title.pack()






alabel = tk.Label(root, text = "\nAuthor")                           # "tlabel" variable stands for "title label"


alabel.pack()


author = tk.Text(root, height = 1, width = 140)

author.config(state = "disabled", bg = "#dddddd")                     # The title bar cannot take an input from the user (state = "disabled")


author.pack()







plabel = tk.Label(root, text = "\nPublication Date")                           # "tlabel" variable stands for "title label"


plabel.pack()


publication_date = tk.Text(root, height = 1, width = 140)

publication_date.config(state = "disabled", bg = "#dddddd")                     # The title bar cannot take an input from the user (state = "disabled")


publication_date.pack()





slabel = tk.Label(root, text = "\nArticle Summary")                           # "tlabel" variable stands for "title label"


slabel.pack()


summary = tk.Text(root, height = 15, width = 140)

summary.config(state = "disabled", bg = "#dddddd")                     # The title bar cannot take an input from the user (state = "disabled")




summary.pack()               # Integrate the tk.Text object named "summary" into the "root" window.







selabel = tk.Label(root, text = "\nSentiment Analysis")                           # "tlabel" variable stands for "title label"


selabel.pack()


sentiment = tk.Text(root, height = 1, width = 140)

sentiment.config(state = "disabled", bg = "#dddddd")                     # The title bar cannot take an input from the user (state = "disabled")




sentiment.pack()               # Integrate the tk.Tk object named "sentiment" into the tk window named "root".






urllabel = tk.Label(root, text = "\n\nArticle URL")                           # "tlabel" variable stands for "title label"


urllabel.pack()




article_url = tk.Text(root, height = 1, width = 140)

article_url.config(bg = "#ffffff")                     # The title bar cannot take an input from the user (state = "disabled")




article_url.pack()




blabel = tk.Label(root, text = "\n")

blabel.pack()



btn = tk.Button(root, text = "Summarize Article", command = summarize)


btn.pack()













root.mainloop()                    # Call the mainloop() method on "Tk" object root.        (Execute the tkinter window. (The object "root" belonging to the tk.Tk class))
