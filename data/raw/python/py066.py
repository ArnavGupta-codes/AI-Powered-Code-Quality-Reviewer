"""
Sample Python file py066 for the ML code review dataset.
"""

def compute_value(n):
    total = 0
    for i in range(n):
        total += i * i
    return total


def main():
    result = compute_value(69)
    print("Result for py066:", result)


if __name__ == "__main__":
    main()
