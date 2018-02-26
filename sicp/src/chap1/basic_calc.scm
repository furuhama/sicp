;; define + operator

; basic recursion
(define (+ a b)
  (if (= a 0)
    b
    (inc (+ (dec a) b))))

; tail recursion
(define (+ a b)
  (if (= a 0)
    b
    (+ (dec a) (inc b))))
