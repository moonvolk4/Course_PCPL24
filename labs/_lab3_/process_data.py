import json
import sys
from cm_timer import cm_timer_1
from print_result import print_result
from gen_random import gen_random
from operator import itemgetter
import random

path = "/Users/volkov_kirill/Desktop/python_projects/Labs_3sem/_lab3_/data_light.json"

with open(path) as f:
    data = json.load(f)

@print_result
def f1(arg):
    return sorted(list(set(map(lambda x: x['job-name'].lower(), arg))), key=str.lower)

@print_result
def f2(arg):
    return list(filter(lambda x: x.lower().startswith('программист'), arg))

@print_result
def f3(arg):
    return list(map(lambda x: f"{x} с опытом Python", arg))

@print_result
def f4(arg):
    salaries = [random.randint(100000, 200000) for _ in range(len(arg))]
    return [f"{job}, зарплата {salary} руб." for job, salary in zip(arg, salaries)]

if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))