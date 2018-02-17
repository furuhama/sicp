#lang racket

(define
    (display_bool bool x y)
    (if bool
        (display x)
        (display y)
    )
    (newline)
)

(display_bool #f "piyo" "piyopiyo")

(display_bool (> 10 5) "piyo" "piyopiyo")
