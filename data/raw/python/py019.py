"""
Sample Python file py019 for the ML code review dataset.
"""

def compute_value(n):
    total = 0
    for i in range(n):
        total += i * i
    return total


def main():
    result = compute_value(22)
    print("Result for py019:", result)


if __name__ == "__main__":
    main()
