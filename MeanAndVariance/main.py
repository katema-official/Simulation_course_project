# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math
import numpy.random as random



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


def show_normal(mu, sigma):
    x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)
    plt.plot(x, stats.norm.pdf(x, mu, sigma))
    plt.show()

def sample_mean(samples):
    l = [int(x) for x in samples.split(" - ")]
    return sum(l)/len(l)

def sample_variance(samples, samp_mean):
    l = [int(x) for x in samples.split(" - ")]
    s = 0
    for i in range(len(l)):
        s += (l[i] - samp_mean)**2
    return s / (len(l) - 1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    """
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
    print("mean of standard deposits = " + str(ret[0]))
    print("variance of standard deposits = " + str(ret[1]))
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
    """

    #-------------------------------------------------------------------------------------
    #----------------------Served register: Withdrawals and Deposits----------------------
    #-------------------------------------------------------------------------------------

    #study of the samples given by observing withdrawals from the served register
    print("-----------------Served register: Withdrawals and Deposits-----------------")
    samples_served_register_withdrawals = "2000 - 2000 - 30 - 720 - 1100 - 1500 - 1500 - 500 - 45 - 500 - 1000 - 1000 - 600 - 1000 - 1000 - 959 - 300 - 200 - 400 - 1000 - 1500 - 895 - 350 - 1090 - 2000 - 500 - 1000 - 300 - 600 - 1500 - 2000 - 250 - 500 - 1100 - 630 - 1300 - 2000 - 900 - 350 - 750 - 150 - 800 - 500 - 500 - 2500"
    X_signed = sample_mean(samples_served_register_withdrawals)
    print("sample mean of withdrawals = " + str(X_signed))
    S_squared = sample_variance(samples_served_register_withdrawals, X_signed)
    S = math.sqrt(S_squared)
    print("sample variance of withdrawals = " + str(S_squared) + ", standard deviation = " + str(S))
    #show_normal(X_signed, S)

    #study of the samples given by observing deposits from the served register
    samples_served_register_deposits = "500 - 8010 - 7600 - 1200 - 1500 - 1000 - 400 - 340 - 500 - 780 - 500 - 1250 - 3700 - 1100 - 3000 - 2100 - 3000 - 1500 - 550 - 1700 - 2000 - 5000 - 1500 - 650 - 3080 - 300 - 3000 - 1900 - 800 - 3500 - 1050 - 100 - 1800 - 1640 - 2800 - 160 - 955 - 350 - 1100 - 750 - 3550 - 700 - 530"
    X_signed = sample_mean(samples_served_register_deposits)
    print("sample mean of deposits = " + str(X_signed))
    S_squared = sample_variance(samples_served_register_deposits, X_signed)
    S = math.sqrt(S_squared)
    print("sample variance of deposits = " + str(S_squared) + ", standard deviation = " + str(S))
    #show_normal(X_signed, S)

    #We also mention that, from some samples, we have measured that the customers that go to the served register
    #to carry out an operation have a 70% probability of doing a withdrawal and a 30% probability of doing a deposit.
    #Also, on average, the number of customers that use the served register daily are 40.

    # -------------------------------------------------------------------------------------
    # --------------------------------Withdrawals register---------------------------------
    # -------------------------------------------------------------------------------------
    print("-----------------Withdrawals register-----------------")
    #the following data are all from a solar day

    samples_withdrawals_register = "100 - 100 - 50 - 200 - 250 - 250 - 500 - 200 - 250 - 500 - 50 - 100 - 2000 - 500 - 100 - 200 - 100 - 150 - 50 - 500 - 150 - 250 - 500 - 250 - 500 - 500 - 500 - 50 - 100 - 300 - 400 - 350 - 100 - 1000 - 50 - 250 - 500 - 100 - 500 - 250 - 200 - 500 - 500 - 50 - 100 - 50 - 150 - 500 - 250 - 40 - 440 - 210 - 420 - 150 - 600 - 150 - 250 - 250 - 500 - 500 - 500 - 500 - 500 - 500 - 500 - 370 - 150 - 500 - 40 - 900 - 200 - 300 - 50 - 150 - 950 - 100 - 700 - 100 - 250 - 250 - 1000 - 150 - 5000 - 1000 - 200 - 50 - 50 - 250 - 500 - 100 - 150 - 500 - 150 - 500 - 100 - 250 - 400 - 350 - 250 - 150 - 100 - 1000 - 1000 - 650 - 250 - 200 - 50 - 300 - 800 - 200 - 200 - 200 - 150 - 1000 - 150 - 150 - 250 - 250 - 500 - 250 - 1000 - 200 - 250 - 800 - 200 - 250 - 250 - 200 - 150 - 300 - 150 - 500 - 500 - 500 - 250 - 1000 - 250 - 50 - 150 - 150 - 100 - 250 - 150 - 50 - 350 - 150 - 250 - 50 - 50"
    n = len([int(x) for x in samples_withdrawals_register.split(" - ")])
    print("Customers that used the withdrawals register in a day: " + str(n))
    X_signed = sample_mean(samples_withdrawals_register)
    print("sample mean of withdrawals = " + str(X_signed))
    S_squared = sample_variance(samples_withdrawals_register, X_signed)
    S = math.sqrt(S_squared)
    print("sample variance of deposits = " + str(S_squared) + ", standard deviation = " + str(S))
    #show_normal(X_signed, S)

    # -------------------------------------------------------------------------------------
    # ---------------------Special register: Withdrawals and Deposits----------------------
    # -------------------------------------------------------------------------------------
    print("-----------------Special register: Withdrawals and Deposits-----------------")
    #the following data are all from a solar day

    #study of the samples given by observing withdrawals from the special register
    samples_special_register_withdrawals = "100 - 300 - 160 - 270 - 250 - 140 - 70 - 40 - 20 - 40 - 150 - 500 - 500 - 210 - 300 - 20 - 300 - 1000 - 1000 - 500 - 90 - 600 - 150 - 600 - 350 - 210 - 80 - 150 - 150 - 150 - 500 - 500 - 1000 - 80 - 150 - 500 - 250 - 100 - 800 - 150 - 150 - 60 - 1000 - 200 - 100 - 150 - 500 - 500 - 500 - 950 - 420 - 100 - 250 - 200 - 100 - 600 - 40 - 50 - 100 - 1000 - 1000 - 60 - 350 - 420 - 420 - 300 - 500 - 500 - 40 - 500 - 950 - 1000 - 1000 - 150 - 250 - 500 - 250 - 500 - 50 - 250 - 140 - 140 - 210 - 140 - 350 - 900 - 140 - 250 - 250 - 40 - 40 - 250 - 20 - 40 - 20 - 120 - 100 - 500 - 500 - 500 - 280"
    n = len([int(x) for x in samples_special_register_withdrawals.split(" - ")])
    print("Customers that used the special register (for withdrawals) in a day: " + str(n))
    X_signed = sample_mean(samples_special_register_withdrawals)
    print("sample mean of withdrawals = " + str(X_signed))
    S_squared = sample_variance(samples_special_register_withdrawals, X_signed)
    S = math.sqrt(S_squared)
    print("sample variance of withdrawals = " + str(S_squared) + ", standard deviation = " + str(S))
    #show_normal(X_signed, S)

    #study of the samples given by observing deposits from the special register
    samples_special_register_deposits = "200 - 600 - 930 - 2800 - 50 - 40 - 600 - 420 - 1100 - 10350 - 2210 - 70 - 450 - 1900 - 80 - 1980 - 410 - 130 - 15000 - 800 - 200 - 400 - 700 - 7000 - 8855 - 6850 - 400 - 2160 - 2000 - 1290 - 400 - 1000 - 130 - 105 - 950 - 3000 - 2800 - 1000 - 20 - 2900 - 800 - 1200 - 1050 - 50 - 330 - 600 - 40 - 960 - 320 - 4450 - 170 - 50 - 1000 - 350 - 150"
    n = len([int(x) for x in samples_special_register_deposits.split(" - ")])
    print("Customers that used the special register (for deposits) in a day: " + str(n))
    X_signed = sample_mean(samples_special_register_deposits)
    print("sample mean of deposits = " + str(X_signed))
    S_squared = sample_variance(samples_special_register_deposits, X_signed)
    S = math.sqrt(S_squared)
    print("sample variance of deposits = " + str(S_squared) + ", standard deviation = " + str(S))
    #show_normal(X_signed, S)

    #we know that, from 8.30 to 13.00, an average of 40 customers arrive to the bank branch.
    #We assume, for simplicity, to model the arrival times of the customers with a poisson process.
    #Let's take as unit of time, for our modelling, the minutes: the rate Lambda at which a customer
    #arrives per minute, in this interval of time, is 40/270 (approx. 0.148)
    #let's try to generate the instants in time in which the customers arrive with an algorithm for
    #simulating a poisson process.
    lambda_served_customers = 40/270
    T = 60*13       #13:00
    i = 0
    t = 60*8 + 30   #8:30
    while t < T:
        i = i + 1
        s = random.exponential(1/lambda_served_customers)
        t += s
        if t < T:
            h = t//60
            m = t%60
            print("the %d th customer arrived at time %d : %d" %(i, h, m))

    #Now let's do the same for the arrival of customers that want no use one of the ATMs.
    #Experience showed that in a solar day (so, from 00:00 to 00:00 of the following day), an average
    #of 300 customers show up to use one of the ATMs. Also in this case, we can model their arrival
    #times with a poisson process.
    lambda_atm_customers = 300 / 1440
    T = 1440    #00:00 of the following day
    i = 0
    t = 0       #00:00 of the current day
    while t < T:
        i = i + 1
        s = random.exponential(1 / lambda_atm_customers)
        t += s
        if t < T:
            h = t // 60
            m = t % 60
            print("the %d th customer arrived at time %d : %d" % (i, h, m))
