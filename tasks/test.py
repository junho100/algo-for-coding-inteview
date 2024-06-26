import glob
import csv
from concurrent.futures import ThreadPoolExecutor
import threading

all_numbers = set()

lock = threading.Lock()

def process_file(file_name):
    local_numbers = set()
    with open(file_name, 'r') as file:
        for line in file:
            number = int(line.strip())
            local_numbers.add(number)
    
    with lock:
        all_numbers.update(local_numbers)

csv_files = glob.glob("./example/*.csv")

with ThreadPoolExecutor() as executor:
    executor.map(process_file, csv_files)

sorted_numbers = sorted(list(all_numbers))

print(sorted_numbers)