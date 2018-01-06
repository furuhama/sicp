"""
main script
"""

# from src import mymath
from src import myabstract


def main():
    """
    main function
    """
    result = myabstract.pi_sum(1000000)
    print(result)
    return 0


if __name__ == '__main__':
    main()
