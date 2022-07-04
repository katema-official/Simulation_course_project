# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math

def show_normal(mu, sigma):
    x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)
    plt.plot(x, stats.norm.pdf(x, mu, sigma))
    plt.show()

def obtain_infos_about_values(values_as_string):
    list_of_values = [int(x) for x in values_as_string.split(" - ")]
    values_and_probabilities = values_with_probabilities(list_of_values)
    #print(values_and_probabilities[0])
    #print(values_and_probabilities[1])
    mean = my_mean(values_and_probabilities[0], values_and_probabilities[1])
    var = variance(values_and_probabilities[0], values_and_probabilities[1])
    std_dev = math.sqrt(var)
    return (mean, var, std_dev)


def values_with_probabilities(l):
    final_values = []
    final_probabilities = []
    for elem in l:
        if elem not in final_values:
            final_values.append(elem)
            final_probabilities.append(1)
        else:
            idx = final_values.index(elem)
            final_probabilities[idx] += 1
    final_probabilities = [x/len(l) for x in final_probabilities]
    print(sum(final_probabilities))
    return (final_values, final_probabilities)

def my_mean(elems, probs):
    sum = 0
    for elem, prob in zip(elems, probs):
        sum += elem*prob
        #print(str(elem) + " " + str(prob) + " = " + str(elem*prob))
    #print("sum = " + str(sum))
    return sum

def variance(elemss, probss):
    #E[x^2] - (E[x])^2
    ret = my_mean([x**2 for x in elemss], probss) - (my_mean(elemss, probss)**2)
    return ret

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ret = obtain_infos_about_values("2000 - 2000 - 30 - 720 - 1100 - 1500 - 1500 - 500 - 45 - 500 - 1000 - 1000 - 600 - 1000 - 1000 - 959 - 300 - 200 - 400 - 1000 - 1500 - 895 - 350 - 1090 - 2000 - 500 - 1000 - 300 - 600 - 1500 - 2000 - 250 - 500 - 1100 - 630 - 1300 - 2000 - 900 - 350 - 750 - 150 - 800 - 500 - 500 - 2500")
    print("mean of standard withdrawals = " + str(ret[0]))
    print("variance of standard withdrawals = " + str(ret[1]))
    print("standard deviation is = " + str(ret[2]))
    show_normal(ret[0], ret[2])

    #examples of withdrawals from the "cassa servita"
    for i in range(10):
        w = -1
        while w <= 0:
            w = int(np.random.normal(ret[0], ret[2]))

            #bills_50 = w//50
            #bills_20 = (w - bills_50*50)//20 + 1

        # the sum to withdraw needs to be a multiple of 5
        w = (w // 5) * 5 + 5
        #we should also model the bills the cashier chooses to give to the customer.
        #My first thought is a normal with mean = 4 and a certain variance, such that it is
        #most likely that he chooses bills of 50, then of 20 and 100, then the rest.

        #w = bills_50*50 + bills_20*20
        print("customer " + str(i) + "th withdrawed " + str(w) + " euros")



    ret = obtain_infos_about_values("500 - 8010 - 7600 - 1200 - 1500 - 1000 - 400 - 340 - 500 - 780 - 500 - 1250 - 3700 - 1100 - 3000 - 2100 - 3000 - 1500 - 550 - 1700 - 2000 - 5000 - 1500 - 650 - 3080 - 300 - 3000 - 1900 - 800 - 3500 - 1050 - 100 - 1800 - 1640 - 2800 - 160 - 955 - 350 - 1100 - 750 - 3550 - 700 - 530")
    print("mean of standard withdrawals = " + str(ret[0]))
    print("variance of standard withdrawals = " + str(ret[1]))
    print("standard deviation is = " + str(ret[2]))
    show_normal(ret[0], ret[2])

    for i in range(10):
        w = -1
        while w <= 0:
            w = int(np.random.normal(ret[0], ret[2]))
            bills_50 = w//50
            bills_20 = (w - bills_50*50)//20 + 1

        w = bills_50*50 + bills_20*20
        print("customer " + str(i) + "th withdrawed " + str(w) + " euros")


