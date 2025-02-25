import numpy as np
import matplotlib.pyplot as plt

import scipy.io as sio

data = sio.loadmat('data1.mat')
# data = sio.loadmat('data2.mat')

time = data['time'].squeeze(0)
T = len(time)  # Number of time instants
sigma2_noise = 1e1  # Variance of observation noise

# y=y+...
# y0=y0+...

# Create arrays to store the track and intermediate variables
M_t_tminus1 = np.zeros((4, T))  # Predictive means
Sigma_t_tminus1 = np.zeros((4, 4, T))  # Predictive covariance matrices
M_t_t = np.zeros((4, T))  # Corrected means (after observation)
Sigma_t_t = np.zeros((4, 4, T))  # Corrected covariance matrices

# Initialization
# Q = ...

# B = ...

R = np.diag([0.1, 0.1, 0.1, 0.1])

M_0_0 = np.array([0, 0, 0, 0])  # Initial mean vector
Sigma_0_0 = 1e2 * np.eye(4)

M_t_tminus1[:, 0] = Q @ M_0_0
Sigma_t_tminus1[:, :, 0] = Q.T @ Sigma_0_0 @ Q + R

# Main Kalman Filter loop
for t in range(T):
    if t > 0:
        # Prediction step
        # To be completed
        # .....
    
    # Correction step
    # % To be completed
    # % Include test to see if y(1,t) is NaN or not
        # % if z(1,t) is a NaN .....
        # % if z(1,t) is not a NaN ....
        # y_tilde=...
        # Kt= ... % Kalman gain
        # % ....


# Create figures here


