import random
import matplotlib.pyplot as plt

class morris_counter_v3:
    def __init__(self,a):
        self.c = 0
        self.morris_array = [0]
        self.a =a

    def insert(self):
        probability = random.random()
        if probability<= 1/(self.a** self.c):
            self.c = self.c+1
        return
    
    def query(self):
        if self.a==1:
            return self.c
        return ((1/(self.a-1))*(self.a** self.c -1))
    
    def run_morris_counter(self,num_of_repetitions):
        for _ in range(num_of_repetitions):
            self.insert()
            self.morris_array.append(self.query())
        return 
    
    def morris_graph(self):
        my_line = []
        for i in range(len(self.morris_array)):
            my_line.append(i)
        plt.figure(figsize=(10, 6))
        plt.plot(self.morris_array, label='approx counter value',color = "orange")
        plt.plot(my_line,color = "blue")
        plt.ylabel("Counter Values")
        plt.legend()
        plt.show()
        return