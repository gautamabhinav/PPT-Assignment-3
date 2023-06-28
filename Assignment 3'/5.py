def plusOne(digits):
    n = len(digits)
    carry = 1  # Start with a carry of 1 to increment the least significant digit

    for i in range(n - 1, -1, -1):
        digits[i] += carry
        carry = digits[i] // 10
        digits[i] %= 10

        # If there is no carry, we can stop the iteration
        if carry == 0:
            break

    # If there is still a carry after the loop, we need to insert a new digit
    if carry == 1:
        digits.insert(0, 1)

    return digits

# Example usage
digits = [1, 2, 3]
result = plusOne(digits)
print(result)
