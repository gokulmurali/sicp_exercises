
(define (pascal row column)
  (cond ((> column row) 0)
	((= column 1) 1)
	((+ (pascal (- row 1) (- column 1))
	    (pascal (- row 1) column))

    )))

(pascal 1 1)
(pascal 2 2)
(pascal 3 2)
(pascal 5 3)
(pascal 5 4)
(pascal 4 4)
(pascal 4 5)
