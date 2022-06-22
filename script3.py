import sys
#realizar un script que imrima una pal x veces, 2 argumentos

if len(sys.argv)!=3:
    print("error 3 arg")
else:
    for i in range(int(sys.argv[2])):
        print(sys.argv[1])