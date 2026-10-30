# Mean-Variance-Standard Deviation Calculator

A small Python project from the freeCodeCamp **Data Analysis with Python** certification, completed as part of my Master's in Business Analytics at the University of Oulu.

## What it does

`calculate()` takes a list of 9 numbers, turns it into a 3×3 matrix with NumPy, and returns the **mean, variance, standard deviation, max, min and sum**:

- along each **column** (axis 0)
- along each **row** (axis 1)
- for the **whole matrix**

If the list does not contain exactly 9 numbers, it raises `ValueError: List must contain nine numbers.`

## Example

```python
import mean_var_std
mean_var_std.calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
```

```
{
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  'variance': [[6.0, 6.0, 6.0], [0.6667, 0.6667, 0.6667], 6.6667],
  'standard deviation': [[2.4495, 2.4495, 2.4495], [0.8165, 0.8165, 0.8165], 2.5820],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],
  'sum': [[9, 12, 15], [3, 12, 21], 36]
}
```

(values rounded here for readability)

## How to run

```bash
pip install numpy
python main.py        # prints the example and runs the unit tests
```

## Files

| File | Purpose |
|------|---------|
| `mean_var_std.py` | The `calculate()` function |
| `main.py` | Runs an example and the tests |
| `test_module.py` | Unit tests (3 tests, all passing) |

## Skills practised

Python · NumPy arrays and reshaping · axis-based aggregation · descriptive statistics · error handling · unit testing
