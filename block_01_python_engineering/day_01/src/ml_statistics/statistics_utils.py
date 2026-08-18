def _validate_values(values: list[float | int]) -> None:
    """Validate that values is non-empty and contains only int or float values.

    Raises:
        ValueError: If the list is empty.
        TypeError: If any value is not an int or float.
    """
    if not values:
        raise ValueError("The list of values is empty.")

    if not all(type(x) in (int, float) for x in values):
        raise TypeError("All values in the list must be numbers.")


def calculate_mean(values: list[float | int]) -> float:
    """Calculate the arithmetic mean of the values."""
    _validate_values(values)
    return sum(values) / len(values)


def calculate_median(values: list[float | int]) -> float:
    """Calculate the median of the values."""
    _validate_values(values)

    sorted_values = sorted(values)
    n = len(sorted_values)

    if n % 2 == 1:
        return float(sorted_values[n // 2])

    mid1 = sorted_values[n // 2 - 1]
    mid2 = sorted_values[n // 2]
    return float((mid1 + mid2) / 2)


def calculate_min(values: list[float | int]) -> float:
    """Calculate the smallest value."""
    _validate_values(values)
    return float(min(values))


def calculate_max(values: list[float | int]) -> float:
    """Calculate the largest value."""
    _validate_values(values)
    return float(max(values))


def calculate_range(values: list[float | int]) -> float:
    """Calculate the difference between the largest and smallest values."""
    _validate_values(values)
    return float(max(values) - min(values))
