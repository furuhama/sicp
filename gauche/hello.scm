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

; local recursive definition
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
