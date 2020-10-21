from argparse import ArgumentParser as ap
from datetime import timedelta
from secrets import choice
from string import ascii_letters
from timeit import default_timer as timer


def reset_stopwatch():
    return timer()


def get_elapsed(starttime):
    end = timer()
    return timedelta(seconds=end - starttime)


def randstring(strlen=64):
    return ''.join(choice(ascii_letters) for _ in range(strlen))


def spawn(listlen=100):
    base_list = [randstring(10) + "." + randstring(10) + "@" + randstring(15) + ".com" for _ in range(listlen)]
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
    return list(seen), uneek


# NOTE:
# In the event that you do not need both lists,
# there is a much simpler, more "pythonic", way
# to do the pruning with python:
def prune(biglist):
    return list(dict.fromkeys(biglist))


if __name__ == "__main__":
    parser = ap()
    parser.add_argument('-e', '--emails', type=int, default=1000, metavar="emails",
                        help='The number of emails to generate (default=1000)', required=False)
    parser.add_argument('-d', '--dump', action="store_true",
                        help='Dump the email list to the console (Default=no)', required=False)
    args = parser.parse_args()
    email_count = args.emails

    # NOTE: The spawning process takes an enormous amount of time,
    # but since the challenge didn't say anything about how long it takes to
    # generate 100,000 emails (only how long it takes to de-dupe them), I
    # didn't do much to try to optimize the creation of the list of emails.
    # But I will say, that I kept it entirely in memory, to avoid having to
    # deal with disk i/o.
    start = reset_stopwatch()
    list_with_dups = spawn(email_count)
    print(f"GENERATED COMPLETE LIST WITH DUPLICATES: (count = {len(list_with_dups)})")
    if args.dump:
        [print(i) for i in list_with_dups]
    t1 = get_elapsed(start)
    print("Elapsed Time: ", t1)


    # This is the part we really care about. This step takes the generated list,
    # and runs it through the de-duplicator, returning two lists: the originals,
    # and the duplicates. Note, that these lists are identical in LENGTH ONLY,
    # because the bifurcation process leaves them unsorted, according to the
    # requirements. If sorted, they could be shown to be identical in content
    # as well.
    start = reset_stopwatch()
    dup_list, orig_list = dups(list_with_dups)
    print(f"IDENTIFIED DUPLICATES IN COMPLETE LIST: (count = {len(dup_list)})")
    if args.dump:
        [print(i) for i in dup_list]
    t2 = get_elapsed(start)
    print("Elapsed time: ", t2)

    print("\n\n")
    print(f"TOTAL ELAPSED TIME: {t1 + t2}")
