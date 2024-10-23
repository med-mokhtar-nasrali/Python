class Player:
    def __init__(self, player_info  ):
        self.name = player_info['name']
        self.age = player_info['age']
        self.position = player_info['position']
        self.team = player_info['team']
players_info=[
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32,
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33,
        "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32,
        "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]
player1=Player(players_info[0])
player2=Player(players_info[1])
player3=Player(players_info[2])
print(player1)
print(player2)
print(player3)

new_team=[]

for i in players_info:
    new_team.append(Player(i))


for player in new_team:
    print(f"Name: {player.name}, Age: {player.age}, Position: {player.position}, Team: {player.team}")