from .. import my_class
from .. import my_package
from .. import sicp

def main_process():
    #  create MyMath instance named hoge
    #  hoge = my_package.MyMath()

    #  create Account instance named ac
    #  ac = my_package.Account("spam")

    #  create CheckingAccount instance
    #  chac = my_package.CheckingAccount("foo")

    #  create CampaignAccount instance
    #  camac = my_package.CampaignAccount("HOGEEEEE")

    """
    some process written below
    """

    #  hoge.sum_cubes(12)
    #  hoge.print_num()

    #  hoge.pi_sum(100000)
    #  hoge.print_num()

    #  hoge.iter_improve(my_package.golden_update, my_package.golden_test)
    #  hoge.print_num()

    #  hoge.square_root(256)
    #  hoge.print_num()

    #  hoge.compose(hoge.square, hoge.successor, 12)
    #  hoge.print_num()

    #  hoge.fn_square_root(256)
    #  hoge.print_num()

    #  hoge.logarithm(32)
    #  hoge.print_num()

    #  hoge.triple(2376)
    #  hoge.print_num()

    #  hoge.sum_even_fibs(50)
    #  hoge.print_num()

    #  hoge.product_even_fibs(30)
    #  hoge.print_num()

    #  print(ac.holder)

    #  ac.deposit(100)
    #  print(ac.balance)
    #  ac.withdraw(10)
    #  print(ac.balance)
    #  print(ac.withdraw(150))
    #  print(ac.balance)

    #  print(getattr(ac, 'balance'))
    #  print(hasattr(ac, 'balance'))

    #  ac.status()

    #  print(ac.interest)

    #  chac.deposit(100)
    #  chac.withdraw(50)
    #  print(chac.balance)

    #  print(camac.balance)
    #  camac.deposit(20)
    #  print(camac.balance)
    #  camac.withdraw(10)
    #  print(camac.balance)

    #  camac.show_inheritance()

    """
    my class modules
    """

    #  # make class
    #  Account = my_class.make_account_class()
    #  # make instance
    #  furuhama_account = Account['new']('furuhama')

    #  # show details
    #  print(furuhama_account['get']('holder'))
    #  print(furuhama_account['get']('interest'))
    #  print(furuhama_account['get']('deposit')(20))
    #  print(furuhama_account['get']('withdraw')(5))

    #  # get unexist variable
    #  print(furuhama_account['get']('hoge'))

    #  CheckingAccount = my_class.make_checking_account_class()
    #  f_account = CheckingAccount['new']('f')
    #  print(f_account['get']('holder'))
    #  print(f_account['get']('interest'))
    #  print(f_account['get']('deposit')(20))
    #  print(f_account['get']('withdraw')(5))

    #  from math import pi
    #  print(my_class.add_complex(my_class.ComplexRI(1, 2), my_class.ComplexMA(2, pi / 2)))
    #  print(my_class.mul_complex(my_class.ComplexRI(0, 1), my_class.ComplexRI(0, 1)))

    #  define operators
    #  print(my_class.ComplexRI(1, 2) + my_class.ComplexMA(2, 0))
    #  print(my_class.ComplexRI(0, 1) * my_class.ComplexRI(0, 1))

    #  print(my_class.iscomplex(my_class.ComplexMA(1, 1)))

    #  print(sicp.counting_change(100))

    #  norm = sicp.normal_exp(2, 20)
    #  itr = sicp.iter_exp(2, 20)
    #  fast = sicp.fast_exp(2, 20)

    #  print(norm, itr, fast)

    #  s = sicp.Rlist(1, sicp.Rlist(2, sicp.Rlist(3)))

    #  print(s.rest)
    #  print(len(s))
    #  print(s[1])

    #  t = sicp.extend_rlist(s.rest, s)
    #  print(t)

    #  print(sicp.map_rlist(s, sicp.square))

    #  print(sicp.filter_rlist(s, lambda x: x % 2 == 1))

    #  tree = ((1, 2), 3, 4)
    #  print(sicp.count_leaves(tree))

    #  big_tree = ((tree, tree), 5)
    #  print(sicp.count_leaves(big_tree))

    #  sq_big_tree = sicp.map_tree(big_tree, sicp.square)
    #  sq_sq_big_tree = sicp.map_tree(sq_big_tree, sicp.square)
    #  print(sq_sq_big_tree)

    #  print(sicp.fib_tree(1))
    #  print(sicp.fib_tree(2))
    #  print(sicp.fib_tree(3))
    #  print(sicp.fib_tree(4))
    #  print(sicp.fib_tree(5))
    #  print(sicp.fib_tree(6))

    #  s = sicp.Rlist(1, sicp.Rlist(2, sicp.Rlist(3)))
    #  print(sicp.set_contains(s, 2))
    #  print(sicp.set_contains(s, 5))

    #  t = sicp.adjoin_set(s, 4)
    #  print(t)

    #  inter_s = sicp.intersect_set(t, sicp.map_rlist(s, sicp.square))
    #  print(inter_s)

    #  union_s = sicp.union_set(t, s)
    #  print(union_s)

    #  sicp.basic_error()
    #  sicp.try_div_zero()
    #  print(sicp.invert_safe(0))

    #  e = sicp.Exp('add', [1, 2])
    #  print(e)

    #  print(sicp.calc_eval(e))

    #  sicp.read_eval_print_loop()

    #  sicp.range_print()

    #  letters = sicp.Letters()
    #  print(letters.__next__())
    #  print(letters.__next__())
    #  print(letters.__next__())
    #  print(letters.__next__())
    #  print(letters.__next__()) # raise error

    #  sicp.counting()
    #  sicp.count_by_iter()

    #  sicp.letters_generation()

    #  sicp.generate_all_pairs()

    #  sicp.using_stream()

    sicp.using_coroutine()
