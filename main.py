import numpy as np

def calc(type):
    arr = np.random.randint(0, 100, 100)
    #arr.sort()
    print("Original Data ")
    print(arr)
    upper = np.quantile(arr, 0.9)
    lower = np.quantile(arr, 0.1)
    condition = np.greater(arr, lower)
    arr = np.extract(condition, arr)
    condition = np.less(arr, upper)
    arr = np.extract(condition, arr)

    print("Trimmed Data ")
    print(arr)

    if type == 'avg':
       return np.average(arr)
    elif type =='std':
        return np.std(arr)
    elif type == 'min':
        return np.min(arr)
    elif type == 'max':
        return np.max(arr)

def main():
    print (calc('avg'))

if __name__ == "__main__":
    main()

