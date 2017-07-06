from numpy import array
from numpy import arange as range #renaming 'range' from a list type to an array type to increase speed

class list_2:

	lst_addable_values = [ type ( [ ] ) , type ( array ( [ 0 ] ) ) ] #things that can be added to the list via the '+' operator

	def __init__ ( self , iterable = [ ] ) :
		self._lst = array ( iterable )
		self.__is_Aaddable = True

	def __str__ ( self ) :
		return ( str ( list ( self._lst ) ) )

	def __add__ ( self , y ) :

		try:

			if type ( y ) in list_2.lst_addable_values or self.__is_Aaddable:

				len_y = len ( y )
				leng = len_y + len ( self._lst )
				temp_lst = [	]
		
				for x in range ( leng ) :
					if x >= len ( self._lst ) :
						temp_lst.append ( y [ x - len ( self._lst ) ] )

					else :
						temp_lst.append ( self._lst [ x ] )

				return ( list_2 ( temp_lst ) )

			else:
				raise TypeError

		except AttributeError:
			pass

	def __delitem__(self,key):
		self. pop ( key )

	def __len__ ( self ) :

		length = 0

		for x in self._lst :
			length += 1

		return length

	def __getitem__ ( self , index ) :
		return ( self._lst [ index ] )

	def __setitem__ ( self , key , value ) :
		self._lst [ key ] = value

	def __contains__ ( self , item ) :
		for x in self._lst :
			if x == item :
				break
		else:
			return False
		return True

	def __iter__ ( self ) :
		for x in self._lst :
			yield ( x )
	
	def __reversed__ ( self ) :
		for x in reversed ( self._lst ) :
			yield ( x )

	def __mul__ ( self , value ) :
		temp_lst = range ( len ( self ) * value )
		x=0
		for i in range(value):
			for j in self:
				temp_lst[ x ] = j
				x += 1
		return list_2 ( temp_lst )

	def append ( self , item ) :
		
		temp_lst = array ( list ( self._lst ) + [ None ] )
		temp_lst [ -1 ] = item
		
		self._lst = array ( temp_lst )
	
	def pop ( self , index = -1 ) :
		temp_lst = list ( self._lst )
		temp_val = temp_lst.pop ( index )
		self._lst = array ( temp_lst )
		return temp_val

	def remove ( self , value ):

		for x in range ( len ( self ) ):
			if self [ x ] == value :
				self.pop ( x )
				break
		else:
			raise AttributeError

	def count ( self , value ) :
		count = 0

		for x in self :
			if x == value :
				count += 1

		return count

	def clear ( self ) :
		self._lst = array( [ ] )

	def reverse ( self ) :
		
		temp_lst = list_2()

		for x in reversed ( self ) :
			temp_lst.append ( x )
		
		self._lst = array ( temp_lst._lst )
	
	def index ( self , value , start = None , stop = None ) :#fix index
		if start == None and stop == None:

			for x in range ( len ( self ) ) :
				if self[ x ] == value:
					return x
			else:
				raise ValueError

		elif stop == None:

			for x in range ( start , len ( self ) ):
				if self[ x ] == value:
					return x
			else:
				raise ValueError

		else:

			for x in range ( start , stop ) :
				if self[ x ] == value:
					return x
			else:
				raise ValueError

	def extend ( self , iterable ) :

		for x in iterable :
			self.append( x )

	def insert ( self , index , object ) :

		temp_lst = array ( range ( len ( self ) + 1 ) )
		temp_bool = False
		
		for x in range ( len ( self ) ) :
			
			if x == index :
			
				temp_lst [ x ] = object
				temp_lst [ x + 1 ] = self [ x ]
				temp_bool = True
			
			elif temp_bool:

				temp_lst[ x + 1 ] = self [ x ]

			else:

				temp_lst [ x ] = self [ x ]

		self._lst = temp_lst

	def __qsort ( self , arr ) :
		if len(arr) <= 1 :
			return arr
		else:
			return self.__qsort ( [ x for x in arr [ 1 : ] if x < arr [ 0 ] ] ) + [ arr [ 0 ] ] + self.__qsort ( [ x for x in arr [ 1 : ] if x >= arr [ 0 ] ] )

	def sort ( self ) :
		self._lst = self.__qsort(self._lst)

def main ( ) :
	from random import shuffle
	list_2_temp = list_2 ( [ 5 , 2 , 23 , 6 , - 1 , 7 ] )
	print(list_2_temp)
	list_2_temp.sort()
	print(list_2_temp)

if __name__ == '__main__':
        main()
