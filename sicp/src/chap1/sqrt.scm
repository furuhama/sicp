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

;; refactor improvement process
;; evaluate guess number by ratio

(define (square-root x)
  (define (sqrt-iter guess x)
    (define (good-enough? guess x)
      (< (/ (abs (- ((lambda (x) (* x x)) guess) x)) x) 0.001))

    (define (improve guess x)
      ((lambda (x y) (/ (+ x y) 2)) guess (/ x guess)))

    (if (good-enough? guess x)
      guess
      (sqrt-iter (improve guess x) x)))
  (sqrt-iter 1.0 x))

;; main process

(print (sqrt 9))
(print (square-root 9))

(print (sqrt 90000001))
(print (square-root 90000001))

;; in this pattern, results are really different
;; (square-root is the better way)
(print (sqrt 0.00001))
(print (square-root 0.00001))
