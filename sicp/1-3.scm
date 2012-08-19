(define (square x)(* x x))

(define (sum-of-squares x y)(+ (square x)(square y)))

(sum-of-squares 2 3)

(define (great x y z)
  (if (and (<= x y) (<= x z)) 
    (sum-of-squares y z) 
      (if (and (<= y x) (<= y z)) 
	(sum-of-squares x z)
	  (if (and (<= z x)(<= z y))
	    (sum-of-squares x y)))))

		         

(great 4 3 2)  
(great 2 3 4)
(great 3 2 4)
(great 2 2 4)
(great 5 5 5)
