from dataclasses import dataclass, field


@dataclass(order=True)
class FootballPlayer:
    name: str = field(compare=False)
    surname: str = field(compare=False)
    value: int = field(repr=False)


@dataclass
class FootballTeam:
    name: str
    players: list = field(init=False, default_factory=list, repr=False, compare=False)

    def add_players(self, *args):
        self.players.extend(args)


# Входные данные1
player = FootballPlayer('Kylian', 'Mbappe', 180000000)

print(player)
print(player.name)
print(player.surname)
print(player.value)
# Выходные данные1

# FootballPlayer(name='Kylian', surname='Mbappe')
# Kylian
# Mbappe
# 180000000

# Входные данные2
player1 = FootballPlayer('Jude', 'Bellingham', 120000000)
player2 = FootballPlayer('Vinicius', 'Junior', 120000000)
player3 = FootballPlayer('Kylian', 'Mbappe', 180000000)

print(player1 == player2)
print(player1 == player3)
print(player1 > player3)
print(player1 < player3)
# Выходные данные2
# True
# False
# False
# True

# Входные данные3
team = FootballTeam('PSG')

print(team)
print(team.name)
print(team.players)

team.add_players(FootballPlayer('Kylian', 'Mbappe', 180000000))
print(team.players)
# Выходные данные3
# FootballTeam(name='PSG')
# PSG
# []
# [FootballPlayer(name='Kylian', surname='Mbappe')]

# Входные данные4
team1 = FootballTeam('PSG')
team2 = FootballTeam('PSG')
team3 = FootballTeam('Arsenal')

player1 = FootballPlayer('Jude', 'Bellingham', 120000000)
player2 = FootballPlayer('Vinicius', 'Junior', 110000000)
player3 = FootballPlayer('Kylian', 'Mbappe', 180000000)

team1.add_players(player1)
team2.add_players(player2)
team3.add_players(player3)

print(team1 == team2)
print(team1 != team2)
print(team1 == team3)
print(team1 != team3)

# Выходные данные4
# True
# False
# False
# True


# TEST_5:
player1 = FootballPlayer('Ronaldo', '', 20000000)
player2 = FootballPlayer('Lothar', 'Matthaus', 250000000)
player3 = FootballPlayer('Xavi', 'Simons', 54000000)
player4 = FootballPlayer('Paolo', 'Maldini', 28000000)
player5 = FootballPlayer('Лев', 'Яшин', 200000000)
player6 = FootballPlayer('Diego', 'Maradona', 305000000)
player7 = FootballPlayer('Lionel', 'Messi', 180000000)
player8 = FootballPlayer('Kristiano','Ronaldo',10000000)

team = FootballTeam('Best')
print(team.name)

team.add_players(player1, player2, player3, player4, player5, player6, player7, player8)
print(team.players)


# TEST_5:
# Best
# [FootballPlayer(name='Ronaldo', surname=''), FootballPlayer(name='Lothar', surname='Matthaus'), FootballPlayer(name='Xavi', surname='Simons'), FootballPlayer(name='Paolo', surname='Maldini'), FootballPlayer(name='Лев', surname='Яшин'), FootballPlayer(name='Diego', surname='Maradona'), FootballPlayer(name='Lionel', surname='Messi'), FootballPlayer(name='Kristiano', surname='Ronaldo')]