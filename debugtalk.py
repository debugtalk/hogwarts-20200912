import time
import random

from httprunner import __version__


def get_httprunner_version():
    return __version__


def sum_two(m, n):
    return str(m + n)


def get_doc_id_len(docId):
    print("docId===: ", docId)
    return str(len(docId))


def sleep(n_secs):
    time.sleep(n_secs)


def gen_member_id():
    return f"1979064713794{random.randint(100, 999)}"
