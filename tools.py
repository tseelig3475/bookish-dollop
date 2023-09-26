import requests
import json
import time

#get all players in the league (USE ONLY ONCE A DAY!)

#return time as yyyy_m_dd string for file naming                                                     
def getTime():                                                                     
   t = time.localtime()
   t = str(t.tm_year) + '_' + str(t.tm_mon) + '_' + str(t.tm_mday)                                                             
   return t                                                                        

#get players and write to cwd            
def getPlayers(playersUrl):
   #make request for json file
   players_request = requests.get(playersUrl)

   players = players_request.json()
   json_object = json.dumps(players, indent=4)

   #get time for file naming
   t = getTime()

   #write out json file
   with open("players" + t + ".json", "w") as outfile:
      outfile.write(json_object)

   return 0

def getRoster(rosterUrl, userId):
   #get roster of league and select out roster                                     
   league = requests.get(rosterUrl).json()
                                                                                   
   #grab my roster                                                                 
   for i in league:                                                                
      if i['owner_id'] == userId: roster = i                                       
                                                                                   
   return roster   

if __name__ == "__main__":
   getPlayers()

