class rock_paper_scissors():
	def get_winner(p1:int, p2:int):
		if p1 == p2:
			return "tie"
		elif (p1 + 1) % 3 == p2:
			return "player2"
		return "player1"

class tic_tac_toe():
# 7 = empty
  
	def get_winner(map):
		for row in map:
			if sum(row) == 3:
				return "player1"
			elif sum(row) == 6:
				return "player2" 
		for i in range(0, 3):
			suma = 0
			for n in range(0, 3):
				suma += map[n][i]
			if suma == 3:
				return "player1"
			elif suma == 6:
				return "player2" 
		if sum([map[0][0], map[1][1], map[2][2]]) == 3:
			return "player1"
		elif sum([map[0][0], map[1][1], map[2][2]]) == 6:
			return "player2" 
		if sum([map[0][2], map[1][1], map[2][0]]) == 3:
			return "player1"
		elif sum([map[0][2], map[1][1], map[2][0]]) == 6:
			return "player2" 
		else:
			return 0
