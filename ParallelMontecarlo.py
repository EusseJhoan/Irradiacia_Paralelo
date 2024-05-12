from mpi4py import MPI
import numpy as np
import pandas as pd



comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def f(lam, theta):
    """
    Compute the spectral radiance using Planck's law.

    Args:
        lam (float): Wavelength (meters).
        theta (float): Polar angle (radians).

    Returns:
        float: Spectral radiance (W/m^2).
    """    
    c1 = 3.747e-16  # 2*pi*h*c*c [Wm^2]
    c2 = 1.438e-2   # h*c/k [mK]
    Rsol = 6.96392e8  # Solar radius [m]
    Dsol = 1.496e11   # Distance Earth-Sun [m]
    T = 5782.0        # Surface temperature [K]
    f_t = np.cos(theta) * np.sin(theta)
    Ed = f_t * (Rsol / Dsol) ** 2 * c1 / (lam ** 5 * (np.exp(c2 / (lam * T)) - 1.0))
    return Ed

def mc_parallel(N):

    """
    Perform parallel Monte Carlo integration using MPI.

    Args:
        N (int): Total number of samples.

    Returns:
        None
    """

    N_local = N // size #Define the size of the local array 
    
    #Define integration bounds
    lam1, lam2 = 0.1e-9, 3000e-9
    t1, t2 = 0.0, np.pi / 2.0
    phi1, phi2 = 0.0, 2.0 * np.pi
    local_sum = 0.0

    wt = MPI.Wtime()

    #Estimate the local value of integrals
    for _ in range(N_local):
        lam = np.random.uniform(lam1, lam2)
        theta = np.random.uniform(t1, t2)
        local_sum += f(lam, theta)

    
    # Reduce local sums to get the global sum
    global_sum = comm.reduce(local_sum, op=MPI.SUM, root=0)
    wt = MPI.Wtime() - wt

    
    #Extract the Montecarlo estimate from core 0 
    if rank == 0:
        integral_estimate = (t2 - t1) * (phi2 - phi1) * (lam2 - lam1) * global_sum / N
        return [N, integral_estimate, wt] 


# Total number of samples
N = 100
results=[]

for _ in range(7): 
    
    results.append(mc_parallel(N))
    N *= 10


# Convert results list to a numpy array
results_array = np.array(results)

df = pd.DataFrame(results_array)

# Save the numpy array to a CSV file
filename = f'mc_parallel_{size}.csv'
df.to_csv(filename, index=False, header=False)

print(f"Finished proccess for {size} cores")