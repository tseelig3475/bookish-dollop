import os
import json
import tools

URL = 'https://api.sleeper.app/v1/league/1001700554860531712/rosters'
USER_ID = '600034026157309952'
LEAGUE_ID = '1001700554860531712'

#list of URLS
PLAYERS_URL = 'https://api.sleeper.app/v1/players/nfl'
ROSTER_URL = 'https://api.sleeper.app/v1/league/'+ LEAGUE_ID +'/rosters'

def main():
   #get current date
   t = tools.getTime()

   #check if players stats have been downloaded today
   if os.path.isfile('players' + t + '.json') == False:
      print('Getting todays players')
      tools.getPlayers(PLAYERS_URL)

   #open todays player list                                                           
   with open('players' + t + '.json', 'r') as f:                                      
      players = json.load(f) 
   
   #get my roster
   roster = tools.getRoster(ROSTER_URL, USER_ID)
   
   #get starters and bench
   starters = roster['starters']
   bench = []
   for i in roster['players']:
      if i not in starters: bench.append(i)

   #check status of starters for inactive players
   print('Checking for inactive players')
   for i in starters:
      if players[i]['position'] != 'DEF':
         status = players[i]['status']
         if status == 'Inactive':
            print(players[i]['full_name'] + ' is inactive. Check for further info')



   print('check line complete')
   return 0


if __name__ == '__main__':
   main()

