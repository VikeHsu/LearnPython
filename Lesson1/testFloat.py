import sys

def main():
    f1 = 1.0
    f2 = 0.0
    f3 = sys.float_info.max
    f4 = sys.float_info.min  # Smallest positive value
    inf = float('inf')

    print("Initial value of f1:", f1)

    # Add small increments to f1 to demonstrate precision loss
    for _ in range(1000000):
        f1 += 0.000001
    print("After 1,000,000 increments of 0.000001, f1:", f1)

    # Divide by zero to show infinity
    try:
        print("f1 / f2 (divide by zero):", f1 / f2)
    except ZeroDivisionError:
        print("f1 / f2 (divide by zero): ZeroDivisionError")

    # Show max and min values
    print("Maximum float value:", f3)
    print("Minimum positive float value:", f4)

    # Demonstrate overflow
    print("f3 * 2 (overflow):", f3 * 2)

    # Demonstrate underflow
    print("f4 / 2 (underflow):", f4 / 2)

    # Check infinity arithmetic
    print("inf + 1:", inf + 1)
    print("inf - inf:", inf - inf)  # This should result in NaN (not a number)

if __name__ == "__main__":
    main()