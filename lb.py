import numpy as np
import matplotlib.pyplot as plt

# selection of site
# Advection of incoming particles of direct neighborhood
# collision of new set of advected particles
# post-collision rearrangement
# next site selection



def main():
    ''' Variables '''
    # lattice dimensions = nb cells
    Nx = 300 
    Ny = 100 # for 2D
    # Timesteps (simulation duration)
    Nt = 1000
    # time scale = kinematic velocity = relaxation time
    tau = .53

    # time and space steps
    deltaT = 1
    deltaX = 1

    '''Lattice Speeds & Weights''' # each direction has a set speed of 1 to go to a node in any direction
    # Nb of velocities (= neighbours)
    NL = 3 # 1D
    # NL = 9 # 2D

    # discreete velocities of each neihbouring node
    cx = np.array([0,-1,1])  # 1D
    # 2D
    # cx = np.array([0,-1,0,1,1, 1, 0,-1,-1])
    # cy = np.array([0, 1,1,1,0,-1,-1,-1, 0])
    
    # weights
    weights = np.array([2/9,5/9,2/9]) # 1D
    # weights = np.array([4/9,1/36,1/9,1/36,1/9,1/36,1/9,1/36,1/9]) # 2D

    '''Initial conditions'''
    # "phase space " = distribution function of 3 dimensions : 1 or2 geometrical dimension(s), 1 velocity dimension
    f = np.ones([Nx,NL]) # 1D
    # f = np.ones([Nx,Ny,NL]) # 2D


main()