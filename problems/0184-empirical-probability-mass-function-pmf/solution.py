def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    # TODO: Implement the function
    import numpy as np
    vals,counts = np.unique(np.array(samples),return_counts=True)
    total = len(samples)
    return [(vals[i],(counts[i]/total)) for i in range(len(vals))]