(define (double x)
  (+ x x))
(define (halve x)
  (/ x 2))

(define (* a b)
  (define (*iter a b 0)))

(define (*iter a b aa)  
  (cond ((= b 0) aa)
	((even? b) (*iter (double a) (halve b) aa)))
	(else (*iter a (- b 1) (+ aa a))
	
	))

  (* 2 3)
  (* 2 4)

