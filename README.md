# pqc-python
This repository contains examples for using postquantum cryptography NIST algorithms based on liboqs-python.
This module provides a Python 3 interface to liboqs (https://github.com/open-quantum-safe/liboqs).

1. Compile liboqs (https://github.com/open-quantum-safe/liboqs-python) and copy liboqs.so.* to /usr/local/lib   

2. python3 kem.py

You can choose different KEM algoritms and simulate a communication between two parts (generation public-private key, encapsulating and decap the secret shared)
