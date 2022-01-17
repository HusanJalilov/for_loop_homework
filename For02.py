def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    s=[]
    d=str(n)
    for x in range(len(d)):
        s.append(d[x])
    return(s)
    
        
    
print(main(1245))

