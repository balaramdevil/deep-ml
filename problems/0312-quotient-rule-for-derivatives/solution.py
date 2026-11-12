import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    g_val = 0
    h_val = 0
    g_der = 0
    h_der = 0
    coeff = 0
    for j in g_coeffs[::-1]:
        g_val += (j*(x**coeff))
        coeff +=1
    coeff = 0
    for j in h_coeffs[::-1]:
        h_val += (j*(x**coeff))
        coeff +=1
    coeff = 0
    for j in g_coeffs[::-1]:
        if coeff!=0 :
            g_der += (j*(x**(coeff-1))*coeff)
        coeff +=1
    coeff = 0
    for j in h_coeffs[::-1]:
        if coeff!=0:
            h_der += (j*(x**(coeff-1))*coeff)
        coeff +=1
    return ((g_der*h_val) - (g_val*h_der)) / (h_val**2)