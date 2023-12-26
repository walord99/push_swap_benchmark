import random
import subprocess
import sys
from multiprocessing import Process, Value, Array, Pool

path = ''
seed = -1

def main():

    if not (len(sys.argv) == 3 or len(sys.argv) == 4):
        print("arguments: path, iteration")
        sys.exit(1)
    try:
        globals()['path'] = sys.argv[1]
        iteration = int(sys.argv[2])
        if len(sys.argv) == 4:
            globals()['seed'] = int(sys.argv[3])
        print("%s" %(run_test(10, iteration)))
        print("%s" %(run_test(100, iteration)))
        print("%s" %(run_test(500, iteration)))
    except Exception as error:
        print("invalide args", error)

def child(return_array, pos, list_size):
    list = ""
    rand = list_generator(list_size)
    for num in rand:
        list += f"%s " %(str(num))
    return_array[pos] = int(subprocess.getoutput(f'%s %s | wc -l' %(path, str(list))))

def run_test(list_size, iteration):
    total = 0

    op_count = Array('i' ,iteration)
    i = 0
    p = []
    while i != iteration:
        p.append(Process(target=child, args=(op_count, i, list_size)))
        p[i].start()
        i += 1
    for proc in p:
        proc.join()
    for i in op_count:
        total += i
    return total / iteration

def list_generator(size):
    list = []
    if seed != -1:
        random.seed(seed);
    for i in range(size):
        r = random.randint(0, 2147483647)
        if r not in list:
            list.append(r)
    return list


if __name__ == "__main__":
    main()