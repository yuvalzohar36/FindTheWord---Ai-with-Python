import random
target_word = "Define Some Word"
mutationRate = 0.01

class Pop():
	def __init__(self) :
		self.pop_size = 500
		self.population = []
		for i in range(self.pop_size):      # Create all population
			self.population.append(Dna(target_word))

	def evaluate(self):
		for p in range(self.pop_size):
			newstr =''.join(self.population[p].genes)
			print(newstr)
			if (newstr == target_word):
				print("Win")
				return newstr
				
		for i in range(self.pop_size):
			self.population[i].calc_fitness(target_word)
		mating_pool = []

		for j in range(self.pop_size):
			multi = int(random.randint(0,int(self.population[j].fitness * 100)))
			for p in range(multi):
				mating_pool.append(self.population[j])

		for k in range(len(self.population)):
			a = int(random.randint(0,len(mating_pool)-1))
			b= int(random.randint(0,len(mating_pool)-1))
			ParentA = mating_pool[a]
			ParentB = mating_pool[b]
			child = ParentA.crossover(ParentB)
			self.population[k] = child 

class Newchar ():
	def random_char():
		c = random.randint(64,122)           # According to ascii table, google it for more information .
		if (c == 64):
			c = 32                             # Convert @ to space
		return chr(c)

class Dna():
	def __init__(self, target_word):
		self.genes = []
		self.fitness = 1
		for i in range(len(target_word)):
			self.genes.append(Newchar.random_char())                   # Create random chars genes array

	def calc_fitness(self, target):
		score = 1
		for i in range (len(self.genes)):
			if (self.genes[i] == target[i]):
				score+=1
		self.fitness = score / len(target)

	def crossover(self, partner):
		child = Dna(self.genes)
		midpoint = random.randint(0,len(self.genes))
		for j in range(len(self.genes)):
			if (j > midpoint):
				child.genes[j] = self.genes[j]
			else:
				child.genes[j] = partner.genes[j]
		return child

	def mutation(self):
		for k in range(len(self.genes)):
			if (random.randint(0,1) < mutationRate):
				self.genes[k] = Newchar.random_char()


if __name__ == '__main__':
	print("Target is : " + target_word)
	pop = Pop()
	pop.evaluate()
	while (pop.evaluate() != target_word):
		pop.evaluate()

