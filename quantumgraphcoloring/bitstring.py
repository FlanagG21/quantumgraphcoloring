
import numpy as np
from typing import List
class BitString:
    """
    Class representing a bit string.

    :param N: Length of the bit string.
    """
    def __init__(self, N):
        """
        Initialize the BitString object.

        :param N: Length of the bit string.
        """
        self.N = N
        self.config = np.zeros(N, dtype=int)

    def __repr__(self):
        pass

    def __eq__(self, other):
        """
        Check if two BitString objects are equal.

        :param other: Another object to compare.
        :return: True if equal, False otherwise.
        """
        if other is None :
            return False
        if type(self) != type(other) :
            return False
        if self.N != other.N :
            return False              
        return np.array_equal(self.config, other.config)


    
    def __len__(self):
        """
        Get the length of the bit string.

        :return: Length of the bit string.
        """
        return self.N

    def on(self):
        """
        Count the number of 'on' bits in the bit string.

        :return: Number of 'on' bits.
        """
        return self.config.sum()

    
    def off(self):
        """
        Count the number of 'off' bits in the bit string.

        :return: Number of 'off' bits.
        """
        return self.N - self.config.sum()
    
    def flip_site(self,i):
        """
        Flip the bit at the specified index.

        :param i: Index of the bit to flip.
        """
        self.config[i] = (self.config[i] + 1) % 2 
    
    def int(self):
        """
        Convert the bit string to an integer.

        :return: Integer representation of the bit string.
        """
        num = 0
        for i, bit in enumerate(reversed(self.config)):
            num += bit * (2 ** i)
        return num

    def set_config(self, s:List[int]):
        """
        Set the bit string from a list of integers.

        :param s: List of integers representing the bit string.
        """
        for i, bit in enumerate(s):
            self.config[i + (self.N - len(s))] = bit
        
    def set_int_config(self, dec:int):
        """
        Set the bit string from an integer.

        :param dec: Integer representation of the bit string.
        """        
        for i in range(len(self.config)):
            self.config[i] = dec % 2
            dec //= 2
        self.config = self.config[::-1]
        



    def __str__(self):
        """
        Get the string representation of the bit string.

        :return: String representation of the bit string.
        """
        builder = ""
        for bit in self.config:
            builder += str(bit)
        return builder
