# Least Square Method
Short python library that implements least square method.
```python
import lsm

def main():
    print(lsm.LeastSquareMethod([1,2,3],[4,7,10],[lambda x:x**2, lambda x:x, lambda x:1]))
    return 0

main()
```
```python
Output: [-0.  3.  1.]
```
u - vector of u variables <br/>
y - vector of y results <br/>
fi - vector of fi(u) functions that will be used in approximation of system mathematica model.
