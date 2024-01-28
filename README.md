##This project uses content based filtering , we fetch movies from dataset and it also uses TMDB API to fetch poster of those movies.

This project showcases a content-based movie recommendation system, leveraging natural language processing and machine learning techniques. The system offers personalized movie suggestions based on various factors such as movie descriptions, genres, keywords, cast, and crew.

In the initial stages, the project involved collecting and preprocessing data from two datasets (tmdb_5000_movies.csv and tmdb_5000_credits.csv). The data was merged, missing values were handled, and JSON columns were transformed for better analysis.

Text processing played a crucial role in the project, involving tokenization, cleaning, and stemming of textual data in movie descriptions, genres, keywords, cast, and crew. The extracted information was then consolidated into a new feature called 'tags'.

Feature engineering utilized the CountVectorizer technique to convert processed text into numerical vectors. These vectors were used to calculate cosine similarity between movies, forming the basis for recommendations.

For practical use, the project includes a python file (movie_recommendation.py) for model training. After training, the model can be deployed on a website to provide users with movie recommendations. The necessary files for deployment are model/movie_list.pkl (processed movie data) and model/similarity.pkl (cosine similarity matrix).

The project's dependencies include standard Python libraries such as pandas, nltk, and scikit-learn,flask, which can be installed using pip install pandas nltk scikit-learn flask.
