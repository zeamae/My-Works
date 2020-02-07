import random
import time
import matplotlib.pyplot as plt

start_timemten = time.time()

print("To be sorted:")

print("  ")
mtenlist = []
for i in range(0,10):
    mt = random.randint(0,10)
    mtenlist.append(mt)

def Merge_SortTen(mtenlist):
    
    if len(mtenlist)>1:
        mid = len(mtenlist)//2
        array1 = mtenlist[:mid]
        array2 = mtenlist[mid:]
        Merge_SortTen(array1)
        Merge_SortTen(array2)
        i=0
        j=0
        k=0
        while i < len(array1) and j < len(array2):
            if array1[i] <= array2[j]:
                mtenlist[k] = array1[i]
                i = i+1
            else:
                mtenlist[k] = array2[j]
                j = j+1
            k = k+1
        while i < len(array1):
            mtenlist[k] = array1[i]
            i = i+1
            k = k+1
        while j < len(array2):
            mtenlist[k] = array2[j]
            j = j+1
            k = k+1

Merge_SortTen(mtenlist)
end_timemten = time.time()
mergeten = end_timemten - start_timemten
print('10 Integers')
print(mtenlist)
print('Execution Time: ', mergeten)
print("")


print("----")
start_timemhun = time.time()
mhunlist = []
for i in range(0,100):
    mhun = random.randint(0,100)
    mhunlist.append(mhun)

def Merge_SortHun(mhunlist):
    
    if len(mhunlist)>1:
        mid = len(mhunlist)//2
        array1 = mhunlist[:mid]
        array2 = mhunlist[mid:]
        Merge_SortHun(array1)
        Merge_SortHun(array2)
        i=0
        j=0
        k=0
        while i < len(array1) and j < len(array2):
            if array1[i] <= array2[j]:
                mhunlist[k] = array1[i]
                i = i+1
            else:
                mhunlist[k] = array2[j]
                j = j+1
            k = k+1
        while i < len(array1):
            mhunlist[k] = array1[i]
            i = i+1
            k = k+1
        while j < len(array2):
            mhunlist[k] = array2[j]
            j = j+1
            k = k+1

Merge_SortHun(mhunlist)
end_timemhun = time.time()
mergehun = end_timemhun - start_timemhun
print('100 Integers')
print(mhunlist)
print('Execution Time: ', end_timemhun - start_timemhun)
print("")


print("----")
start_timetho = time.time()
mthoulist = []
for i in range(0,1000):
    mthou = random.randint(0,1000)
    mthoulist.append(mthou)

def Merge_SortThou(mthoulist):
    
    if len(mthoulist)>1:
        mid = len(mthoulist)//2
        array1 = mthoulist[:mid]
        array2 = mthoulist[mid:]
        Merge_SortThou(array1)
        Merge_SortThou(array2)
        i=0
        j=0
        k=0
        while i < len(array1) and j < len(array2):
            if array1[i] <= array2[j]:
                mthoulist[k] = array1[i]
                i = i+1
            else:
                mthoulist[k] = array2[j]
                j = j+1
            k = k+1
        while i < len(array1):
            mthoulist[k] = array1[i]
            i = i+1
            k = k+1
        while j < len(array2):
            mthoulist[k] = array2[j]
            j = j+1
            k = k+1
Merge_SortThou(mthoulist)
end_timemthou = time.time()
mergethou = end_timemthou - start_timetho
print('1000 Integers')
print(mthoulist)
print('Execution Time: ', mergethou)
print("")



left = [1,2,3]
height = [mergeten, mergehun, mergethou]

tick_label = ['10', '100', '1000']

plt.bar(left, height, tick_label=tick_label,
        width=0.8, color=['red', 'green'])

plt.xlabel('Number of Integers')
plt.ylabel('Execution Time (sec)')

plt.title('Merge Sort')

plt.show()
