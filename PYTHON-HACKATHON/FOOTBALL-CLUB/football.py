class Footballer:
	def __init__(self, name, club, transfer_fee, position, debut_date, continent):
		self.name = name
		self.club = club
		self.transfer_fee = transfer_fee
		self.position = position
		self.debut_date = debut_date
		self.continent = continent

class SuperLeague:
	def __init__(self, footballers, club_rankings):
		self.footballers = footballers
		self.club_rankings = club_rankings

	#method 1
	def high_value_players(self, threshold_fee):
		dic = {}
		for i in self.footballers:
			if i.continent == 'Europe' and i.transfer_fee > threshold_fee and self.club_rankings[i.club] <= 5:
				dic[i.name] = i.transfer_fee
		return dic

	#method 2
	def versatile_players(self, year):
		name_lis = []
		for i in self.footballers:
			if len(i.position) > 2 and int(i.debut_date.split('/')[2]) > year:
				name_lis.append(i.name)
		return name_lis

if __name__ == '__main__':
	footballers = []
	club_rankings = {}
	n = int(input())
	for _ in range(n):
		name = input()
		club = input()
		transfer_fee = float(input())
		m = int(input())
		position = []
		for k in range(m):
			position.append(input())
		debut_date = input()
		continent = input()
		footballers.append(Footballer(name, club, transfer_fee, position, debut_date, continent))
	for i in range(5):
		club_name = input()
		rank = int(input())
		club_rankings[club_name] = rank

	threshold_fee = float(input())
	year = int(input())

	obj = SuperLeague(footballers, club_rankings)

	result_1 = obj.high_value_players(threshold_fee)
	result_2 = obj.versatile_players(year)

	if len(result_1) != 0:
		for i,j in result_1.items():
			print(f'{i} {j}')
	else:
		print("No high-value player found with given criteria.")

	if len(result_2) != 0:
		result_2.sort()
		for i in result_2:
			print(i)
	else:
		print("No versatile player found with given criteria.")






