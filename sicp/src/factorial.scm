;; factorial

(define (factorial n)
  (if (= n 1)
    1
    (* n (factorial (- n 1)))))

;; main process

(print (factorial 10))
