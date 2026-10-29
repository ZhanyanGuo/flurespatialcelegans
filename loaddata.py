
import numpy as np

path = 
arr = np.load(path, allow_pickle=False)

print("Shape:", arr.shape)
print("Dimensions:", arr.ndim)
print("Data type:", arr.dtype)
print("Total elements:", arr.size)
print("Memory (MB):", arr.nbytes / 1024**2)

if np.issubdtype(arr.dtype, np.number):
    print("Minimum:", np.min(arr))
    print("Maximum:", np.max(arr))
    print("Nonzero elements:", np.count_nonzero(arr))
    print("Nonzero fraction:", np.count_nonzero(arr) / arr.size)

    values, counts = np.unique(arr, return_counts=True)

    print("\nUnique values:", len(values))
    if len(values) <= 30:
        print("Value counts:")
        for value, count in zip(values, counts):
            print(f"  {value}: {count}")
    else:
        print("First 15 values:", values[:15])
        print("Last 15 values:", values[-15:])

print("\nFirst few entries:")
print(arr.flat[:20])
