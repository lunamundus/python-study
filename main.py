class Player:
    def __init__(self, name, team):
        self.name = name
        self.xp = 1500
        self.team = team


    def introduce(self):
        print(f"Hello! I'm {self.name}, and I play for {self.team}")


class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []


    def show_players(self):
        for player in self.players:
            player.introduce()      # add_player 메서드에서 new_player를 생성할 떄 Player class를 사용하고 있으므로, Player class 내의 메서드를 사용할 수 있음


    def show_team_xp(self):
        total_xp = 0
        for player in self.players:
            total_xp = total_xp + player.xp

        print(f"{self.team_name} has totally {total_xp} XP!")


    def add_player(self, name):
        new_player = Player(name=name, team=self.team_name)      # self.team_name은 Team class 내의 team_name을 의미함
        self.players.append(new_player)
        print(f"{new_player.name} is successfully added to {self.team_name}.")


    def remove_player(self, name):
        if len(self.players) == 0:
            print(f"{self.team_name} has no player!")
        else:
            for player in self.players:
                if player.name == name:
                    self.players.remove(player)
                    print(f"{player.name} is successfully removed from {self.team_name}!")



team_x = Team(team_name="Team X")
team_x.add_player("nico")

team_y = Team(team_name="Team Y")
team_y.add_player("lynn")
team_y.add_player("lucas")
team_y.add_player("harry")

team_y.remove_player("lucas")

team_x.show_team_xp()
team_y.show_team_xp()