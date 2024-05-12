import numpy as np
import pandas as pd
import time

def f(lam, theta):
    """
    Function to calculate the solar irradiance at a given wavelength and angle.

    Parameters:
    lam (float): Wavelength in meters.
    theta (float): Angle in radians.

    Returns:
    float: Solar irradiance in W/m^2.
    """
    c1 = 3.747e-16  # 2*pi*h*c*c [Wm^2]
    c2 = 1.438e-2   # h*c/k [mK]
    Rsol = 6.96392e8  # Solar radius [m]
    Dsol = 1.496e11   # Distance Earth-Sun [m]
    T = 5782.0        # Surface temperature [K]
    f_t = np.cos(theta) * np.sin(theta)
    Ed = f_t * (Rsol / Dsol) ** 2 * c1 / (lam ** 5 * (np.exp(c2 / (lam * T)) - 1.0))
    return Ed

def mc(N):
    """
    Function to calculate the integral of the solar irradiance over a hemisphere using Monte Carlo method.

    Parameters:
    N (int): Number of random points.

    Returns:
    float: Integral value.
    """
    
    #Define integration bounds
    lam1, lam2 = 0.1e-9, 3000e-9
    t1, t2 = 0.0, np.pi / 2.0
    phi1, phi2 = 0.0, 2.0 * np.pi
    integral_sum = 0.0

    
    #generation of random numbers inside the integration bounds
    for _ in range(N):
        lam = np.random.uniform(lam1, lam2)
        theta = np.random.uniform(t1, t2)
        integral_sum += f(lam, theta)

    integral = (t2 - t1) * (phi2 - phi1) * (lam2 - lam1) * integral_sum / N #Montecarlo estimate
    return integral

results = []
N = 100 #Number of random points
    
for _ in range(7): 

    start_time = time.time()
    integral_value = mc(N) # Calculate the Montecarlo estimate
    end_time = time.time()

    elapsed_time = end_time - start_time # Time 

    results.append([N, integral_value, elapsed_time])

    N *= 10    


# Convert results list to a numpy array
results_array = np.array(results)

df = pd.DataFrame(results_array)

# Save the numpy array to a CSV file
filename = f'mc_serial2.csv'
df.to_csv(filename, index=False, header=False)

print(f"Finished proccess for serial computing")
