(define (improveguess y x)
       (/ (+ (/ x (* y y)) (* 2 y)) 3))
    
(define (cube x) (* x x x))
    
(define (goodenough? guess x)
       (< (/ (abs (- (cube guess) x)) guess) 0.0001))
    
(define (cuberoot-iter guess x) 
           (if (goodenough? guess x) guess
                 (cuberoot-iter (improveguess guess x) x)))

(define (cuberoot x) (cuberoot-iter 1.0 x))
(cuberoot 8)

