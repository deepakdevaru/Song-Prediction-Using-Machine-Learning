import pandas as pd
import random


class PlayListSelection:

    def __init__(self,value):
        self.value =value

    def main(self):

        switcher = {
                    1: self.dinner_track(),
                    2: self.party_track(),
                    3: self.sleep_track(),
                    4: self.workout_track()
                    }
        return switcher.get(self.value)




    def dinner_track(self):
        dataframe = pd.read_csv('datasets/dinner_track.csv')
        song_name = random.choice(dataframe['name'])
        index = dataframe.loc[dataframe['name']==song_name]
        artist = index.iloc[:,3]
        genere = 'dinner_track'
        return song_name,artist,genere

    def party_track(self):
        dataframe = pd.read_csv('datasets/party_track.csv')
        song_name = random.choice(dataframe['name'])
        index = dataframe.loc[dataframe['name'] == song_name]
        artist = index.iloc[:, 3]
        genere ='party_track'
        return song_name, artist,genere

    def sleep_track(self):
        dataframe = pd.read_csv('datasets/sleep_track.csv')
        song_name = random.choice(dataframe['name'])
        index = dataframe.loc[dataframe['name'] == song_name]
        artist = index.iloc[:, 3]
        genere ='sleep_track'
        return song_name, artist,genere

    def workout_track(self):
        dataframe = pd.read_csv('datasets/workout_track.csv')
        song_name = random.choice(dataframe['name'])
        index = dataframe.loc[dataframe['name'] == song_name]
        artist = index.iloc[:,3]
        genere ='workout_track'
        return song_name, artist,genere

