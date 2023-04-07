def digit_sum(n):
    """Helper function to compute the sum of digits of a number."""
    return sum(int(d) for d in str(n))

def max_winners(n):
    """Returns the number of values of s where the prize is split among most people."""
    counts = [0] * (n+1)  # initialize counts of winners for each possible value of s
    for i in range(1, n+1):
        counts[digit_sum(i)] += 1  # increment count for the sum of digits of each coupon
    max_count = max(counts)  # find the largest number of winners
    return counts.count(max_count)  # count the number of possible values of s with max_count winners

n = 30
print(max_winners(n))  
