import py_compile


def main(n):
    """
    Return numbers from zero to n in a list view.
    Args:
        n: int
    Returns:
        list: return  answer
    """
    s=[]
    for x in range(n):
        s.append(x)
    return s
print(main(6))