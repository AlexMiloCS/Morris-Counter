import math
import matplotlib as plt

class morris_probabilities:
    def __init__(self,n_max, k_max):
        self.P = []
        for n in range(n_max + 1):
            row = []
            for k in range(k_max + 2):
                row.append(0.0)
            self.P.append(row)
        self.P[1][1] = 1.0 
        for n in range(2, n_max + 1):
            for k in range(1, k_max + 1):
                self.P[n][k] = self.P[n-1][k-1] * (1 / (2 ** (k - 1))) + self.P[n-1][k] * (1 - 1 / (2 ** k))

    def get_probability(self,n,k):
        return self.P[n][k]
    
    def get_p(self):
        return self.P
    
    def get_all_probabilities(self,k):
        probability_dict = {}
        for i in range(1, 1001):
            probability_dict[i] = self.P_table[i][k]
        return probability_dict
    
    def plot_results(self,dict):
        plt.figure(figsize=(10, 6))
        plt.plot(list(dict.values()))
        plt.xlabel("n")
        plt.ylabel("Probability")
        plt.grid(True)
        plt.show()

    
    