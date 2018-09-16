from Board import Board
import numpy as np
import matplotlib.pyplot as plt




b = Board(board_size=15)
#b.uniformPopulate()
#b.hStripesPopulate(mod=1)
#b.multPopulate()
b.pythagTiling(big_sq_size=2)
#b.bothStripesPopulate(mod=2)

b.displayBoard()


exit(0)



def plotPathsVsTiles(b_sizes):

    b_sizes = np.array(b_sizes)
    n_tiles = b_sizes**2
    n_paths = []
    n_closed_paths = []

    for size in b_sizes:

        b = Board(board_size=size)
        #b.uniformPopulate()
        b.hStripesPopulate()
        n_paths.append(len(b.paths_list))
        n_closed_paths.append(b.N_closed_paths)

    #plt.plot(b_sizes,n_paths)
    plt.plot(n_tiles,n_paths,'b')
    plt.plot(n_tiles,n_closed_paths,'k')
    plt.xlabel('# tiles')
    plt.ylabel('# paths')
    plt.plot(n_tiles,12*n_tiles**0.5,'ro')

    plt.savefig('horiz_p_vs_tiles.png')
    plt.show()

sizes = [1,3,5,8,10,15,20,30,40,50]

plotPathsVsTiles(sizes)

exit(0)




b = Board(board_size=25)
#b.uniformPopulate()
#b.hStripesPopulate(mod=1)
b.multPopulate()
#b.bothStripesPopulate(mod=2)

b.displayBoard()


exit(0)






b = Board(board_size=5)
b.uniformPopulate()

#b.bothStripesPopulate(mod=2)

b.displayBoard()
























#
