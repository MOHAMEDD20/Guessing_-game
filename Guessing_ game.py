import random


# flobal variables
trys = ''        #guesses
points= 10       # number of tries


# helper functions
def new_game():
	'''
		start new guessin game 
		input: void 
		output: void

	 	# MODIFIED: None
	 	#EFFECTS: takes the chossen movie name and match it with the guessed letter 
	 				if it is one of the word : replace the '-'' with this letter
	 					otherwise: reduce points by one
	'''
	global trys, points

	print("let's Guess the characters")
	while points > 0:	
		failed = 0

		print('You are Guessing: ', end=' ')
		for char in choosen_movie: 
			if char in trys: 
				print(char, end='')		
			else: 
				print("-", end='')
				failed += 1
		if failed == 0:
			print("Congrats!! You Win :)") 
			print("The Movie  is: ", choosen_movie) 
			break
		print()	

		guess = input("guess Letter:")		
		trys += guess 
		if guess not in choosen_movie:	
			points-= 1
			print("Wrong!! be careful You have", + points, 'more guesses ')	
			if points == 0:
				print("Sorry!! You Loose :(")


if __name__ == '__main__':
	# Enter Game user's name
	name = input("What is your name to start the game~# ")
	print("Good Luck", name, "let's do that bro ^_^", '\n\n')

	# handle movie list from movies file
	movie_list =open('4_5774084939603511397.txt').read().splitlines()
	movies = [movie.lower() for movie in movie_list]

	# choose randomly one of the existant movies
	choosen_movie = random.choice(movies)

	new_game()