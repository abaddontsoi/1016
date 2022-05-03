import argparse
from distutils.log import error
from os import remove
from traceback import print_exception


parser = argparse.ArgumentParser()

parser.add_argument('-i', '--ip', help='Input an IPv4 as parameter', nargs=1)
parser.add_argument('-m', '--mask', help='Input a network mask as parameter', nargs=1)

args = parser.parse_args()

def checkRange(ip):
    if len(ip) != 4:
        print('no good ip/mask entered')
        return False
    for i in ip:
        if i not in range(0,256):
            print('out of range')
            return False
    return True

splited = []

try:
    if args.ip is not None:
        splited = [ int(txt) for txt in args.ip[0].split('.')]
except ValueError:
    print('\nvalue error')

if checkRange(splited):
    try:
        print('IP')
        for i in splited:
            print(i)

        if splited[0] in range(0,127):
            print('is class A')

        if splited[0] in range(128, 192):
            print('is class B')

        if splited[0] in range(192,223):
            print('in class C')


        print('\nIP in binary: ')
        splited_bin = [f'{data:08b}' for data in splited]

        for i in splited_bin:
            print(i, end='\t')
        print()
    except ValueError as ve:
        print('value eror')


splited_mask = []
try:
    if args.mask is not None:
        splited_mask = [int(txt) for txt in args.mask[0].split('.')]
except ValueError as ve:
    print('Mask value error')

if checkRange(splited_mask):
    full_one = '11111111'
    full_zero = '00000000'

    print('\nMask')
    try:
        for i in splited_mask:
            print(i, end=' ')

        print('\nMask in binary: ')
        splited_bin = [f'{data:08b}' for data in splited_mask]

        for i in splited_bin:
            print(i, end='\t')
        print()

        _mask_diff_zero = []
        _mask_diff_one = []
        for j in splited_bin:
            _mask_diff_zero.append([i for i in range(len(j)) if j[i] != full_one[i]])
            _mask_diff_one.append([i for i in range(len(j)) if j[i] != full_zero[i]])

        for item in _mask_diff_zero:
            mask_diff_zero = [len(data) for data in _mask_diff_zero]
            mask_diff_one = [len(data) for data in _mask_diff_one]

        print(mask_diff_zero, end=' zero diff\n')
        print(mask_diff_one, end=' one diff\n')

        exp = 0
        for item in mask_diff_zero:
            if item!=0:
                exp += item
        total_host = 2**exp-2
        print(total_host, end=' hosts\n')

        for item in mask_diff_one:
            if item!=8:
                total_network = 2**item - 2
                print(total_network, end=' subnet\n')
                break

    except ValueError as ve:
        print('value eror')
