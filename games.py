class piedra_papel_tijeras():
    # 0 = rock
	# 1 = paper
	# 2 = scissors
 
	## Returns:
	# 0 = tie
	# 1 = player 1 winner
	# 2 = player 2 winner

	def get_winner(p1:int, p2:int):
		if p1 == p2:
			return 0
		elif (p1 + 1) % 3 == p2:
			return 2
		else:
			return 1

class tic_tac_toe():
# 7 = empty
# 1 = player 1
# 2 = player 2
  
	def get_winner(map):
		for row in map:
			if sum(row) in (3, 6):
				return row[0]
		for i in range(0, 3):
			suma = 0
			for n in range(0, 3):
				suma += map[n][i]
			if suma in (3, 6):
				return map[0][i]
		if sum([map[0][0], map[1][1], map[2][2]]) in (3, 6):
			return map[0][0]
		if sum([map[0][2], map[1][1], map[2][0]]) in (3, 6):
			return map[0][2]
		else:
			return 0