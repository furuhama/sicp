"""
main script
"""

# from src import my_package
from src import my_class


def main():
    """
    main function
    """

    # create MyMath instance named hoge
    # hoge = my_package.MyMath()

    # create Account instance named ac
    # ac = my_package.Account("spam")

    # create CheckingAccount instance
    # chac = my_package.CheckingAccount("foo")

    # create CampaignAccount instance
    # camac = my_package.CampaignAccount("HOGEEEEE")

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

    # print(ac.holder)

    # ac.deposit(100)
    # print(ac.balance)
    # ac.withdraw(10)
    # print(ac.balance)
    # print(ac.withdraw(150))
    # print(ac.balance)

    # print(getattr(ac, 'balance'))
    # print(hasattr(ac, 'balance'))

    # ac.status()

    # print(ac.interest)

    # chac.deposit(100)
    # chac.withdraw(50)
    # print(chac.balance)

    # print(camac.balance)
    # camac.deposit(20)
    # print(camac.balance)
    # camac.withdraw(10)
    # print(camac.balance)

    # camac.show_inheritance()

    """
    my class modules
    """

    # make class
    Account = my_class.make_account_class()
    # make instance
    furuhama_account = Account['new']('furuhama')

    # show details
    print(furuhama_account['get']('holder'))
    print(furuhama_account['get']('interest'))
    print(furuhama_account['get']('deposit')(20))
    print(furuhama_account['get']('withdraw')(5))

    # get unexist variable
    print(furuhama_account['get']('hoge'))


if __name__ == '__main__':
    main()
