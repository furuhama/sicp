;; basic factorial

(define (factorial n)
  (if (= n 1)
    1
    (* n (factorial (- n 1)))))

;; tail recursion

(define (t-fact n)
  (define (fact-iter prod count max-count)
    (if (> count max-count)
      prod
      (fact-iter (* count prod)
                 (+ count 1)
                 max-count)))
  (fact-iter 1 1 n))

;; main process

(print (factorial 10))

(print (t-fact 10))
