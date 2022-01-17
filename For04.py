def main(A,B):
    """
    Return the numbers from A to B in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    s=[]
    for x in range(A,B):
        s.append(x)
    return s
print(main(2,7))
        