"""
main script
"""

from src import my_package


def main():
    """
    main function
    """

    hoge = my_package.MyMath(0)
    hoge.add(10, 100)
    hoge.print_num()

    hoge.summation(20, hoge.cube, hoge.successor)
    hoge.print_num()

    hoge.sum_cubes(12)
    hoge.print_num()

    result = my_package.iter_improve(
        my_package.golden_update, my_package.golden_test)
    print(result)
    return 0


if __name__ == '__main__':
    main()
