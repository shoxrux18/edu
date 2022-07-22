# def remove_exclamation_marks(s):
#     valueToBeRemoved = 'd'
#     lst = []
#     for r in s:
#         lst.append(r)
    
        
        
#     lst = [value for value in lst if value != valueToBeRemoved]
#     lst = "".join(lst)
#     return lst
# print(remove_exclamation_marks('hello world!!!'))
# s = "nima gap?p"

# t = {k:s.count(k) for k in s}

# print({k:v for k,v in t.items() if v == max(t.values())})


import datetime
"""
CONSTRUCTOR
"""
# class Car:
#     # constructor -> object yaratayotganda self dan kn 
#     # keladi parametrlar - yurgan,narxi,obyektni dastlabki qiymatini elon qilish -cons
#     # init function constructor deyiladi
#     def __init__(self,yurgan,narxi):
#         self.nomi = None
#         self.rangi = None
#         self.yili = None
#         self.yurgan = yurgan
#         self.narxi = narxi
    
#     def real_narx(self):
#         return self.narxi * (1 - self.yurgan / 1000000)

#     def yoshi(self):
#         return datetime.datetime.now().year - self.yili

# car = Car(15000,12000)
# print(car.real_narx())


"""
DESTRUCTOR
"""
# class Car:
#     # desctructor -> objectni ochirish uchun chaqiriladi,obyekt ochirilganda del metodi 
#     # chaqiriladi
#     def __init__(self,yurgan,narxi):
#         self.nomi = None
#         self.rangi = None
#         self.yili = None
#         self.yurgan = yurgan
#         self.narxi = narxi
#     def __del__(self):
#         print('Xotiradan ochdi')

#     def real_narx(self):
#         return self.narxi * (1 - self.yurgan / 1000000)

#     def yoshi(self):
#         return datetime.datetime.now().year - self.yili

# car = Car(16000,12000)
# print(car.real_narx())

"""
INHERITENCE
"""

# class Shakl:
#     def __init__(self,nomi):
#         pass


# def most_populated(population):
#     years = dict()
#     for person in population:
#         for year in range(person[0], person[1]):
#             if year in years:
#                 years[year] += 1
#             else:
#                 years[year] = 0
#     return max(years, key=years.get) if [key for key, val in years.items() if val == max(years.values())] else False

# print(most_populated([(1, 4), (3, 8),
#                       (9, 10), (2, 7)]))


# def abs():
#     numbers = [1,2,3,1,1]
#     numbers.sort()
#     print(numbers)

# abs()

# declare our own string class
# class String:
	
# 	# magic method to initiate object
# 	def __init__(self, string):
# 		self.string = string
		
# 	# print our string object
# 	def __repr__(self):
# 		return 'Object: {}'.format(self.string)
		
# 	def __add__(self, other):
# 		return self.string + other

# # Driver Code
# if __name__ == '__main__':
	
# 	# object creation
# 	string1 = String('Hello')
	
# 	# concatenate String object and a string
# 	print(string1 +' Geeks')
class Example:
    def __init__(self):
        print("Instance Created")
      
    # Defining __call__ method
    def __call__(self):
        print("Instance is called via special method")
  
# Instance created
e = Example()
  
# __call__ method will be called
e()