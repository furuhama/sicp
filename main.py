"""
main script
"""

from src import my_package


def main():
    """
    main function
    """

    hoge = my_package.MyMath(0)
    # hoge
    hoge.sum_cubes(12)
    hoge.print_num()

    hoge.pi_sum(10000)
    hoge.print_num()

    hoge.iter_improve(my_package.golden_update, my_package.golden_test)
    hoge.print_num()


if __name__ == '__main__':
    main()
