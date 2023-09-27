# MovieRecommenderSystem
I made this project by using google colab notebook and using PyCharm. i made this whole project by taking some guidance from online plateform.
The 'movies_2.csv' table is made by me, it is a merge of two original movies and credits file. It has total 3 columns : 'movie_id';'title';'tags', Where 'movie_id' and 'title' are default there are no changes in those columns but 'tags' column is a merge of colums of overview, some actor/actress name and director name of that particular movie.
Now, using CountVectorizer() in the 'tags' column and then using cosine_similarity() in it.
Now, sorting the cosine_similarity() data in descending order (as given in a google colab notebook code).
Then I define recommend function which gives an output of top 5 similiar movies to the input movie that you have entered.
After checking the code if its working or not. 
Open PyCharm and make a new project. Then export the 'movies_2.csv' table and uses pickle to import cosine_simililarity() data (that we did earlier).
Now, as from code file. We write the code on PyCharm.
Write 'streamlit run name.py' in the PyCharm Terminal to run the code in your browser.
Hence, our movie recommender system is completed.
