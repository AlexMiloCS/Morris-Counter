import random
import matplotlib.pyplot as plt

class morris_counter_v2:
    def __init__(self, number_of_counters):
        self.number_of_counters = number_of_counters
        self.my_counters = {}
        self.my_morris_array_mean = []
        self.my_morris_array_median = []
        for i in range(number_of_counters):
            self.my_counters[i] = 0

    def insert(self , counter):
        probability = random.random()
        if probability< 1/(2** counter):
            counter = counter+1
        return counter
    
    def query_median(self):
        add_counters = 0
        for counter,value in self.my_counters.items():
            add_counters += value
        median_counter = add_counters/self.number_of_counters
        return (2**median_counter-1)
    
    def query_mean(self):
        add_counters = 0
        for counter,value in self.my_counters.items():
            add_counters += (2**value)
        return (add_counters-self.number_of_counters)/self.number_of_counters
    
    def run_morris_counter(self,num_of_repetitions):
        for _ in range(num_of_repetitions):
            for counter,value in self.my_counters.items():
                self.my_counters[counter] = self.insert(value)           
            self.my_morris_array_mean.append(self.query_mean())
            self.my_morris_array_median.append(self.query_median())
        return 
    
    def morris_graph(self):
        my_line = []
        for i in range(len(self.my_morris_array_mean)):
            my_line.append(i)
        plt.figure(figsize=(10, 6))
        plt.plot(self.my_morris_array_mean,color = "orange", label='Mean aprroximation')
        plt.plot(self.my_morris_array_median,color = "green", label='Median aprroximation')
        plt.plot(my_line,color = "blue")
        plt.legend()
        plt.show()
        return
    
    def get_results(self):
        mean = self.query_mean()
        median = self.query_median()
        return mean,median