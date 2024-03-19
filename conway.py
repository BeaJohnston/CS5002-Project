import matplotlib as mpl
from matplotlib import pyplot
import numpy

def createLattice(x,y):
    return numpy.random.rand(x,y)

def main():
    lattice = createLattice(100,100)
    cmap = mpl.colors.ListedColormap(['black','green'])
    bounds = [0,0.5,1]
    norm = mpl.colors.BoundaryNorm(bounds,cmap.N)
    img = pyplot.imshow(lattice, interpolation='nearest', cmap=cmap, norm=norm)
    pyplot.colorbar(img,cmap=cmap,norm=norm,boundaries=bounds,ticks=[0,0.5,1])
    pyplot.show()

if __name__ == "__main__":
    main()