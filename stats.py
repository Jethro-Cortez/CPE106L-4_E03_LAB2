# stats.py

def mean(numbers):
    """Calculates the mean of a list of numbers."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def median(numbers):
    """Calculates the median of a list of numbers."""
    if not numbers:
        return 0
    numbers.sort()
    midpoint = len(numbers) // 2
    if len(numbers) % 2 == 1:
        return numbers[midpoint]
    else:
        return (numbers[midpoint] + numbers[midpoint - 1]) / 2

def mode(numbers):
    """Calculates the mode of a list of numbers."""
    if not numbers:
        return 0
    frequency = {}
    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1
    max_frequency = max(frequency.values())
    modes = [key for key, val in frequency.items() if val == max_frequency]
    # Return the first mode if there are multiple modes
    return modes[0] if modes else 0

def main():
    """Tests the mean, median, and mode functions."""
    test_numbers = [1, 2, 2, 3, 4, 5, 5, 5]
    print(f"Numbers: {test_numbers}")
    print(f"Mean: {mean(test_numbers)}")
    print(f"Median: {median(test_numbers)}")
    print(f"Mode: {mode(test_numbers)}")

if __name__ == "__main__":
    main()
