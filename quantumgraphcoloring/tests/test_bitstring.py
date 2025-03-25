
import sys

import pytest
import numpy as np
import montecarlo as montecarlo


def test_create():
    my_bs2 = montecarlo.BitString(8)
    my_bs2.flip_site(2)
    my_bs2.flip_site(2)
    print(" The following should be 0:")
    print(my_bs2)

    my_bs2.flip_site(2)
    my_bs2.flip_site(7)
    my_bs2.flip_site(0)
    print(" The following should have 0,2,7 bits flipped:")
    print(my_bs2)

    print(" Length of bitstring: ", len(my_bs2))
    assert(len(my_bs2) == 8)
    

    
def test_basicFunctions():
    my_bs = montecarlo.BitString(13)
    my_bs.set_config([0,1,1,0,0,1,0,0,1,0,1,0,0])
    assert(my_bs.on() == 5)
    assert(my_bs.off() == 8)
    assert(my_bs.int() == 3220)
    
    
def test_advanced():
    my_bs3 = montecarlo.BitString(20)
    my_bs3.set_int_config(3221)

    # Let's make sure this worked:
    tmp = np.array([0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,1,0,1,0,1])
    assert((my_bs3.config == tmp).all())

    # We can provide an even stronger test here:
    for i in range(1000):
        my_bs3.set_int_config(i) # Converts from integer to binary
        assert(my_bs3.int() == i) # Converts back from binary to integer and tests

def test_equal():
    my_bs4 = montecarlo.BitString(13)
    my_bs4.set_config([0,1,1,0,0,1,0,1,1,0,1,0,0])

    my_bs5 = montecarlo.BitString(13)
    my_bs5.set_int_config(3252)
    assert(my_bs4 == my_bs5)

    my_bs5.flip_site(5)
    assert(my_bs4 != my_bs5)