"""
main script
"""

# from src import mymath
from src import myabstract


def main():
    """
    main function
    """
    result = myabstract.sum_cubes(10)
    print(result)
    return 0


if __name__ == '__main__':
    main()
