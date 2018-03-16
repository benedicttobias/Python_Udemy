temperatures = [10, -20, -289, 100]
def c_to_f(c):
    if c >= -273.15:
        f = c* 9/5 + 32
        return str(f)
    else:
        return ""

with open("output.txt", "w") as myfile:
    for t in temperatures:
        myfile.write(str(c_to_f(t)) + "\n")
