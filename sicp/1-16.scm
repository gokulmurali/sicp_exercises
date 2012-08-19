(define (fast-iter b n a)
  (cond ((= n 0) a)
	((even? n) (fast-iter (square b) (/ n 2) a))
	(else (fast-iter b (- n 1) (* a b))))
        )	

(define(fast b n)
  (fast-iter b n 1))


(fast 2 2)
(fast 2 3)
