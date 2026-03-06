import ctypes
import os

lib_path = os.path.abspath("my_lib.so")
my_lib = ctypes.CDLL(lib_path)
my_lib.add_integers.argtypes = [ctypes.c_int, ctypes.c_int]
my_lib.add_integers.restype = ctypes.c_int

# Call the function!
result = my_lib.add_integers(int(input()), int(input()))

print(f"Python says: The result is {result}")
