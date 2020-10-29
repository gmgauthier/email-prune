# email-pruner [![gmgauthier](https://circleci.com/gh/gmgauthier/email-prune.svg?style=svg)](https://circleci.com/gh/gmgauthier/email-prune)

An experiment in Python lists.

#### Requirements
* Python 3.7+ (needed for the "fprint" statements)
* Pipenv ~2020.8.13 (for virtualenv dev)
* Pytest 6+

#### Setup
* cd into the root of the project
* type these commands
```shell script
$ python3 -m pip install pipenv 
$ pipenv --python 3.7
$ pipenv install
$ pipenv shell
```
This will drop you into the virtualenv, with the right packages already installed. Next, all you need to do, is run the tests, then run the app, which should look someething like this:


```shell script
(email-prune) [23:02:47][~/Projects/Coding/Python/email-prune]
gmgauthier@shackleton $ pytest -vv                         
=================== test session starts ==============================================================================
platform darwin -- Python 3.8.6, pytest-6.1.1, py-1.9.0, pluggy-0.13.1 -- /Users/gmgauthier/.local/share/virtualenvs/email-prune-6GbCapbV/bin/python
cachedir: .pytest_cache
rootdir: /Users/gmgauthier/Projects/Coding/Python/email-prune
collected 6 items

test_email_pruner.py::test_email_creation PASSED                                                                 [ 16%]
test_email_pruner.py::test_dup_list_creation PASSED                                                              [ 33%]
test_email_pruner.py::test_compare_dups_and_pruned PASSED                                                        [ 50%]
test_email_pruner.py::test_alternative_pruner PASSED                                                             [ 66%]
test_email_pruner.py::test_random_string_contents PASSED                                                         [ 83%]
test_email_pruner.py::test_random_string_len PASSED                                                              [100%]

============================ 6 passed in 0.03s ========================================================================
(email-prune) [23:02:55][~/Projects/Coding/Python/email-prune]
gmgauthier@shackleton $ python ./email_pruner.py -e 750000              
GENERATED COMPLETE LIST WITH DUPLICATES: (count = 1500000)
Elapsed Time:  0:00:57.541989
IDENTIFIED DUPLICATES IN COMPLETE LIST: (count = 750000)
Elapsed time:  0:00:00.545665

TOTAL ELAPSED TIME: 0:00:58.087654
```

### NOTES
I have a lot of comments in the code and on the tests, that explain my reasoning around certain decisions. I'll just explain the console output here. 

What you're seeing echoed out to the console is a record of the amount of time it took to execut the two major steps in this code (a) the generation of the emai list (which includes the duplications inserted in random order), and (b) the amount of time it took to execute the identification of those duplications, including bifurcating the list into two separate lists: originals, and duplicates. 

As you can see, this particular execution was a sort of simple "load test" on the app. The requirements called for isolating the duplicates in 100,000 emails in less than a second. This code was able to do 1.5 million, in 546 milliseconds. Not bad! 

The tests are run with pytest. They are designed to run quickly. I'm only seeding 100 emails. The point is merely to demonstrate the functionality of the methods I wrote, and to showcase the importance of TESTING the application (and to demonstrate that I can reason good assertions from the requirements). 

I should mention, I could have wrapped the tests in the Behave DSL, but chose not to for this challenge because the nature of the work being done in this application is at the functional integration level, rather than at the level of user interaction. Gherkin specifications are best used in the context of a behavioral relationship between user and application, rather than as a tool for "englishifying" component level specifications. The "raw" test code is much more instructive, if you know what you're looking for.

