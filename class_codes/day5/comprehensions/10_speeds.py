python -m timeit -s 'listx=range(10)' 'map(str, listx)'

python -m timeit -s 'listx=range(10)' '[str(x) for x in listx]'


python -m timeit -s 'listx=range(10)' 'map(lambda x: x+3, listx)'

python -m timeit -s 'listx=range(10)' '[x+3 for x in listx]'
