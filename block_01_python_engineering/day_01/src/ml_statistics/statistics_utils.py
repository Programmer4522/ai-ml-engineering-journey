def _validate_values(values : list[float | int]) -> None:
    """
    Validates the numbers in the list.
    
    Parameters:
    values (list[float | int]): A list of numerical values.
    
    Returns:
    None: It just verifies and doesn't return anything.

    Raises:
    ValueError: If the list of values is empty.
    TypeError: If any value in the list is not a number.

    >>> _validate_values([])
    Traceback (most recent call last):
    ...
    ValueError: The list of values is empty.

    >>> _validate_values([1.0, 2.0, "3.0", 4.0, 5.0])
    Traceback (most recent call last):
    ...
    TypeError: All values in the list must be numbers.
    """
    
    if not values:
        raise ValueError("The list of values is empty.")
        
    if not all(type(x) in (int, float) for x in values):
        raise TypeError("All values in the list must be numbers.")
    
    # return None

def calculate_mean(values : list[float | int]) -> float:
    """
    Calculate and return the mean of the values in the list.
    
    Parameters:
    values (list[float | int]): A list of numerical values.
    
    Returns:
    float: The mean of the values in the list.
    
    Raises:
    ValueError: If the list of values is empty.
    TypeError: If any value in the list is not a number.
    
    Example:
    >>> calculate_mean([1.0, 2.0, 3.0, 4.0, 5.0])
    3.0
    
    >>> calculate_mean([])
    Traceback (most recent call last):
    ...
    ValueError: The list of values is empty.
    """
    
    _validate_values(values=values)
    
    return sum(values)/len(values)

def calculate_median(values : list[float | int]) -> float:
    """
    Calculate and return the median of the values in the list.
    
    Parameters:
    values (list[float | int]): A list of numerical values.
    
    Returns:
    float: The median of the values in the list.
    
    Raises:
    ValueError: If the list of values is empty.
    TypeError: If any value in the list is not a number.
    
    Example:
    >>> calculate_median([1.0, 2.0, 3.0, 4.0, 5.0])
    3.0
    
    >>> calculate_median([1.0, 2.0, 3.0, 4.0])
    2.5
    
    >>> calculate_median([])
    Traceback (most recent call last):
    ...
    ValueError: The list of values is empty.
    """
    
    _validate_values(values=values)
    
    sorted_values = sorted(values)
    n = len(sorted_values)
    
    if n % 2 == 1:
        return float(sorted_values[n // 2])
    else:
        mid1 = sorted_values[n // 2 - 1]
        mid2 = sorted_values[n // 2]
        return float((mid1 + mid2) / 2)

def calculate_min(values : list[float | int]) -> float:
    """
    Calculate and return the smallest value in the list.
    
    Parameters:
    values (list[float | int]): A list of numerical values.
    
    Returns:
    float: The smallest value in the list.
    
    Raises:
    ValueError: If the list of values is empty.
    TypeError: If any value in the list is not a number.
    
    Example:
    >>> calculate_min([1.0, 2.0, 3.0, 4.0, 5.0])
    1.0
    
    >>> calculate_min([])
    Traceback (most recent call last):
    ...
    ValueError: The list of values is empty.
    """
    
    _validate_values(values=values)
    
    return float(min(values))

def calculate_max(values : list[float | int]) -> float:
    """
    Calculate and return the largest value in the list.
    
    Parameters:
    values (list[float | int]): A list of numerical values.
                
    Returns:
    float: The largest value in the list.
                
    Raises:
    ValueError: If the list of values is empty.
    TypeError: If any value in the list is not a number.
                
    Example:
    >>> calculate_max([1.0, 2.0, 3.0, 4.0, 5.0])
    5.0
    
    >>> calculate_max([])
    Traceback (most recent call last):
    ...
    ValueError: The list of values is empty.
    """
    
    _validate_values(values=values)
    
    return float(max(values))

def calculate_range(values : list[float | int]) -> float:
    """
    Calculate and return the range of the values in the list.
    
    Parameters:
    values (list[float | int]): A list of numerical values.
                
    Returns:
    float: The range of the values in the list.
                
    Raises:
    ValueError: If the list of values is empty.
    TypeError: If any value in the list is not a number.
                
    Example:
    >>> calculate_range([1.0, 2.0, 3.0, 4.0, 5.0])
    4.0
    
    >>> calculate_range([])
    Traceback (most recent call last):
    ...
    ValueError: The list of values is empty.
    """
    
    _validate_values(values=values)
    
    return float(max(values)) - float(min(values))

values: list[float | int] = [1.0, 2.8, 3.3, 4, 5, 6.0, 7.4, 8.1, 9.0, 10]
# values: list[float | int] = ["hello", 'world']
# values: list[float | int] = []
# values: list[float| int] = [1, 2, 3, 4, 5]
print(sorted(values))

print(calculate_mean(values=values))
print(calculate_median(values=values))
print(calculate_min(values=values))
print(calculate_max(values=values))
print(calculate_range(values=values))