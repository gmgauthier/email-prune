from string import ascii_letters
from secrets import choice
from timeit import default_timer as timer
from datetime import timedelta


def reset_stopwatch():
    return timer()


def get_elapsed(starttime):
    end = timer()
    return timedelta(seconds=end-starttime)


def randstring(strlen=64):
    return ''.join(choice(ascii_letters) for _ in range(strlen))


def spawn(listlen=100):
    base_list = [randstring(10)+"."+randstring(10)+"@"+randstring(15)+".com" for _ in range(listlen)]
    dup_list = [choice(base_list) for _ in range(len(base_list))]
    final_list = []
    for i in range(listlen):
        final_list.append(base_list[i])
        final_list.append(dup_list[i])
    return final_list


def dups(biglist):
    seen = set()
    uneek = []
    for x in biglist:
        if x not in seen:
            uneek.append(x)
            seen.add(x)
    return seen


if __name__ == "__main__":
    start = reset_stopwatch()
    list_with_dups = spawn(50000)
    print(f"GENERATED COMPLETE LIST WITH DUPLICATES: (count = {len(list_with_dups)})")
    # [print(i) for i in list_with_dups]
    t1 = get_elapsed(start)
    print("Elapsed Time: ", t1)

    start = reset_stopwatch()
    dup_list = dups(list_with_dups)
    print(f"IDENTIFIED DUPLICATES IN COMPLETE LIST: (count = {len(dup_list)})")
    # [print(i) for i in dup_list]
    t2 = get_elapsed(start)
    print("Elapsed time: ", t2)

    start = reset_stopwatch()
    list_with_dups = list(dict.fromkeys(list_with_dups))
    print(f"GENERATED PRUNED LIST WITHOUT DUPLICATES: (count = {len(list_with_dups)})")
    # [print(i) for i in list_with_dups]
    t3 = get_elapsed(start)
    print("Elapsed Time: ", t3)
    print(f"TOTAL ELAPSED TIME: {t1+t2+t3}")
    print(f"ELAPSED TIME WITHOUT GENERATOR: {t2+t3}")
