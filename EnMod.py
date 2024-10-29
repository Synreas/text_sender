class EnMod:
	_string = ""
	_list = []
	string_em = ""
	list_em = []

	def __init__(self, arr=""):
		if(type(arr) is str):
			self._string = arr
			self._list = self.parser(arr)

		elif(type(arr) is list):
			self._list = arr

	def parser(self, st, w=" "):
		parsed = []
		word = ""
		for i in st:
			if ord(i) != ord(w):
				word += i
			elif(word != ""):
				parsed.append(word)
				word = ""
		parsed.append(word)
		word = ""
		return parsed

	def upload(self, arr):
		self.__init__(arr)

	def reset(self):
		self._string = ""
		self._list = []
		self.string_em = ""
		self.list_em = []

	def uploaded(self):
		return self._string

	def encrypt(self):
		self.list_em = []
		self.string_em = ""
		for i in self._list:
			l = len(i)
			word = ""
			for j in i:
				w = chr(ord(j) + l)
				l += 1
				word += w
			self.list_em.append(word)

		for i in range(len(self.list_em)):
			self.string_em += self.list_em[i]
		
		seperator = chr(ord(sorted(self.string_em)[-1]) + 1)
		self.string_em = ""

		for i in range(len(self.list_em)):
			self.string_em += self.list_em[i]
			if(i != len(self.list_em) - 1):
				self.string_em += seperator

	def decrypt(self):
		seperator = sorted(self._string)[-1]
		self._list = self.parser(self._string, seperator)
		self.list_em = []
		self.string_em = ""
		for i in self._list:
			l = len(i)
			word = ""
			for j in i:
				w = chr(ord(j) - l)
				l += 1
				word += w
			self.list_em.append(word)

		for i in range(len(self.list_em)):
			self.string_em += self.list_em[i]
			if(i != len(self.list_em) - 1):
				self.string_em += " "

	def encrypted(self):
		self.encrypt()
		return self.string_em

	def decrypted(self):
		self.decrypt()
		return self.string_em