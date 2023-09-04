import dis

def magic_calculation(a, b):
    result = 98
    result += a
    result += b
    result = result ** b
    result += a + b
    return result

# Disassemble and print the bytecode instructions
bytecode = dis.Bytecode(magic_calculation)
for instr in bytecode:
    print(f"{instr.offset:2} {instr.opcode:4} {instr.opname:<20}{instr.argrepr}")
