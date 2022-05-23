import lsm

def main():
    print(lsm.LeastSquareMethod([1,2,3],[4,7,10],[lambda x:x**2, lambda x:x, lambda x:1]))
    return 0

main()