class Team:
    def __init__(self,name):
        self.team= name
        
    def assign_player(self, player):
        print(f"{player.name} is playing for {self.team}")
class Player:
    def __init__(self,name):
        self.name= name
        
p = Player("shahadat")
t = Team("Dhaka")
t.assign_player(p)
        
        