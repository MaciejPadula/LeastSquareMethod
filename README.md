# Least Square Method
Short python library that implements least square method.
```python
import lsm

def main():
    print(lsm.LeastSquareMethod([1,2,3],[4,7,10],[lambda x:x**2, lambda x:x, lambda x:1]))
    return 0

main()
```
First argument is vector of u variables. Second argument is vector of y results. Last argument is vector of functions that we want to use in our mathematical model.
