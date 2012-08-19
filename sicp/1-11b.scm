(define (f n)
 (if (= n 1)
  1 
  (f-iter n 2 1 0 )))

(define (f-iter n n1 n2 n3)
  (if (< n 3)
    n1
    (f-iter (- n 1) (+ n1 (* 2 n2) (* 3 n3)) n1 n2)))

(f 1)
(f 2)
(f 3)
(f 4)
(f 5)
