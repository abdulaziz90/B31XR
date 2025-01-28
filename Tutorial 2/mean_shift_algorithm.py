import numpy as np

def mean_shift(data, kernel_bandwidth=1):
    """
    Perform mean shift clustering on the input data.
    """
    # Define the kernel function
    kernel = lambda x: np.exp(-x**2 / kernel_bandwidth**2)
    
    # Initialize the centroids
    centroids = np.array(data)
    
    while True:
        # Initialize the new centroids
        new_centroids = np.array([np.zeros(data.shape[1]) for _ in range(centroids.shape[0])])
        
        # Initialize the weights
        weights = np.zeros((centroids.shape[0], data.shape[0]))
        
        for i, x in enumerate(data):
            # Calculate the distances between the data point and the centroids
            distances = np.linalg.norm(x - centroids, axis=1)
            
            # Calculate the weights for each centroid
            weights[:, i] = kernel(distances)
            
        # Update the new centroids
        for i in range(centroids.shape[0]):
            new_centroids[i] = np.average(data, axis=0, weights=weights[i])
        
        # Check for convergence
        if np.linalg.norm(new_centroids - centroids) < 1e-6:
            break
        
        # Update the centroids
        centroids = new_centroids
    
    return centroids