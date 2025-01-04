def mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def median(numbers):
    if not numbers:
        return 0
    numbers.sort()
    midpoint = len(numbers) // 2
    if len(numbers) % 2 == 1:
        return numbers[midpoint]
    else:
        return (numbers[midpoint] + numbers[midpoint - 1]) / 2

def mode(numbers):
    if not numbers:
        return 0
    theDictionary = {}
    for number in numbers:
        count = theDictionary.get(number, None)
        if count is None:
            theDictionary[number] = 1
        else:
            theDictionary[number] = count + 1
    theMaximum = max(theDictionary.values())
    modes = [key for key, value in theDictionary.items() if value == theMaximum]
    return modes

def main():
    numbers = input("Enter a list of numbers separated by commas: ").split(',')
    numbers = [float(num) for num in numbers]
    print(f"Mean: {mean(numbers)}")
    print(f"Median: {median(numbers)}")
    print(f"Mode: {mode(numbers)}")

if __name__ == "__main__":
    main()