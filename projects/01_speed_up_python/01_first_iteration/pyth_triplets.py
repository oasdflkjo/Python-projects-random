import time

# funnction that finds out pythagorian triplets
# ie 3 4 5 and 5 12 13 and so on
# using this as an example of "costly function"
# that needs some speeding up


def count_triplets(limit):
    result = 0
    for a in range(1, limit + 1):
        for b in range(a+1, limit + 1):
            for c in range(b+1, limit + 1):
                if c*c > a*a + b * b:
                    break
                if c*c == (a*a + b * b):
                    result += 1
    return result


if __name__ == '__main__':
    start = time.time()
    result = count_triplets(1000)
    duration = time.time() - start
    print(result, duration)
