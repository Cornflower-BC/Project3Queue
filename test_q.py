from q import *
import pytest

def test_is_empty():
    empty = Queue()
    assert empty.is_empty()

def test_add():
    fish = Queue()
    fish.add("one fish")
    assert(repr(fish) == "Queue object: one fish -- ")
    fish.add("two fish")
    assert(repr(fish) == "Queue object: one fish -- two fish -- ")
    fish.add("red fish")
    assert(repr(fish) == "Queue object: one fish -- two fish -- red fish -- ")
    fish.add("blue fish")
    assert(repr(fish) == "Queue object: one fish -- two fish -- red fish -- blue fish -- ")

def test_size():
    starfish = Queue()
    starfish.add("purple")
    assert starfish.size == 1

def test_pop_left():
    squid = Queue()
    squid.add("tentacle")
    squid.add("beak")
    assert(repr(squid) == "Queue object: tentacle -- beak -- ")
    squid.pop_left()
    assert(repr(squid) == "Queue object: beak -- ")
    
    
