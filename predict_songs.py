import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from playlist_selection import PlayListSelection

class SongPredict:

    index =0
    def main(self):
        sp = SongPredict()

        d = 4
        given_playlist = [1, 2, 3, 4]
        playlist_name = {1: 'dinner_track',
                    2: 'party_track',
                    3: 'sleep_track',
                    4: 'workout_track'}

        number_of_selections = [0] * d
        sum_of_rewards = [0] * d
        n = 0
        d = len(given_playlist)
        play_list=0

        while n >= 0:
            reward =[0]*(d)
            max_upper_bound = 0


            for i in range(0,d):
                if number_of_selections[i] >0 :
                    average_reward = sum_of_rewards[i] / number_of_selections[i]
                    delta_i = math.sqrt(3/2 * math.log(n+1)/ number_of_selections[i])
                    upper_bound = average_reward+delta_i
                else :
                    upper_bound = 1e400

                if upper_bound > max_upper_bound :
                    max_upper_bound = upper_bound
                    play_list = given_playlist[i]
            print("")
            print('%s playlist was recomended in the previous stage' % playlist_name.get(play_list))
            index = sp.playlist_choosen(given_playlist, 0, play_list)


            reward[index] = 1

            number_of_selections[given_playlist.index(play_list)] += 1
            sum_of_rewards[given_playlist.index(play_list)] += reward [given_playlist.index(play_list)]
            n = n + 1


    def playlist_choosen (self,given_playlist,previous_playlist,play_list):
        sp= SongPredict()


        if play_list !=0:

            p1 = PlayListSelection(play_list)
            song_name, artist, genere = p1.main()
            ask_user = int(input('Do you like  %s  song by  %s  from  %s playlist: ' %(song_name,artist,genere)))

            if ask_user == 1:
                return given_playlist.index(play_list)
            else:
                previous_playlist = play_list
                now_playlist_selected = random.choice(given_playlist)
                if now_playlist_selected!= previous_playlist:
                    p2 = PlayListSelection(now_playlist_selected)
                    song_name, artist, genere = p2.main()
                    ask_user = int(input('Do you like %s song by %s from %s playlist: ' %(song_name,artist,genere)))

                    if ask_user == 1:
                        return given_playlist.index(now_playlist_selected)
                    else:
                        previous_playlist=now_playlist_selected
                        return sp.playlist_choosen(given_playlist,previous_playlist,0)
                else : return sp.playlist_choosen(given_playlist,previous_playlist,0)


        else:
            now_playlist_selected = random.choice(given_playlist)
            if now_playlist_selected != previous_playlist:
                p3 = PlayListSelection(now_playlist_selected)
                song_name, artist, genere = p3.main()
                ask_user = int(input('Do you like " %s " song by " %s " from " %s " playlist: ' %(song_name,artist,genere)))

                if ask_user == 1:
                    return given_playlist.index(now_playlist_selected)
                else:
                    previous_playlist = now_playlist_selected
                    return sp.playlist_choosen(given_playlist, previous_playlist, 0)
            else: return sp.playlist_choosen(given_playlist, previous_playlist, 0)


s = SongPredict()
s.main()
















