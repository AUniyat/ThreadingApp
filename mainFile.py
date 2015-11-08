__author__ = 'ALEX'
#A simple app that takes in one input from the user and checks whether the number is a prime number or not
#The app itself is made using threading, there is one thread that checks if the input number is a prime
import threading

#A class that checks is a number is a prime or not
class PrimeNumber(threading.Thread):
    def __init__(self, number):
        threading.Thread.__init__(self)
        self.Number = number

    def run(self):
        cont = True
        while cont == True :
            for i in range(2, self.Number):
                if (self.Number % i) == 0:
                    print " %d is not a prime number" % self.Number
                    return

            else:
                print "%d is a prime number" % self.Number
                return



#a list of threads is made
threads = []
#A loop that runs as long as the user enters a number that is 1 or larger
while True:
    try:
        input = long(raw_input("number: "))
    except:
        print "Please enter a number"
        continue
    if input < 1:
        break

    #a thread is made when a user inputs a number
    thread = PrimeNumber(input)
    threads += [thread]
    #the thread starts
    thread.start()

for x in threads:
    x.join()
