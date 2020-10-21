# functional pytests
from email_pruner import dups, randstring, prune


# pytest uses some under-the-covers magic to make fixtures available to
# test methods. Check the "conftest.py" for the source of the "emails"
# argument you see in these tests.

def test_email_creation(emails):
    # spawn will return double the number requested,
    # because it generates randomized duplicates of
    # every email created. So, our test should be for
    # double the amount requested.
    assert len(emails) == 200


def test_dup_list_creation(emails):
    # the dups function copies out the duplicates
    # into a fresh list, giving us the freedom to
    # do what we like with them. Since 50% was the
    # requirement, this means that the dup list
    # should be just as long as the pruned list
    dup_list, prune_list = dups(emails)
    assert len(dup_list) == 100
    assert len(dup_list) == len(prune_list)


def test_compare_dups_and_pruned(emails):
    # the original spec says to leave the two lists unsorted
    # so name-for-name comparison should fail, because the
    # bifurcation process is going to create two disparately
    # ordered lists. So, here I include two assertions to
    # first confirm that the unordered lists are mismatched,
    # and second, confirm that the sorted lists can be shown
    # to be identical in content.
    dup_list, prune_list = dups(emails)
    assert not dup_list == prune_list
    assert dup_list.sort() == prune_list.sort()


def test_alternative_pruner(emails):
    # Python dictionaries provide a MUCH cleaner and simpler
    # technique for pruning duplicates from a list. However,
    # it discards the duplicates, rather than giving them
    # back to you. So, I provide this here just for illustration.
    # We want both lists, so that I can prove that my code worked.
    pruned = prune(emails)
    assert len(pruned) == 100


def test_random_string_contents():
    rstring = randstring() # default length = 64, alphas only.
    not_allowed = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~0123456789"
    assert not rstring.__contains__(not_allowed)


def test_random_string_len():
    rstring = randstring() # default length
    assert len(rstring) == 64