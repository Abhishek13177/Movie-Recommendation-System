from flask import Flask,request, render_template
import pickle
import requests

movies=pickle.load(open('model/movies_list.pkl','rb'))
similarity=pickle.load(open('model/similarity.pkl','rb'))

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url).json()

    try:
        poster_path = data['poster_path']
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        return full_path
    except KeyError:
        # Handle the case where 'poster_path' key is not present in the response
        return None  # Or return a default poster path or an indication that the poster is not available


def recommend(movie):
       try:
              index = movies[movies['title'] == movie].index[0]
       except IndexError:
              # Handle the case where the index is out of bounds
              return [], []

       distances = sorted(list(enumerate(similarity[index])), reverse= True , key= lambda x:x[1])
       recommended_movies_name = []
       recommended_movies_poster = []
       for i in distances[1:6]:
              movie_id = movies.iloc[i[0]].movie_id
              recommended_movies_poster.append(fetch_poster(movie_id))
              recommended_movies_name.append(movies.iloc[i[0]].title)

       return recommended_movies_name,recommended_movies_poster      

app = Flask(__name__)

@app.route('/')
def home():
         return render_template("index.html")  

@app.route('/about')
def about():
         return render_template("about.html")  

@app.route('/recommendation', methods = ['GET','POST'])
def recommendation():
       movies_list = movies['title'].values
       status = False
       
       if request.method == 'POST':
              try:   
                     if request.form:
                       movies_name=request.form['movies']
                       print(movies_name)
                       recommended_movies_name, recommended_movies_poster = recommend(movies_name)
                       print(recommended_movies_name)
                       print(recommended_movies_poster)
                       status = True
                       return render_template("prediction.html", movies_name = recommended_movies_name, poster = recommended_movies_poster, movies_list= movies_list, status=status)


              except Exception as e:
                    error = {'error': e}
                    return render_template("prediction.html",error = error, movies_list= movies_list, status=status)
       
       else:
            return render_template("prediction.html",movies_list= movies_list, status=status)  




if __name__ == '__main__':
    app.debug = True
    app.run()    