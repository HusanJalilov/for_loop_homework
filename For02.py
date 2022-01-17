def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    d=""
    s=str(n)
    for x in range(len(s)):
        d+=s[x]+","
    return d
        
    
print(main(1245))

