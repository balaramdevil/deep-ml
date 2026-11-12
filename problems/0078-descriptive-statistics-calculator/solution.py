import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    vals,cnts = np.unique(data,return_counts=True)
    idx = np.argmax(cnts)
    mode = vals[idx]
    mean = np.mean(data)
    median = np.median(data)
    variance = np.var(data)
    std_dev = np.std(data)
    percentile_25 = np.percentile(data,25)
    percentile_50 = np.percentile(data,50)
    percentile_75 = np.percentile(data,75)
    iqr = percentile_75 - percentile_25
    return {'mean': mean, 'median': median, 'mode': mode, 'variance': variance, 'standard_deviation': std_dev, '25th_percentile': percentile_25, '50th_percentile': percentile_50, '75th_percentile': percentile_75, 'interquartile_range': iqr}