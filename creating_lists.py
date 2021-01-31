import timeit
import matplotlib.pyplot as plt


# create a list using concatentation
def listCreateV1(n):
    l = []
    for i in range(n):
        l = l + [i]

# create a list using list's append method
def listCreateV2(n):
    l = []
    for i in range(n):
        l.append(i)

# create list using a list comprehension
def listCreateV3(n):
    l = [i for i in range(n)]

# create a list from a range object
def listCreateV4(n):
    l = list(range(n))


t1 = list()
t2 = list()
t3 = list()
t4 = list()

values = list(range(1000, 10000, 1000))

for v in values:
    t1.append(timeit.timeit("listCreateV1("+str(v)+")", "from __main__ import listCreateV1", number=100)/100)
    t2.append(timeit.timeit("listCreateV2("+str(v)+")", "from __main__ import listCreateV2", number=100)/100)
    t3.append(timeit.timeit("listCreateV3("+str(v)+")", "from __main__ import listCreateV3", number=100)/100)
    t4.append(timeit.timeit("listCreateV4("+str(v)+")", "from __main__ import listCreateV4", number=100)/100)


plt.plot(values, t1, color='red')
plt.plot(values, t2, color='blue')
plt.plot(values, t3, color='green')
plt.plot(values, t4, color='yellow')
plt.legend(('concat', 'append', 'comprehension', 'range'), loc='upper left')
plt.title('Comparing ways to create a list')
plt.show()

