import csv
import time

def load_data(file_path):
    dataset = []
    with open(file_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cleaned_id = row['Product ID'].strip(', ')
            dataset.append({
                'customer_name': row['Customer Name'],
                'purchase_date': row['Purchase Date'],
                'product_id': cleaned_id,
                'product_category': row['Product Category'],
                'amount': float(row['Amount'])
            })
    return dataset

# 1. Sequential Search (Unindexed / Unsorted Data)
def sequential_search(data, target_id):
    comparisons = 0
    start = time.perf_counter()
    results = []
    for item in data:
        comparisons += 1
        if item['product_id'] == target_id:
            results.append(item)
    end = time.perf_counter()
    return results, comparisons, (end - start) * 1000

# 2. Binary Search (Indexed / Sorted Data)
def binary_search(sorted_data, target_id):
    comparisons = 0
    start = time.perf_counter()
    low, high = 0, len(sorted_data) - 1
    found_idx = -1

    while low <= high:
        comparisons += 1
        mid = (low + high) // 2
        mid_id = sorted_data[mid]['product_id']

        if mid_id == target_id:
            found_idx = mid
            break
        elif mid_id < target_id:
            low = mid + 1
        else:
            high = mid - 1

    results = []
    if found_idx != -1:
        i = found_idx
        while i >= 0 and sorted_data[i]['product_id'] == target_id:
            results.append(sorted_data[i])
            i -= 1
        i = found_idx + 1
        while i < len(sorted_data) and sorted_data[i]['product_id'] == target_id:
            results.append(sorted_data[i])
            i += 1

    end = time.perf_counter()
    return results, comparisons, (end - start) * 1000

if __name__ == "__main__":
    file_name = "Kamsberry Store RESPONSES - Form Responses 1.csv"
    target = "PROD101"

    data = load_data(file_name)
    seq_res, seq_comp, seq_time = sequential_search(data, target)

    sorted_data = sorted(data, key=lambda x: x['product_id'])
    bin_res, bin_comp, bin_time = binary_search(sorted_data, target)

    print("=" * 55)
    print(f"  SEARCH SIMULATION COMPARISON FOR: {target}")
    print("=" * 55)
    print(f"[Sequential Search - Unindexed]")
    print(f"  Matches Found : {len(seq_res)}")
    print(f"  Comparisons   : {seq_comp}")
    print(f"  Time Elapsed  : {seq_time:.4f} ms\n")
    print(f"[Binary Search - Indexed/Sorted]")
    print(f"  Matches Found : {len(bin_res)}")
    print(f"  Comparisons   : {bin_comp}")
    print(f"  Time Elapsed  : {bin_time:.4f} ms")
    print("=" * 55)