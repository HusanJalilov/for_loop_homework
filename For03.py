def main(k,n):
    """
    Repeat the number k n times and return to the list view.
    Args:
        k: int
        n: int
    Returns:
        list: return  answer
    """
    s=[]
    k=str(k)
    s.append(k)
    return s*n
print(main(1,4))