from Board import Board
import numpy as np
import matplotlib.pyplot as plt






b = Board(board_size=15)
#b.uniformPopulate()
#b.totalAddPopulate(mult=3)
#b.fibonacciPopulate()
#b.hStripesPopulate(mod=4)
#b.vStripesPopulate(mod=2)
#b.radialPopulate(mod=4)
#b.multPopulate(mod=3)
b.pythagTiling(big_sq_size=2,bigrot=0,smallrot=3)
#b.bothStripesPopulate(mod=4)

b.displayBoard()


exit(0)



def plotPathsVsTiles(b_sizes):

    b_sizes = np.array(b_sizes)
    n_tiles = b_sizes**2
    n_paths = []
    n_closed_paths = []
    label = ''
    for size in b_sizes:

        b = Board(board_size=size)
        #b.vStripesPopulate(mod=2)
        b.randomRotPopulate()
        n_paths.append(len(b.paths_list))
        n_closed_paths.append(b.N_closed_paths)
        label = b.label

    #plt.plot(b_sizes,n_paths)
    plt.plot(n_tiles,n_paths,'b',label='total paths')
    plt.plot(n_tiles,n_closed_paths,'k',label='closed paths')
    plt.xlabel('# tiles')
    plt.ylabel('# paths')
    #plt.plot(n_tiles,12*n_tiles**0.5,'ro',label='12*sqrt(n_tiles)')
    plt.plot(n_tiles,.6*n_tiles,'ro',label='.6*n_tiles')
    plt.plot(n_tiles,.35*n_tiles,'go',label='.35*n_tiles')

    plt.legend()
    plt.savefig('saved_plots/' + label + '_vs_tiles.png')
    #plt.show()



sizes = [1,3,5,8,10,15,20,30,40,50,70]
sizes = list(range(1,20)) + [30,30,40,40,50,50]
plotPathsVsTiles(sizes)

exit(0)



























#
