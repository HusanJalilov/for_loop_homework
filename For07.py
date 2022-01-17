def main(N):
    """
    Return the sum of odd numbers from zero to N.
    Args:
        N: int
    Returns:
        int: return  answer
    """
    s=0
    for x in range(N):
        d=x%2
        if d!=0:
            s=x+s
    return s
print(main(12))