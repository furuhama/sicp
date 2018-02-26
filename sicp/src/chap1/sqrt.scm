;; define sqrt function

(define (sqrt x)
  (define (sqrt-iter guess x)
    (define (good-enough? guess x)
      ;; normal implementation

      ; (define (square x)
      ;   (* x x))
      ; (< (abs (- (square guess) x)) 0.001))

      ;; use lambda
      (< (abs (- ((lambda (x) (* x x)) guess) x)) 0.001))

    (define (improve guess x)
      ;; normal implementation

      ; (define (average x y)
      ;   (/ (+ x y) 2))
      ; (average guess (/ x guess)))

      ;; use lambda
      ((lambda (x y) (/ (+ x y) 2)) guess (/ x guess)))
    (if (good-enough? guess x)
      guess
      (sqrt-iter (improve guess x) x)))
  (sqrt-iter 1.0 x))

;; main process

(print (sqrt 9))
