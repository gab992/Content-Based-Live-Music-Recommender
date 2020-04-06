from __future__ import unicode_literals
import spotipy
import pandas as pd
import numpy as np
from spotipy.oauth2 import SpotifyClientCredentials

from sklearn.preprocessing import StandardScaler
from scipy.spatial.distance import euclidean

from bs4 import BeautifulSoup
import requests
import time, os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import re
import pickle
from collections import defaultdict

chromedriver = "/Applications/chromedriver" # path to the chromedriver executable
os.environ["webdriver.chrome.driver"] = chromedriver

import youtube_dl
import os
import shutil

import librosa
import matplotlib.pyplot as plt
import librosa
from IPython.display import Audio
from librosa import display

from spotipy.oauth2 import SpotifyClientCredentials
from selenium.common.exceptions import NoSuchElementException

# These functions are for data retrieval
def get_pitchfork_artists():
    '''Returns the list of artists in the pitchfork list of top 200 albums of the 2010s'''
    driver = webdriver.Chrome(chromedriver)
    driver.get('https://pitchfork.com/features/lists-and-guides/the-200-best-albums-of-the-2010s/')

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    albums_html = soup.find_all('h2')
    artists = []
    for album_h in albums_html:
        al = album_h.prettify().splitlines()
        artist = al[1].strip()
        artist = artist[:len(artist)-1]
        artists.append(artist)
    driver.close()

    # Cleaning results as they were cleaned for initial model training
    artists = artists[:-3]
    artists.remove('JAY-Z / Kanye West')
    artists.remove('Various Artists')
    artists.remove('21 Savage / Metro Boomin')
    artists.remove('D’Angelo &amp; the Vanguard')
    artists.remove('Jean Grae / Quelle Chris')
    artists.remove('Various Artists')
    artists.remove('Girls')
    artists.append('JAY-Z')
    artists.append('21 Savage')
    artists.append('Metro Boomin')
    artists.append('D’Angelo')
    artists.append('Jean Grae')
    return artists

def get_tracks_and_pop_pitchfork(artist, cid, secret):
    '''Returns a list of an artists top 10 songs from spotify'''
    from spotipy.oauth2 import SpotifyClientCredentials

    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

    tracks = []
    pop = []
    dance = []
    energy = []
    key = []
    loudness = []
    mode = []
    speech = []
    acoustic = []
    instrumental = []
    liveness = []
    valence = []
    tempo_spot = []
    duration_ms = []
    time_sig = []
    analysis_url = []
    artist = sp.search(q=artist, type='artist', limit=1)['artists']['items'][0]
    artist_id = artist['id']
    genres = artist['genres']
    top_tracks = sp.artist_top_tracks(artist_id)['tracks']
    for track in top_tracks[0:10]:
        tracks.append(track['name'])
        pop.append(track['popularity'])
        audio = sp.audio_features(track['id'])[0]
        dance.append(audio['danceability'])
        energy.append(audio['energy'])
        key.append(audio['key'])
        loudness.append(audio['loudness'])
        mode.append(audio['mode'])
        speech.append(audio['speechiness'])
        acoustic.append(audio['acousticness'])
        instrumental.append(audio['instrumentalness'])
        liveness.append(audio['liveness'])
        valence.append(audio['valence'])
        tempo_spot.append(audio['tempo'])
        duration_ms.append(audio['duration_ms'])
        time_sig.append(audio['time_signature'])
        analysis_url.append(audio['analysis_url'])
    return genres, tracks, pop, dance, energy, key, loudness, mode, speech, acoustic, instrumental, liveness, valence, tempo_spot, duration_ms, time_sig, analysis_url


def get_tracks_and_pop_songkick(artist, cid, secret):
    '''Returns a list of an artists top 10 songs from spotify'''
    from spotipy.oauth2 import SpotifyClientCredentials

    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

    tracks = []
    pop = []
    dance = []
    energy = []
    key = []
    loudness = []
    mode = []
    speech = []
    acoustic = []
    instrumental = []
    liveness = []
    valence = []
    tempo_spot = []
    duration_ms = []
    time_sig = []
    analysis_url = []
    artist = sp.search(q=artist, type='artist', limit=1)['artists']['items'][0]
    artist_id = artist['id']
    genres = artist['genres']
    top_tracks = sp.artist_top_tracks(artist_id)['tracks']
    for track in top_tracks[0:5]:
        tracks.append(track['name'])
        pop.append(track['popularity'])
        audio = sp.audio_features(track['id'])[0]
        dance.append(audio['danceability'])
        energy.append(audio['energy'])
        key.append(audio['key'])
        loudness.append(audio['loudness'])
        mode.append(audio['mode'])
        speech.append(audio['speechiness'])
        acoustic.append(audio['acousticness'])
        instrumental.append(audio['instrumentalness'])
        liveness.append(audio['liveness'])
        valence.append(audio['valence'])
        tempo_spot.append(audio['tempo'])
        duration_ms.append(audio['duration_ms'])
        time_sig.append(audio['time_signature'])
        analysis_url.append(audio['analysis_url'])
    return genres, tracks, pop, dance, energy, key, loudness, mode, speech, acoustic, instrumental, liveness, valence, tempo_spot, duration_ms, time_sig, analysis_url

def get_tracks_and_pop_user(artist, cid, secret):
    '''Returns a list of an artists top 10 songs from spotify'''
    from spotipy.oauth2 import SpotifyClientCredentials

    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

    tracks = []
    pop = []
    dance = []
    energy = []
    key = []
    loudness = []
    mode = []
    speech = []
    acoustic = []
    instrumental = []
    liveness = []
    valence = []
    tempo_spot = []
    duration_ms = []
    time_sig = []
    analysis_url = []
    artist = sp.search(q=artist, type='artist', limit=1)['artists']['items'][0]
    artist_id = artist['id']
    genres = artist['genres']
    top_tracks = sp.artist_top_tracks(artist_id)['tracks']
    for track in top_tracks[0:3]:
        tracks.append(track['name'])
        pop.append(track['popularity'])
        audio = sp.audio_features(track['id'])[0]
        dance.append(audio['danceability'])
        energy.append(audio['energy'])
        key.append(audio['key'])
        loudness.append(audio['loudness'])
        mode.append(audio['mode'])
        speech.append(audio['speechiness'])
        acoustic.append(audio['acousticness'])
        instrumental.append(audio['instrumentalness'])
        liveness.append(audio['liveness'])
        valence.append(audio['valence'])
        tempo_spot.append(audio['tempo'])
        duration_ms.append(audio['duration_ms'])
        time_sig.append(audio['time_signature'])
        analysis_url.append(audio['analysis_url'])
    return genres, tracks, pop, dance, energy, key, loudness, mode, speech, acoustic, instrumental, liveness, valence, tempo_spot, duration_ms, time_sig, analysis_url

def get_urls(tracks, artist):
    '''returns a list of urls for youtube videos if sogs indicated by each corresponding
    index in the song_list and artist_list'''
    url_list=[]
    driver = webdriver.Chrome(chromedriver)
    time.sleep(5)
    for track in tracks:
        try:
            driver.get('https://www.youtube.com/')
            time.sleep(3)
            search = driver.find_element_by_xpath("//input[@id='search']").send_keys(track + ' ' + artist, Keys.ENTER)
            time.sleep(3)
            video = driver.find_element_by_xpath("//ytd-video-renderer[@class='style-scope ytd-item-section-renderer']").click()
            url_list.append(driver.current_url)
        except NoSuchElementException:
            url_list.append('failed')
    driver.close()
    return url_list

def get_audio(url):
    '''Usere youtube_dl to extract the audio from a youtube video as an mp3'''
    ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'quiet': False
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def extract_features(mp3):
    '''Extracts librosa audio features from 0:45 to 1:15 of an mp3 file'''
    y, sr = librosa.load(mp3, offset=45, duration=30);
    y_harmonic, y_percussive = librosa.effects.hpss(y)
    tempo, beat_frames = librosa.beat.beat_track(y_percussive, sr=sr)
    zcr = librosa.feature.zero_crossing_rate(y)
    mfccs = librosa.feature.mfcc(y, sr=sr)
    spectral_contrast = librosa.feature.spectral_contrast(y, sr=sr)
    chroma = librosa.feature.chroma_cqt(y_harmonic, sr=sr)
    tonnetz = librosa.feature.tonnetz(y, sr=sr)
    spectral_flatness = librosa.feature.spectral_flatness(y)
    rms = librosa.feature.rms(y)
    spectral_centroid = librosa.feature.spectral_centroid(y)
    spectral_bandwidth = librosa.feature.spectral_bandwidth(y)

    features = {'tempo':tempo,'zcr':zcr,'mfccs':mfccs,'spectral_contrast':spectral_contrast,'chroma':chroma, \
                'tonnetz':tonnetz,'spectral_flatness':spectral_flatness,'rms':rms,'spectral_centroid':spectral_centroid, \
                'spectral_bandwidth':spectral_bandwidth}
    return features

def get_data_pitchfork(artists, cid, secret):
    '''Executes full data extraction pipeline for a list of artists in the pitchfork top albums of the 2010s list'''
    df = pd.DataFrame(columns=['Artist','Track'])
    searched_artists = []
    for artist in artists:
        if artist not in searched_artists:
            try:
                genres, tracks, pop, dance, energy, key, loudness, mode, speech, acoustic, instrumental, liveness, valence, tempo_spot, duration_ms, time_sig, analysis_url = get_tracks_and_pop_pitchfork(artist, cid, secret)
                urls = get_urls(tracks, artist)
                print(tracks)
                for i, track in enumerate(tracks):
                    df = df.append({'Artist':artist,'Track':track,'Genres':genres, 'Popularity':pop[i], 'Dance':dance[i], \
                                    'Energy':energy[i], 'Key':key[i], 'Loudness':loudness[i], 'Mode':mode[i], \
                                    'Speech':speech[i], 'Acoustic':acoustic[i], 'Instrumental':instrumental[i], \
                                    'Liveness':liveness[i], 'Valence':valence[i], 'Tempo_Spot':tempo_spot[i], \
                                    'Duration_ms':duration_ms[i], 'Time_Sig':time_sig[i], 'Analysis_URL':analysis_url[i]}, ignore_index=True)
                    for file in os.listdir():
                        if file.endswith(".mp3") or file.endswith(".webm"):
                            os.remove(file)
                    if urls[i] != 'failed':
                        try:
                            get_audio(urls[i]);
                        except:
                            print('Audio extraction failed')
                    for file in os.listdir():
                        if file.endswith(".mp3"):
                            feat = extract_features(file)
                            df.loc[(df.Track==tracks[i]), 'tempo'] = feat['tempo']
                            df.loc[(df.Track==tracks[i]), 'zcr'] = np.mean(feat['zcr'])
                            df.loc[(df.Track==tracks[i]), 'rms'] = np.mean(feat['rms'])
                            df.loc[(df.Track==tracks[i]), 'spec_flat'] = np.mean(feat['spectral_flatness'])
                            df.loc[(df.Track==tracks[i]), 'zcr'] = np.mean(feat['zcr'])
                            df.loc[(df.Track==tracks[i]), 'spec_cent'] = np.mean(feat['spectral_centroid'])
                            df.loc[(df.Track==tracks[i]), 'spec_band'] = np.mean(feat['spectral_bandwidth'])
                            for j, e in enumerate(feat['mfccs']):
                                df.loc[(df.Track==tracks[i]), f'mfcc{j+1}'] = np.mean(e)
                                df.loc[(df.Track==tracks[i]), f'mfcc{j+1}_var'] = np.var(e)
                            for j, e in enumerate(feat['spectral_contrast']):
                                df.loc[(df.Track==tracks[i]), f'spec_cont{j+1}'] = np.mean(e)
                            for j, e in enumerate(feat['chroma']):
                                df.loc[(df.Track==tracks[i]), f'chroma{j+1}'] = np.mean(e)
                            for j, e in enumerate(feat['tonnetz']):
                                df.loc[(df.Track==tracks[i]), f'tonnetz{j+1}'] = np.mean(e)
                            shutil.move(file, '/Volumes/Samsung_T5/proj_5_songkick/'+artist.replace('/','')+'-'+tracks[i].replace('/','')+'.mp3')
                searched_artists.append(artist)
            except:
                pass
    return df

def get_data_user(artists, cid, secret):
    '''Executes for data extraction pipeline for a user's list of artists'''
    df = pd.DataFrame(columns=['Artist','Track'])
    searched_artists = []
    for artist in artists:
        if artist not in searched_artists:
            try:
                genres, tracks, pop, dance, energy, key, loudness, mode, speech, acoustic, instrumental, liveness, valence, tempo_spot, duration_ms, time_sig, analysis_url = get_tracks_and_pop_user(artist, cid, secret)
                urls = get_urls(tracks, artist)
                print(tracks)
                for i, track in enumerate(tracks):
                    df = df.append({'Artist':artist,'Track':track,'Genres':genres, 'Popularity':pop[i], 'Dance':dance[i], \
                                    'Energy':energy[i], 'Key':key[i], 'Loudness':loudness[i], 'Mode':mode[i], \
                                    'Speech':speech[i], 'Acoustic':acoustic[i], 'Instrumental':instrumental[i], \
                                    'Liveness':liveness[i], 'Valence':valence[i], 'Tempo_Spot':tempo_spot[i], \
                                    'Duration_ms':duration_ms[i], 'Time_Sig':time_sig[i], 'Analysis_URL':analysis_url[i]}, ignore_index=True)
                    for file in os.listdir():
                        if file.endswith(".mp3") or file.endswith(".webm"):
                            os.remove(file)
                    if urls[i] != 'failed':
                        try:
                            get_audio(urls[i]);
                        except:
                            print('Audio extraction failed')
                    for file in os.listdir():
                        if file.endswith(".mp3"):
                            feat = extract_features(file)
                            df.loc[(df.Track==tracks[i]), 'tempo'] = feat['tempo']
                            df.loc[(df.Track==tracks[i]), 'zcr'] = np.mean(feat['zcr'])
                            df.loc[(df.Track==tracks[i]), 'rms'] = np.mean(feat['rms'])
                            df.loc[(df.Track==tracks[i]), 'spec_flat'] = np.mean(feat['spectral_flatness'])
                            df.loc[(df.Track==tracks[i]), 'zcr'] = np.mean(feat['zcr'])
                            df.loc[(df.Track==tracks[i]), 'spec_cent'] = np.mean(feat['spectral_centroid'])
                            df.loc[(df.Track==tracks[i]), 'spec_band'] = np.mean(feat['spectral_bandwidth'])
                            for j, e in enumerate(feat['mfccs']):
                                df.loc[(df.Track==tracks[i]), f'mfcc{j+1}'] = np.mean(e)
                                df.loc[(df.Track==tracks[i]), f'mfcc{j+1}_var'] = np.var(e)
                            for j, e in enumerate(feat['spectral_contrast']):
                                df.loc[(df.Track==tracks[i]), f'spec_cont{j+1}'] = np.mean(e)
                            for j, e in enumerate(feat['chroma']):
                                df.loc[(df.Track==tracks[i]), f'chroma{j+1}'] = np.mean(e)
                            for j, e in enumerate(feat['tonnetz']):
                                df.loc[(df.Track==tracks[i]), f'tonnetz{j+1}'] = np.mean(e)
                            shutil.move(file, '/Volumes/Samsung_T5/proj_5_data_2/'+artist.replace('/','')+'-'+tracks[i].replace('/','')+'.mp3')
                searched_artists.append(artist)
            except:
                pass
    return df

def get_data_songkick(artists, cid, secret):
    '''Executes full data extraction pipeline for a list of artists with upcoming shows in a specific location'''
    df = pd.DataFrame(columns=['Artist','Track'])
    searched_artists = []
    for artist in artists:
        if artist not in searched_artists:
            try:
                genres, tracks, pop, dance, energy, key, loudness, mode, speech, acoustic, instrumental, liveness, valence, tempo_spot, duration_ms, time_sig, analysis_url = get_tracks_and_pop_songkick(artist, cid, secret)
                urls = get_urls(tracks, artist)
                print(tracks)
                for i, track in enumerate(tracks):
                    df = df.append({'Artist':artist,'Track':track,'Genres':genres, 'Popularity':pop[i], 'Dance':dance[i], \
                                    'Energy':energy[i], 'Key':key[i], 'Loudness':loudness[i], 'Mode':mode[i], \
                                    'Speech':speech[i], 'Acoustic':acoustic[i], 'Instrumental':instrumental[i], \
                                    'Liveness':liveness[i], 'Valence':valence[i], 'Tempo_Spot':tempo_spot[i], \
                                    'Duration_ms':duration_ms[i], 'Time_Sig':time_sig[i], 'Analysis_URL':analysis_url[i]}, ignore_index=True)
                    for file in os.listdir():
                        if file.endswith(".mp3") or file.endswith(".webm"):
                            os.remove(file)
                    if urls[i] != 'failed':
                        try:
                            get_audio(urls[i]);
                        except:
                            print('Audio extraction failed')
                    for file in os.listdir():
                        if file.endswith(".mp3"):
                            feat = extract_features(file)
                            df.loc[(df.Track==tracks[i]), 'tempo'] = feat['tempo']
                            df.loc[(df.Track==tracks[i]), 'zcr'] = np.mean(feat['zcr'])
                            df.loc[(df.Track==tracks[i]), 'rms'] = np.mean(feat['rms'])
                            df.loc[(df.Track==tracks[i]), 'spec_flat'] = np.mean(feat['spectral_flatness'])
                            df.loc[(df.Track==tracks[i]), 'zcr'] = np.mean(feat['zcr'])
                            df.loc[(df.Track==tracks[i]), 'spec_cent'] = np.mean(feat['spectral_centroid'])
                            df.loc[(df.Track==tracks[i]), 'spec_band'] = np.mean(feat['spectral_bandwidth'])
                            for j, e in enumerate(feat['mfccs']):
                                df.loc[(df.Track==tracks[i]), f'mfcc{j+1}'] = np.mean(e)
                                df.loc[(df.Track==tracks[i]), f'mfcc{j+1}_var'] = np.var(e)
                            for j, e in enumerate(feat['spectral_contrast']):
                                df.loc[(df.Track==tracks[i]), f'spec_cont{j+1}'] = np.mean(e)
                            for j, e in enumerate(feat['chroma']):
                                df.loc[(df.Track==tracks[i]), f'chroma{j+1}'] = np.mean(e)
                            for j, e in enumerate(feat['tonnetz']):
                                df.loc[(df.Track==tracks[i]), f'tonnetz{j+1}'] = np.mean(e)
                            shutil.move(file, '/Volumes/Samsung_T5/proj_5_songkick/'+artist.replace('/','')+'-'+tracks[i].replace('/','')+'.mp3')
                searched_artists.append(artist)
            except:
                pass
    return df

def get_city_data(cities, key):
    '''Returns a dictionary with city as key and a list of performers with upcoming shows as values'''
    city_ids = []
    performer_dict = defaultdict(list)
    for city in cities:
        query = city
        response = requests.get(f'https://api.songkick.com/api/3.0/search/locations.json?query={query}&apikey={key}')
        name = response.json()['resultsPage']['results']['location'][0]['metroArea']['displayName']
        city_id = response.json()['resultsPage']['results']['location'][0]['metroArea']['id']
        city_ids.append(city_id)
    for page in range(0,3):
        parameters = {
            'page': page
        }
        for i, city2 in enumerate(city_ids):
            query = city2
            response = requests.get(f'https://api.songkick.com/api/3.0/metro_areas/{7644}/calendar.json?apikey={key}', params=parameters)
            for event in response.json()['resultsPage']['results']['event']:
                for performer in event['performance']:
                    performer_dict[cities[i]].append(performer['displayName'])
    return performer_dict

def create_songkick_csvs(cities, key, cid, secret):
    '''Creates a csv file in the current directory for each city in the cities list'''
    performer_lists = get_city_data(cities, key)
    for city in cities:
        df = get_data_songkick(performer_lists[city], cid, secret)
        df.to_csv(f'{city}_data.csv')

def center_scale(data):
    '''Centers and scales data'''
    new_data = data - data.mean()
    scaler = StandardScaler()
    return scaler.fit_transform(new_data)

# The following functions are used for the recommender

pickle_in = open("pca_mfcc_2.pickle","rb")
pca_mfcc = pickle.load(pickle_in)
#pickle_in = open("pca_spotify_2.pickle","rb")
#pca_spotify = pickle.load(pickle_in)
pickle_in = open("km_mfccs.pickle","rb")
km = pickle.load(pickle_in)

def prep_data(data):
    '''converts dataframe from data retrieval into data for the recommenders'''
    if 'Unnamed: 0' in data.columns:
        data = data.drop(columns=['Unnamed: 0'])
    data = data.dropna().reset_index()
    data = data.drop(columns=['index','Analysis_URL','Duration_ms','Genres','Key','Time_Sig','mfcc1','mfcc1_var','tempo','Popularity', \
                          'mfcc14','mfcc14_var','mfcc15','mfcc15_var','mfcc16','mfcc16_var','mfcc17', 'Tempo_Spot',\
                          'mfcc17_var','mfcc18','mfcc18_var','mfcc19','mfcc19_var','mfcc20','mfcc20_var'])
    spotify = center_scale(data.iloc[:, 2:11].copy())
    mfccs = center_scale(data.iloc[:, 16:40].copy())
    zcr = center_scale(np.array(data.iloc[:, 11]).reshape(-1,1))
    pcafeat_mfcc = pca_mfcc.transform(mfccs)
    #pcafeat_spotify = pca_spotify.transform(spotify)
    X = np.concatenate([zcr, pcafeat_mfcc, spotify], axis=1)
    clusters = km.predict(X[:, 1:3])
    X = np.concatenate([np.array(data.Artist).reshape(-1,1), np.array(data.Track).reshape(-1,1), X, clusters.reshape(-1,1)], axis=1)
    X = pd.DataFrame(X, columns=['Artist','Track','ZCR','MFCC_PCA_1','MFCC_PCA_2','Acoustic','Dance','Energy','Inst','Live','Loud','Mode','Speech','Valence','Cluster'])
    return X

def recommender_1(cid, secret):
    '''Generates recommendations based only on euclidean distances calculated using spotify audio features'''
    city = input('Enter the city you live in: ')
    upcoming = pd.read_csv(f'{city}_data.csv')
    artists = []
    for _ in range(0,3):
        artists.append(input('Enter an artist you like: '))
    u_artists = get_data_user(artists, cid, secret)
    user = prep_data(u_artists)
    upcoming = prep_data(upcoming)

    playlist = []
    for i, row in user.iterrows():
        u_data = row[5:14]
        #center_scale(np.array(row[5:14]).reshape(-1,1))
        shortest_dist = np.inf
        playlist.append('Error: No Song')
        for j, row2 in upcoming.iterrows():
            dist = euclidean(u_data, row2[5:14])
            #u_data, center_scale(np.array(row2[5:14]).reshape(-1,1)))
            if dist < shortest_dist:
                shortest_dist = dist
                playlist[i] = row.Artist+'  ---------  '+row2.Track+' by '+row2.Artist
    return playlist

def recommender_2(cid, secret):
    '''Generates recommendations using the pca component cluster assignments and then spotify feature similarity'''
    city = input('Enter the city you live in: ')
    upcoming = pd.read_csv(f'{city}_data.csv')
    artists = []
    for _ in range(0,3):
        artists.append(input('Enter an artist you like: '))
    u_artists = get_data_user(artists, cid, secret)

    user = prep_data(u_artists)
    upcoming = prep_data(upcoming)
    playlist = []
    for cluster in range(0,4):
        user_temp = user.loc[user.Cluster==cluster].reset_index()
        user_temp = user_temp.drop(columns = 'index')
        upcoming_temp = upcoming.loc[upcoming.Cluster==cluster].reset_index()
        upcoming_temp = upcoming_temp.drop(columns = 'index')
        for i, row in user_temp.iterrows():
            u_data = row[5:14]
            shortest_dist = np.inf
            for j, row2 in upcoming_temp.iterrows():
                dist = euclidean(u_data, row2[5:14])
                if dist < shortest_dist:
                    shortest_dist = dist
                    new_track = row.Artist+'  ---------  '+row2.Track+' by '+row2.Artist
            playlist.append(new_track)
    return playlist

def simplest_recommender(cid, secret):
    '''Generates recommended playlist using only spotify features'''
    city = input('Enter the city you live in: ')
    artists = []
    for _ in range(0,3):
        artists.append(input('Enter an artist you like: '))

    user_data = pd.DataFrame(columns=['Artist','Track'])
    for artist in artists:
        try:
            genres, tracks, pop, dance, energy, key, loudness, mode, speech, acoustic, instrumental, liveness, valence, tempo_spot, duration_ms, time_sig, analysis_url = get_tracks_and_pop_user(artist, cid, secret)
            for i, track in enumerate(tracks):
                user_data = user_data.append({'Artist':artist,'Track':track, 'Acoustic':acoustic[i], 'Dance':dance[i], \
                                'Energy':energy[i], 'Instrumental':instrumental[i], 'Liveness':liveness[i], 'Loudness':loudness[i], 'Mode':mode[i], \
                                'Speech':speech[i], 'Valence':valence[i]}, ignore_index=True)
        except:
            pass
    user_data = pd.DataFrame(center_scale(user_data.iloc[:, 2:]))
    upcoming = pd.read_csv(f'{city}_data.csv')
    upcoming = prep_data(upcoming)
    playlist = []
    for i, row in user_data.iterrows():
        u_data = row
        shortest_dist = np.inf
        playlist.append('Error: No Song')
        for j, row2 in upcoming.iterrows():
            dist = euclidean(u_data, row2[5:14])
            if dist < shortest_dist:
                shortest_dist = dist
                playlist[i] = row2.Track+' by '+row2.Artist
    return playlist
