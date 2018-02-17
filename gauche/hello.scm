;; gauche, scheme processor

(print (+ 1 2)) ; 3

(print '(+ 1 2)) ; (+ 1 2)

;; global definition
(define x 3)
(print x) ; 3

(print (quote x)) ; x

(print (quote 'x)) ; 'x

(print (and (= 2 2) (> 2 1))) ; #t

(print (or (> 2 2) '(a b))) ; (a b)

;; condition control statement
(print (cond ((> 3 2) 'greater)
             ((< 3 2) 'less))) ; greater

;; case statement
(print (case (* 2 3)
         ((2 3 5 7) 'prime)
         ((1 4 6 8 9) 'composite))) ; composite

(print (case (car '(c d))
         ((a e i o u) 'vowel)
         ((w y) 'semivowel)
         (else 'consonant))) ; consonant

;; local definition
(let ((x 2) (y 3))
  (print (* x y))) ; 6

(let ((x 2) (y 3)) ; x = 2, y = 3
  (let ((x 7) (z (+ x y))) ; x = 7, y = 3, z = 5
    (print (* z x)))) ;; 35

(define x 3)
(define y 4)
(let ((x 5) (y (+ x 1))) (print y)) ; 4
(let* ((x 5) (y (+ x 1))) (print y)) ; 6

;; local recursive definition
(letrec ((even?
           (lambda (n)
             (if (zero? n)
               #t
               (odd? (- n 1)))))
         (odd?
           (lambda (n)
             (if (zero? n)
               #f
               (even? (- n 1))))))
  (print (even? 3872))
  (print (odd? 3265)))

;; global definition
(define (hard-even? x)
  (define (even? n)
    (if (zero? n)
      #t
      (odd? (- n 1))))
  (define (odd? n)
    (if (zero? n)
      #t
      (even? (- n 1))))
  (even? x))

(print (hard-even? 10))

;; arithmetic calcilation
(print (- (quotient (* (+ 3 7 10) (- 1000 8)) 992) 17))

(print (remainder 27 4))

(print (not (= 15 14)))

;; list
(print (cons 'a 'b)) ; (a . b)

(print (list 'a 'b )) ; (a b)

(print (cons 'a (cons 'b '()))) ; (a b)

(print (car (cons 'a 'b))) ; a

(print (cdr (cons 'a 'b))) ; b

(print (cdr (list 'a 'b))) ; (b)

(print (cadr '(a b))) ; (car (cdr '(a b))) ; b

(print (list-tail '(a b c) 0)) ; (a b c)

(print (list-tail '(a b c) 1)) ; (b c)

(print (list-tail '(a b c) 2)) ; (c)

(print (list-tail '(a b c) 3)) ; ()

; (print (list-tail '(a b c) 4)) ; error

(print (list-ref '(a b c) 0)) ; a

(print (append '(a b) '(c d) '() '(e))) ; (a b c d e)

(define L1 (list 'a 'b 'c))
(define L2 (list 'd))
(define L3 (append L1 L2)) ; L1 part is fixed in this line
(set-car! L1 1)
(print L1) ; (1 b c)
(set-car! L2 2)
(print L2) ; (2)
(print L3) ; (a b c 2) ; only L2 part is changed

(print (null? '())) ; #t

(print (list? '(a b))) ; #t

(print (list? '(a . b))) ; #f

;; equivalence
(print (eqv? 'a 'a)) ; #t

(print (eqv? 'a 'b)) ; #f

(print (eqv? 100 (+ 50 50))) ; #t

(print (eqv? (list 'a 'b) (list 'a 'b))) ; #f

(print (equal? (list 'a 'b) (list 'a 'b))) ; #t

;; types
(print (boolean? #f))

(print (integer? 3))

(print (pair? '(a b)))

(print (null? '()))

(print (symbol? 'a))

(print (procedure? +))
; all evaled to be #t

;; evaluation
(print (apply cons '(1 2))) ; (1 . 2)

(print (apply + 1 2 '(3 4 5))) ; 15

; In Gauche, the second argument of `eval` is needed
; which means environment specifier
(eval '(+ 1 2) (interaction-environment))
