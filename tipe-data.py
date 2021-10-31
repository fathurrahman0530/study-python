# jenis tipe data pada python

# tipe data : angka bulat (integer)
data_integer = 5
print("data : ", data_integer)
print("Bertipe data : ", type(data_integer))

# tipe data : angka dan koma (float)
data_float = 2.5
print("data : ", data_float)
print("Bertipe data : ", type(data_float))

# tipe data : kumpulan karakter (string)
data_string = "Fathur Rahman"
print("data : ", data_string)
print("Bertipe data : ", type(data_string))

# tipe data : biner true / false (boolean)
data_bool = True
print("data : ", data_bool)
print("Bertipe data : ", type(data_bool))

## tipe data : khusus

# bilangan kompleks
data_complex = complex(7, 3)
print("data : ", data_complex)
print("bertipe data : ", type(data_complex))

# tipe data dari bahasa C
from ctypes import c_double, c_char

data_c_double = c_double(12.5)
print("data : ", data_c_double)
print("bertipe data : ", type(data_c_double))