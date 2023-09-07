def magic_calculation(a, b):
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)

# Compile the function into bytecode
compiled_code = compile(magic_calculation.__code__, filename="", mode="exec")

# Use the dis module to disassemble the bytecode
import dis
dis.dis(compiled_code)
