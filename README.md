# SHA-1 Algorithm Implementation
This project implements the SHA-1 algorithm for generating a hash from an input message.

## Table of contents
- [Overview](#overview)
- [Python Version Compatibility](#python-version-compatibility)
- [Installation and Dependencies](#installation-and-dependencies)
- [Usage](#usage)
- [Comparison of speed and memory consumption](#comparison-of-speed-and-memory-consumption)
- [Running Tests](#running-tests)

## Overview
SHA-1 (Secure Hash Algorithm 1) is a cryptographic hash function that produces a 160-bit (20-byte) hash value. It is commonly used to ensure data integrity.

The implemented `SHA1` class from `sha_1` module contains the following methods:

- `__init__(self, input_message: str)`: Initializes the SHA1 object with the input message.
- `rotate(n, b)`: Performs a cyclic left shift on a 32-bit number.
- `pad_with_zeros(self)`: Pads the input message to ensure it has 512 bits.
- `split_blocks(self)`: Splits the padded data into 64-byte blocks.
- `expand_block(self, block: bytes)`: Expands a 512-bit block into an 80-word message schedule.
- `hash(self)`: Generates the SHA-1 hash for the provided data.

## Python Version Compatibility
This project is developed using Python version 3.10.7. While it may be possible to run the project on earlier Python versions, it is important to note that doing so might result in unexpected side effects or errors. For optimal performance and to prevent potential issues, it's recommended to use Python version 3.10.7 or higher.

## Installation and Dependencies

To utilize the `SHA-1` algorithm implementation, ensure you have Python installed. You can install the required dependencies by running the following command:

```bash
pip install -r requirements.txt
```

## Usage
You can create an instance of the `SHA1` class by providing a string input message, and then use the `hash()` method to get the SHA-1 hash.

Example:

```python
from sha_1 import SHA1

message = "Your message here"
sha1 = SHA1(message)
hashed_result = sha1.hash()
print("SHA-1 Hash:", hashed_result)
```

## Comparison of speed and memory consumption
Compared to the library implementation, this implementation is much slower. Below is a comparison of the speed of own implementation and the library implementation for messages of different lengths.

```text
Input message: Hello World
Custom implementation:	0a4d55a8d778e5022fab701977c5d840bbc486d0 	Execution time: 0.0001979998778551817	seconds
Library implementation:	0a4d55a8d778e5022fab701977c5d840bbc486d0	Execution time: 3.410014323890209e-05	seconds


Input message: Cryptography for Developers
Custom implementation:	ecf754e6346bf05dcd14ffa7d60a7b2791d92e50 	Execution time: 0.0001705000177025795	seconds
Library implementation:	ecf754e6346bf05dcd14ffa7d60a7b2791d92e50	Execution time: 2.299901098012924e-06	seconds


Input message: The National Institute of Standards and Technology (NIST) is an agency of the United States Department of Commerce whose mission is to promote American innovation and industrial competitiveness.
Custom implementation:	be81a05af54c04da654ff4fb50b35a571a3964e5 	Execution time: 0.0009530999232083559	seconds
Library implementation:	be81a05af54c04da654ff4fb50b35a571a3964e5	Execution time: 5.00003807246685e-06	seconds


Input message: SHA-3 (Secure Hash Algorithm 3) is the latest member of the Secure Hash Algorithm family of standards
Custom implementation:	11a6801194a593026665c92ebd1d7e1ce4409147 	Execution time: 0.0005644999910145998	seconds
Library implementation:	11a6801194a593026665c92ebd1d7e1ce4409147	Execution time: 6.00004568696022e-06	seconds


Input message: In mathematics, theta functions are special functions of several complex variables. They show up in many topics, including Abelian varieties, moduli spaces, quadratic forms, and solitons. As Grassmann algebras, they appear in quantum field theory.
Custom implementation:	21390ad07063352b20b15181e1a1324c4af1687c 	Execution time: 0.0007841000333428383	seconds
Library implementation:	21390ad07063352b20b15181e1a1324c4af1687c	Execution time: 3.400025889277458e-06	seconds
```

Below is the memory consumption of the hashing function in own implementation.

```text
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    64     19.7 MiB     19.7 MiB           1       def hash(self) -> str:
    65                                                 """
    66                                                 Generates SHA-1 hash for the provided data.
    67                                         
    68                                                 The hash() method implements the Secure Hash Algorithm 1 (SHA-1) logic for
    69                                                 generating a hashed output from the given data. It follows the SHA-1 hashing
    70                                                 process by first padding the input data, splitting it into blocks, and
    71                                                 applying the defined operations on these blocks iteratively. The algorithm
    72                                                 iterates through each block, expanding it, and updating the state variables
    73                                                 according to the SHA-1 specifications.
    74                                         
    75                                                 :return: hash for input message.
    76                                                 """
    77                                         
    78     19.7 MiB      0.0 MiB           1           self.padded_data = self.pad_with_zeros()
    79     19.7 MiB      0.0 MiB           1           self.blocks = self.split_blocks()
    80
    81     19.7 MiB      0.0 MiB           2           for block in self.blocks:
    82     19.7 MiB      0.0 MiB           1               expanded_block = self.expand_block(block)
    83     19.7 MiB      0.0 MiB           1               a, b, c, d, e = self.h
    84
    85     19.7 MiB      0.0 MiB          81               for i in range(80):
    86     19.7 MiB      0.0 MiB          80                   if 0 <= i < 20:
    87     19.7 MiB      0.0 MiB          20                       f = (b & c) | ((~b) & d)
    88     19.7 MiB      0.0 MiB          20                       k = 0x5A827999
    89     19.7 MiB      0.0 MiB          60                   elif 20 <= i < 40:
    90     19.7 MiB      0.0 MiB          20                       f = b ^ c ^ d
    91     19.7 MiB      0.0 MiB          20                       k = 0x6ED9EBA1
    92     19.7 MiB      0.0 MiB          40                   elif 40 <= i < 60:
    93     19.7 MiB      0.0 MiB          20                       f = (b & c) | (b & d) | (c & d)
    94     19.7 MiB      0.0 MiB          20                       k = 0x8F1BBCDC
    95     19.7 MiB      0.0 MiB          20                   elif 60 <= i < 80:
    96     19.7 MiB      0.0 MiB          20                       f = b ^ c ^ d
    97     19.7 MiB      0.0 MiB          20                       k = 0xCA62C1D6
    98
    99     19.7 MiB      0.0 MiB          80                   a, b, c, d, e = (
   100     19.7 MiB      0.0 MiB          80                       self.rotate(a, 5) + f + e + k + expanded_block[i] & 0xFFFFFFFF,
   101     19.7 MiB      0.0 MiB          80                       a,
   102     19.7 MiB      0.0 MiB          80                       self.rotate(b, 30),
   103     19.7 MiB      0.0 MiB          80                       c,
   104     19.7 MiB      0.0 MiB          80                       d,
   105                                                         )
   106
   107     19.7 MiB      0.0 MiB           1               self.h = (
   108     19.7 MiB      0.0 MiB           1                   self.h[0] + a & 0xFFFFFFFF,
   109     19.7 MiB      0.0 MiB           1                   self.h[1] + b & 0xFFFFFFFF,
   110     19.7 MiB      0.0 MiB           1                   self.h[2] + c & 0xFFFFFFFF,
   111     19.7 MiB      0.0 MiB           1                   self.h[3] + d & 0xFFFFFFFF,
   112     19.7 MiB      0.0 MiB           1                   self.h[4] + e & 0xFFFFFFFF,
   113                                                     )
   114
   115     19.7 MiB      0.0 MiB           1           return ("{:08x}" * 5).format(*self.h)
```

Unfortunately, it is not possible to measure the memory consumption of a library implementation of the `SHA-1` hashing algorithm using the `memory_profile` library.

## Running Tests
To run the tests for this code, execute the tests.py file.

```shell
python tests.py
```
This will run a series of tests to verify the correctness of the methods of the `SHA1` class for generating hash for input message.