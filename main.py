"""
main script
"""

from src import my_package
# from src import myimprove


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

    # result = myimprove.iter_improve(
    #     myimprove.golden_update, myimprove.golden_test)
    # print(result)
    return 0


if __name__ == '__main__':
    main()
