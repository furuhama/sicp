"""
main script
"""

from src import my_package


def main():
    """
    main function
    """

    # create MyMath instance named hoge
    # hoge = my_package.MyMath()

    # create Account instance named ac
    ac = my_package.Account("spam")

    """
    some process written below
    """

    # hoge.sum_cubes(12)
    # hoge.print_num()

    # hoge.pi_sum(100000)
    # hoge.print_num()

    # hoge.iter_improve(my_package.golden_update, my_package.golden_test)
    # hoge.print_num()

    # hoge.square_root(256)
    # hoge.print_num()

    # hoge.compose(hoge.square, hoge.successor, 12)
    # hoge.print_num()

    # hoge.fn_square_root(256)
    # hoge.print_num()

    # hoge.logarithm(32)
    # hoge.print_num()

    # hoge.triple(2376)
    # hoge.print_num()

    # hoge.sum_even_fibs(50)
    # hoge.print_num()

    # hoge.product_even_fibs(30)
    # hoge.print_num()

    print(ac.holder)

    ac.deposit(100)
    print(ac.balance)
    ac.withdraw(10)
    print(ac.balance)
    print(ac.withdraw(150))
    print(ac.balance)

    print(getattr(ac, 'balance'))
    print(hasattr(ac, 'balance'))


if __name__ == '__main__':
    main()
