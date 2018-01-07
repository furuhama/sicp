"""
main script
"""

# from src import mymath
# from src import myabstract
from src import myimprove


def main():
    """
    main function
    """
    result = myimprove.iter_improve(
        myimprove.golden_update, myimprove.golden_test)
    print(result)
    return 0


if __name__ == '__main__':
    main()
