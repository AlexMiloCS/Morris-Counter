import random
import matplotlib.pyplot as plt

class morris_counter:
    def __init__(self):
        self.c = 0
        self.morris_array = [0]

    def insert(self):
        probability = random.random()
        if probability<= 1/(2** self.c):
            self.c = self.c+1
        return
    
    def query(self):
        return (2** self.c -1)
    
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