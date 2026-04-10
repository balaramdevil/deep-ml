import numpy as np

def recall(y_true, y_pred):
    """
    Calculate the recall metric for binary classification.
    
    Args:
        y_true: Array of true binary labels (0 or 1)
        y_pred: Array of predicted binary labels (0 or 1)
    
    Returns:
        Recall value as a float
    """
    actual = np.sum(y_true == 1)
    predicted = np.sum((y_true == y_pred) & (y_true==1))
    return predicted / actual
