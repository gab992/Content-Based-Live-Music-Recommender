# Content-Based-Live-Music-Recommender
I used audio features extracted from mp3s and from Spotify's API to recommend a playlist of songs by artists with upcoming shows in a given city. There are two ways to run this recommender, but both require credentials for API and Songkick APIs.

**Method 1: recommender**  
To use the already trained models, the recommender can be used by running 'get_location_data.ipynb' for whatever cities the user wants and then running 'Recommender.ipynb'.  

**Method 2: re-training models and running recommender**  
The models can be retrained by running 'get_train_data.ipynb' and then running 'PCA_and_clustering.ipynb'. Then the recommender can be run by following the Method 1 instructions.

# Data  
Unfortunately, due to API use conditions I cannot post the data for this project.
I instead provide code for obtaining all the necessary data that can be run by a user with
the following credentials...  
- Songkick API Key  
- Spotify API Client ID  
- Spotify API Client Secret  
These credentials can be requested from [Spotify](https://developer.spotify.com/documentation/general/guides/authorization-guide/) and [Songkick](https://www.songkick.com/api_key_requests/new).  

Code for getting the necessary data is in the following jupyter notebooks...  
- **get_train_data.ipynb**: scrapes pitchforks list of the top 200 albums of the 2010s for
all artists on the list. Gets each artists top tracks from the Spotify API as well as pre-defined
Spotify audio features for each track. It then uses YoutubeDL to scrape mp3s for each track
from Youtube and uses the LibROSA python library to extract additional audio features for each track.
The results are saved to the csv file "pitchfork_data.csv"  
- **get_location_data.ipynb**: uses the Songkick API to get a list of artists with
upcoming concerts in a given list of cities. For each city, a dataset is created using the same
procedure as for the pitchfork artists although only their top 5 tracks are considered.
The notebook saves a csv file called "{city}_data.csv" for each city in the in the cities list that is given by the user.  

# Model  
The necessary models are pickled from their initial training in the following files...  
- **pca_mfcc_2.pickle**: contains the PCA used to reduce the dimentionality of the 24 MFCC features  
- **km_mfccs.pickle**: contains the k-means clustering as applied to the MFCC PCA components  
The following jupyter notebook contains the code used to train the models...  
- **PC_and_clustering.ipynb**: contains some minor data cleaning and the code used for training
the PCA and k-means. This notebook contains a number of necessary pickled objects for the recommender to run.  

# Recommender  
- **Recommender.ipynb**: runs the simple recommender (just matching on euclidean distance calculated
with Spotify features) and the full recommender (using PCA MFCC clustering before matching on euclidean
distance calculated with Spotify features)  

# Supplementary Code  
- **functions.py**: contains functions for all data acquisition notebooks as well as the recommender notebook.  
- **model_functions.py**: contains functions for the PCA_and_clustering notebook.
