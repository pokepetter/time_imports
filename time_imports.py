from time import perf_counter
import sys

target_file = sys.argv[1]

import_times = list()
with open(target_file, 'r', encoding='utf-8') as f:
    file_content = f.read()
    lines = file_content.split('\n')
    for line in lines:
        if line.startswith('import') or line.startswith('from'):
            line = line.strip()
            t0 = perf_counter()
            try:
                exec(line)
            except:
                print('error:', line)

            t1 = perf_counter()
            duration = t1 - t0
            duration = str(round(duration, 4))
            duration += ' '*(10-len(duration))
            print(duration, line)
