import os

with open('Renamed_by_python.py') as f:
    data = f.read()

with open('sample.txt', 'w') as f:
    f.write(data)
os.remove('Renamed_by_python.py')