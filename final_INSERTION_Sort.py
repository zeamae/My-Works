#FINAL

import time
import random
import matplotlib.pyplot as plt

start_time = time.time()
x = []
y = []


def insertion_sort1():
    z = 1000
    numGen = random.sample(range(0, z), z)

    for i in range(1, z):
        value = numGen[i]
        pos = i
        while pos > 0 and numGen[pos - 1] > value:
            numGen[pos] = numGen[pos - 1]
            pos = pos - 1

        numGen[pos] = value

    print(numGen)
    x.append(z)

    end_time = time.time()
    runTime = end_time - start_time
    print("Execution time:", runTime, "seconds")
    y.append(runTime)

insertion_sort1()
print("")

def insertion_sort2():
    z = 500
    numGen = random.sample(range(0, z), z)

    for i in range(1, z):
        value = numGen[i]
        pos = i
        while pos > 0 and numGen[pos - 1] > value:
            numGen[pos] = numGen[pos - 1]
            pos = pos - 1

        numGen[pos] = value

    print(numGen)
    x.append(z)

    end_time = time.time()
    runTime = end_time - start_time
    print("Execution time:", runTime, "seconds")
    y.append(runTime)

insertion_sort2()
print("")

def insertion_sort3():
    z = 100
    numGen = random.sample(range(0, z), z)

    for i in range(1, z):
        value = numGen[i]
        pos = i
        while pos > 0 and numGen[pos - 1] > value:
            numGen[pos] = numGen[pos - 1]
            pos = pos - 1

        numGen[pos] = value

    print(numGen)
    x.append(z)

    end_time = time.time()
    runTime = end_time - start_time
    print("Execution time:", runTime, "seconds")
    y.append(runTime)

insertion_sort3()
print("")

def insertion_sort4():
    z = 1200
    numGen = random.sample(range(0, z), z)

    for i in range(1, z):
        value = numGen[i]
        pos = i
        while pos > 0 and numGen[pos - 1] > value:
            numGen[pos] = numGen[pos - 1]
            pos = pos - 1

        numGen[pos] = value

    print(numGen)
    x.append(z)

    end_time = time.time()
    runTime = end_time - start_time
    print("Execution time:", runTime, "seconds")
    y.append(runTime)

insertion_sort4()
print("")

def insertion_sort5():
    z = 1450
    numGen = random.sample(range(0, z), z)

    for i in range(1, z):
        value = numGen[i]
        pos = i
        while pos > 0 and numGen[pos - 1] > value:
            numGen[pos] = numGen[pos - 1]
            pos = pos - 1

        numGen[pos] = value

    print(numGen)
    x.append(z)

    end_time = time.time()
    runTime = end_time - start_time
    print("Execution time:", runTime, "seconds")
    y.append(runTime)

insertion_sort5()
print("")


print(x)

plt.plot(x, y, 'bo')
plt.xlabel('Number of Integers')
plt.ylabel('Execution Time (sec)')
plt.axis([0, 2000, 0, 0.50])
plt.title("Insertion Sort")
plt.show()
