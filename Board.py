from Tile import Tile
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from random import randint
from math import sqrt,floor,ceil




class Board:



	def __init__(self,board_size=10):

		self.board_size_px = 1000
		self.N_board = board_size

		self.tile_size = int(self.board_size_px/self.N_board)

		self.size_tuple_1x1 = (self.tile_size,self.tile_size)
		self.size_tuple_2x2= (2*self.tile_size,2*self.tile_size)

		self.im_1x1 = Image.open('1x1_colored.png')
		self.im_2x2 = Image.open('2x2_colored.png')

		self.im_1x1.thumbnail(self.size_tuple_1x1)
		self.im_2x2.thumbnail(self.size_tuple_2x2)

		self.edge_match = {0:8,1:7,2:6, 3:11,4:10,5:9, 6:2,7:1,8:0, 9:5,10:4,11:3}

		#This is the list of paths, which will be defined by their start and end points.
		#Each of those points will be defined by the coord of their tile (the 1x1 one)
		#and the index along the edge. So one entry will be like [[coord1,e_ind1],[coord2,e_ind2]]
		self.paths_list = []
		self.frontier_set = set([])
		#I should probably make a set for the path edges too (frontier), because that will be easier
		#to search and remove.

		#The tile list will be the set of 1x1 tiles (because 2x2 ones will get broken)
		#into equivalent 1x1's. The list will be of Tile objects.
		self.tile_list = []
		self.tile_pos_set = set([])
		self.disp_tile_list = []



	def insertTile(self,pos,type,rot):

		#The pos here will be the UPPER LEFT. So if it's a 2x2, you have to check
		#(x,y),(x+1,y),(x,y+1),(x+1,y+1)
		assert type in [1,2], 'type not 1 or 2'

		if type==1:
			assert pos not in self.tile_pos_set, 'tile already in {}!'.format(pos)

			self.tile_pos_set.add(pos)
			self.tile_list.append(Tile(pos,type,rot))
			self.disp_tile_list.append(Tile(pos,type,rot))

			tile = self.tile_list[-1]



			#for each edge:
			#-get its pair
			#-get both of their neighbor pos
			#-check if the neighbors exist
			#-if neither do, new path.
			#-if one does, add to current path.
			#-if both do, combine both those paths.

			for e1_i in range(12):

				e2_i = tile.pair_match[e1_i]

				(e1_s,e1_t) = self.edgeIndexToSideAndTick(e1_i)
				(e2_s,e2_t) = self.edgeIndexToSideAndTick(e2_i)

				n1_pos = self.getNeighborPos(pos,e1_s)
				n2_pos = self.getNeighborPos(pos,e2_s)


				if n1_pos in self.tile_pos_set:

					if n2_pos in self.tile_pos_set:

						#If they're both present:
						n1_e_i = self.edge_match[e1_i]
						n2_e_i = self.edge_match[e2_i]

						for i,p in enumerate(self.paths_list):
							#Just get the index here, because it's a bit more complicated
							#with two.

							if (n1_pos,n1_e_i) in p:
								path1_ind = i

							if (n2_pos,n2_e_i) in p:
								path2_ind = i

						if path1_ind==path_ind:
							



						else:
							#If they're different



					else:

						#If only n1.
						n1_e_i = self.edge_match[e1_i]

						for p in self.paths_list:
							#If that is in any of the path list "ends" (which it must),
							#remove that end, and attach the other one of the pair instead.

							if (n1_pos,n1_e_i) in p:
								p.remove((n1_pos,n1_e_i))
								p.append((pos,e2_i))
								break

				else:

					if n2_pos in self.tile_pos_set:

						#If only n2
						n2_e_i = self.edge_match[e_i]

						for i,p in enumerate(self.paths_list):
							#If that is in any of the path list "ends" (which it must),
							#remove that end, and attach the other one of the pair instead.
							if (n2_pos,n2_e_i) in p:
								p.remove((n2_pos,n2_e_i))
								p.append((pos,e1_i))
								break

					else:
						#If neither are.
						self.paths_list.append([(pos,e1_i),(pos,e2_i)])
						self.frontier_set.add((pos,e1_i))
						self.frontier_set.add((pos,e2_i))


			#Side 0-3, starting from top, CW.
			for s in range(4):
				#edge index for each side, 0-2, counting CW.

				n_coord = self.getNeighborPos(pos,s)

				for e in range(3):

					#This is the edge index of the current tick we're looking at.
					edge_index = 3*s + e
					#This is the corresponding one for the neighbor.
					n_edge_index = self.edge_match[edge_index]

					if (n_coord,n_edge_index) in self.frontier_set:

						for i,p in enumerate(self.paths_list):

							if (n_coord,n_edge_index) in p:

								e_pair_index = tile.pair_match[edge_index]
								(e_pair_s,e_pair_ei) = self.edgeIndexToSideAndTick(e_pair_index)

								#Here we're gonna get the other side of the pair for this
								#tile, and check if it too connects to some path. If it does,
								#we'll check if it's the same path (i.e., a loop), and handle it from
								#there.
								n2_coord = self.getNeighborPos(pos,e_pair_s)


								n2_coord = (pos[0]+n_coord_add[s][0],pos[1]+n_coord_add[s][1])
								if





		#...let's handle this later.
		if type==2:
			#I think for this, I should just check that the spaces are free, decompose
			#it into 1x1's, and then just call this same function on each of those.
			for i in range(2):
				for j in range(2):
					assert (pos[0]+i,pos[1]+j) not in self.tile_pos_set, 'tile already in {}!'.format((pos[0]+i,pos[1]+j))



			self.tile_pos_set.add(pos)
			self.tile_list.append(Tile(pos,type,rot))
			self.disp_tile_list.append(Tile(pos,type,rot))



		pass

	def getNeighborPos(self,pos,side):
		#pos is the x,y coord, side is 0-3, starting top, clockwise.
		#So annoyingly, the origin is the upper left, so we count to the right
		#and down.
		n_coord_add = [[0,-1],[1,0],[0,1],[-1,0]]

		return((pos[0]+n_coord_add[s][0],pos[1]+n_coord_add[s][1]))


	def edgeIndexToSideAndTick(self,e_i):
		#So this takes one of the edge ticks [0-11] and gives you the side [0-3]
		#and the edge tick on that side [0-2], (s,e)

		return((floor(e_i/3.0), e_i%3))


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





#***************Populate methods****************************




	def uniformPopulate(self):

		for i in range(self.N_board):
			for j in range(self.N_board):
				self.insertTile((i,j),type=1,rot=0)

	def randomRotPopulate(self):

		for i in range(self.N_board):
			for j in range(self.N_board):
				self.insertTile((i,j),type=1,rot=randint(0,3))

	def hStripesPopulate(self,mod=2):

		for i in range(self.N_board):
			for j in range(self.N_board):
				self.insertTile((i,j),type=1,rot=j%mod)


	def vStripesPopulate(self,mod=2):

		for i in range(self.N_board):
			for j in range(self.N_board):
				self.insertTile((i,j),type=1,rot=i%mod)


	def bothStripesPopulate(self,mod=2):

		for i in range(self.N_board):
			for j in range(self.N_board):
				self.insertTile((i,j),type=1,rot=(i+j)%mod)
				#self.insertTile((i,j),type=1,rot=floor(sqrt((i**2+j**2)))%mod)























#
