import multiprocessing
from datetime import datetime

def read_info(name):
    all_data = []
    with open(name, 'r') as file1:
        while True:
            line = file1.readline().strip()
            all_data.append(line)
            if not line:
                break

filenames = [f'file {number}.txt' for number in range(1, 5)]
start1 = datetime.now()

# Линейный вызов
for f in filenames:
    # print(f)
    read_info(f)

end1 = datetime.now()
time_of_line_function = end1 - start1
print(f'{time_of_line_function} (линейный)')

# Многопроцессный
if __name__ == '__main__':
    start2 = datetime.now()

    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)

    end2 = datetime.now()
    time_of_multiprocessing = end2 - start2
    print(f'{time_of_multiprocessing} (многопроцессный)')