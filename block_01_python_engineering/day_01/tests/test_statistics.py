import pytest
from ml_statistics.statistics_utils import (
    calculate_mean,
    calculate_median,
    calculate_min,
    calculate_max,
    calculate_range,
)


@pytest.mark.parametrize(
    "values, expected",
    [
        ([10, 20, 30], 20.0),
        ([1.5, 2.5, 3.5], 2.5),
        ([1, 2.6, 3], pytest.approx(2.2)),
        ([0.1, 0.2], pytest.approx(0.15)),
        ([-10, -5, 0, 5, 10], 0.0),
        ([1], 1.0),
        ([5, 5, 5, 5], 5.0),
    ],
)
def test_calculate_mean(values, expected):
    assert calculate_mean(values) == expected


@pytest.mark.parametrize(
    "values, expected",
    [
        ([10, 20, 30], 20.0),
        ([1.5, 2.5, 3.5], 2.5),
        ([1, 2.6, 3], 2.6),
        ([0.1, 0.2], pytest.approx(0.15)),
        ([-10, -5, 0, 5, 10], 0.0),
        ([1], 1.0),
        ([5, 5, 5, 5], 5.0),
    ],
)
def test_calculate_median(values, expected):
    assert calculate_median(values) == expected


@pytest.mark.parametrize(
    "values, expected",
    [
        ([10, 20, 30], 10.0),
        ([1.5, 2.5, 3.5], 1.5),
        ([1, 2.6, 3], 1),
        ([0.1, 0.2], 0.1),
        ([-10, -5, 0, 5, 10], -10.0),
        ([1], 1.0),
        ([5, 5, 5, 5], 5.0),
    ],
)
def test_calculate_min(values, expected):
    assert calculate_min(values) == expected


@pytest.mark.parametrize(
    "values, expected",
    [
        ([10, 20, 30], 30.0),
        ([1.5, 2.5, 3.5], 3.5),
        ([1, 2.6, 3], 3),
        ([0.1, 0.2], 0.2),
        ([-10, -5, 0, 5, 10], 10.0),
        ([1], 1.0),
        ([5, 5, 5, 5], 5.0),
    ],
)
def test_calculate_max(values, expected):
    assert calculate_max(values) == expected


@pytest.mark.parametrize(
    "values, expected",
    [
        ([10, 20, 30], 20.0),
        ([1.5, 2.5, 3.5], 2.0),
        ([1, 2.6, 3], 2.0),
        ([0.1, 0.2], 0.1),
        ([-10, -5, 0, 5, 10], 20.0),
        ([1], 0.0),
        ([5, 5, 5, 5], 0.0),
    ],
)
def test_calculate_range(values, expected):
    assert calculate_range(values) == expected


# ---------------------------------------
#   Input Validation Tests
# ---------------------------------------


@pytest.mark.parametrize(
    "function",
    [
        calculate_mean,
        calculate_median,
        calculate_min,
        calculate_max,
        calculate_range,
    ],
)
def test_empty_values(function):
    with pytest.raises(ValueError):
        function([])


@pytest.mark.parametrize(
    "function",
    [
        calculate_mean,
        calculate_median,
        calculate_min,
        calculate_max,
        calculate_range,
    ],
)
@pytest.mark.parametrize(
    "values",
    [
        [1, "hello", 3],
        [1, True, 3],
    ],
)
def test_invalid_type(function, values):
    with pytest.raises(TypeError):
        function(values)
