import numpy as np

def calculate_confidence(probabilities):
    """

    Calculates confidence based on the highest class probability.

    Parameters
    ----------
    probabilities : array-like

        Example:
        [0.70,0.15,0.15]

    Returns
    -------
    float
    """

    confidence=np.max(probabilities)

    return round(confidence * 100,2)
