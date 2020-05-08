import pytest
import sys
import random
import index


def test_first_word():
    words = ["skillfactory", "testing", "blackbox", "pytest", "unittest", "coverage"]
    secret_word = random.choice(words)
    assert secret_word in words

def test_second_word():
    assert str(int()) not in index.secret_word
