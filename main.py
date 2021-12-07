import numpy as np

def calc():
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

    avg = np.average(arr)
    std = np.std(arr)
    min = np.min(arr)
    max = np.max(arr)
    print("avg = " , avg, " std = ", std, "min = ", min, "max = ", max)


def main():
    calc()

if __name__ == "__main__":
    main()

