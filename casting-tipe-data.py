# belajar casting
# merubah dari satu tipe ke tipe lain

print("=========INTEGER=========")
data_int = 89;
print("data = ", data_int, ", type = ", type(data_int))

data_float = float(data_int)
data_str   = str(data_int)
data_bool  = bool(data_int)

print("data = ", data_float, ", type = ", type(data_float))
print("data = ", data_str, ", type = ", type(data_str))
print("data = ", data_bool, ", type = ", type(data_bool))

print("=========FLOAT=========")
data_float = 8.9;
print("data = ", data_float, ", type = ", type(data_float))

data_int   = int(data_float)
data_str   = str(data_float)
data_bool  = bool(data_float)

print("data = ", data_int, ", type = ", type(data_int))
print("data = ", data_str, ", type = ", type(data_str))
print("data = ", data_bool, ", type = ", type(data_bool))

print("=========BOOL=========")
data_bool = False;
print("data = ", data_bool, ", type = ", type(data_bool))

data_int   = int(data_bool)
data_str   = str(data_bool)
data_float  = float(data_bool)

print("data = ", data_int, ", type = ", type(data_int))
print("data = ", data_str, ", type = ", type(data_str))
print("data = ", data_float, ", type = ", type(data_float))

print("=========STRING=========")
data_str = "16";
print("data = ", data_str, ", type = ", type(data_str))

data_int   = int(data_str)
data_float   = float(data_str)
data_bool  = bool(data_str)

print("data = ", data_int, ", type = ", type(data_int))
print("data = ", data_float, ", type = ", type(data_float))
print("data = ", data_bool, ", type = ", type(data_bool))