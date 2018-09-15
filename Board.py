from Tile import Tile
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from random import randint





class Board:



	def __init__(self,board_size=10):

		self.N_board = board_size

		self.tile_size = 100
		self.size_tuple_1x1 = (self.tile_size,self.tile_size)
		self.size_tuple_2x2= (2*self.tile_size,2*self.tile_size)

		self.im_1x1 = Image.open('1x1_colored.png')
		self.im_2x2 = Image.open('2x2_colored.png')

		self.im_1x1.thumbnail(self.size_tuple_1x1)
		self.im_2x2.thumbnail(self.size_tuple_2x2)


		#This is the list of paths, which will be defined by their start and end points.
		#Each of those points will be defined by the coord of their tile (the 1x1 one)
		#and the index along the edge.
		self.paths_list = []

		#The tile list will be the set of 1x1 tiles (because 2x2 ones will get broken)
		#into equivalent 1x1's. The list will be of Tile objects.
		self.tile_list = []
		self.tile_coord_set = set([])
		self.disp_tile_list = []



	def uniformPopulate(self):

		for i in range(self.N_board):
			for j in range(self.N_board):
				self.insertTile((i,j),type=1,rot=0)

	def randomRotPopulate(self):

		for i in range(self.N_board):
			for j in range(self.N_board):
				self.insertTile((i,j),type=1,rot=randint(0,3))

	def hStripesPopulate(self):

		for i in range(self.N_board):
			for j in range(self.N_board):
				self.insertTile((i,j),type=1,rot=i%2)


	def insertTile(self,pos,type,rot):

		#The pos here will be the UPPER LEFT. So if it's a 2x2, you have to check
		#(x,y),(x+1,y),(x,y+1),(x+1,y+1)
		assert type in [1,2], 'type not 1 or 2'

		if type==1:
			assert pos not in self.tile_coord_set, 'tile already in {}!'.format(pos)

			self.tile_coord_set.add(pos)
			self.tile_list.append(Tile(pos,type,rot))
			self.disp_tile_list.append(Tile(pos,type,rot))

		#...let's handle this later.
		if type==2:
			#I think for this, I should just check that the spaces are free, decompose
			#it into 1x1's, and then just call this same function on each of those.
			for i in range(2):
				for j in range(2):
					assert (pos[0]+i,pos[1]+j) not in self.tile_coord_set, 'tile already in {}!'.format((pos[0]+i,pos[1]+j))



			self.tile_coord_set.add(pos)
			self.tile_list.append(Tile(pos,type,rot))
			self.disp_tile_list.append(Tile(pos,type,rot))



		pass


	def decomp2x2(self,pos,type,rot):
		pass


	def plotType1(self,tile):
		#pos will be the UPPER LEFT coord of the tile.
		pos = tile.pos
		rot = tile.rot
		self.bg.paste(self.im_1x1.rotate(rot*90),box=(pos[0]*self.tile_size,pos[1]*self.tile_size))

	def plotType2(self,pos):
		#pos will be the UPPER LEFT coord of the tile.
		self.bg.paste(self.im_2x2,box=(pos[0]*self.tile_size,pos[1]*self.tile_size))



	def displayBoard(self):

		self.bg = Image.new(mode='RGBA',size=(self.N_board*self.tile_size,self.N_board*self.tile_size),color='white')

		for tile in self.disp_tile_list:
			self.plotType1(tile)

		self.bg.show()

		return(0)































#
