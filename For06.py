def main(A,B):
    """
    Return the sum of all integers from A to B.
    Args:
        A: int
        B: int
    Returns:
        int: return  answer
    """
    summ=0
    for x in range(A,B):
        summ+=x
    return summ
print(main(1,10))