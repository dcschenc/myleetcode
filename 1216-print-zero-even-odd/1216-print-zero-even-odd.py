from threading import Semaphore
class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.z = Semaphore(1)
        self.e = Semaphore(0)
        self.o = Semaphore(0)

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            self.z.acquire()
            printNumber(0)
            if i % 2 == 0:
                self.o.release()
            else:
                self.e.release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1, 2):
            self.e.acquire()
            printNumber(i)
            self.z.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
            self.o.acquire()
            printNumber(i)
            self.z.release()
            
    # def __init__(self, n):
    #     self.n = n
    #     self.zero = Semaphore(1)
    #     self.odd = Semaphore(0)
    #     self.even = Semaphore(0)        
        
	# # printNumber(x) outputs "x", where x is an integer.
    # def zero(self, printNumber: 'Callable[[int], None]') -> None:
    #     for i in range(self.n):
    #         self.zero.acquire()
    #         printNumber(0)
    #         if i % 2 == 0:
    #             self.odd.release()
    #         else:
    #             self.even.release()

    # def odd(self, printNumber: 'Callable[[int], None]') -> None:
    #     for i in range(1, self.n, 2):
    #         self.odd.acquire()
    #         printNumber(i)  
    #         self.zero.release()      
        
    # def even(self, printNumber: 'Callable[[int], None]') -> None:
    #     for i in range(2, self.n, 2):
    #         self.even.acquire()
    #         printNumber(i)
    #         self.zero.release()
        
        

        