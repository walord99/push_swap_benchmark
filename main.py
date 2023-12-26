import random
import subprocess
import sys

def main():

    if len(sys.argv) != 3:
        print("arguments: path, iteration")
        sys.exit(1)
    try:
        path = sys.argv[1]
        iteration = int(sys.argv[2])
        print("%s" %(run_test(10, iteration, path)))
        print("%s" %(run_test(100, iteration, path)))
        print("%s" %(run_test(500, iteration, path)))
    except:
        print("invalide args")

def run_test(list_size, iteration, path):
    total = 0

    i = iteration;
    while i != 0:
        list = ""
        rand = list_generator(list_size)
        for num in rand:
            list += f"%s " %(str(num))
        total += int(subprocess.getoutput(f'%s %s | wc -l' %(path, str(list))))
        i -= 1
    return total / iteration

def list_generator(size):
    list = []
    for i in range(size):
        r = random.randint(0, 2147483647)
        if r not in list:
            list.append(r)
    return list


if __name__ == "__main__":
    main()