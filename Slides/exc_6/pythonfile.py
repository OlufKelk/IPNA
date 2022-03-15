def utility(z,psi):
    """ Calculates utility of given some assets, z, and relative risk aversion, psi.

    Args:
    z (float): the agents assets
    psi (float): the agents relative risk aversion

    Returns:
    (float): utility of assets
    """
    return (z**(1+psi))/(1+psi)