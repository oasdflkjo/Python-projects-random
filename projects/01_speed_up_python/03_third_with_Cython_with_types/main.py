import pyth_triples
import time


def main():
    start = time.time()
    result = pyth_triples.count_triplets(1000)
    duration = time.time() - start
    print(result, duration)


if __name__ == '__main__':
    main()
