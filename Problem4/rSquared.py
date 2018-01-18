import numpy as np

def r_squared(y, estimated):
    """
    Calculate the R-squared error term.
    Args:
        y: list with length N, representing the y-coords of N sample points
        estimated: a list of values estimated by the regression model
    Returns:
        a float for the R-squared error term
    """

    error = 0
    for i in range(len(y)):
        error += (y[i]-estimated[i])**2
    meanError = error / len(y)
    return 1 - (meanError/np.var(y)) 
