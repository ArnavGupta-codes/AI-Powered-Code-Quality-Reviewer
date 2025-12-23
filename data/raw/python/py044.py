"""
Sample Python file py044 for the ML code review dataset.
"""

def compute_value(n):
    total = 0
    for i in range(n):
        total += i * i
    return total


def main():
    result = compute_value(47)
    print("Result for py044:", result)


if __name__ == "__main__":
    main()
