from a1_partb import SetList

class DisjointSet:


	def __init__(self):
		self.parent = {}
		self.rank = {}
		self.num_sets = 0

		

	def make_set(self, element):
		if element in self.parent:
			return False
		self.parent[element] = element
		self.rank[element] = 1
		self.num_sets += 1
		return True
	
	def get_set_size(self,element):
		rep = self.find_set(element)
		if rep is None:
			return 0
		return self.rank[rep]
		

		

	def find_set(self, element):
		if element not in self.parent:
			return None
		if self.parent[element] != element:
			self.parent[element] = self.find_set(self.parent[element])
		return self.parent[element]

		
	

		

	def union_set(self, element1, element2):
		rep1 = self.find_set(element1)
		rep2 = self.find_set(element2)

		if rep1 is None or rep2 is None or rep1 == rep2:
			return False
		if self.rank[rep1] > self.rank[rep2]:
			self.parent[rep2] = rep1
			self.rank[rep1] += self.rank[rep2]

		else:
			self.parent[rep1] = rep2
			self.rank[rep2] += self.rank[rep1]

		self.num_sets -= 1
		return True

	def get_num_sets(self):
		return self.num_sets


	def __len__(self):
		return len(self.parent)
