def main(A,B):
    """
    Return the numbers from B to A in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    s=[]
    for x in range(B,A-1,-1):
        s.append(x)
    return s
print(main(5,9))