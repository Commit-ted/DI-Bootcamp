# one line of code
print(("Hello world\n" * 4) + ("I love python\n" * 4), end ="")

# of line with loops
exec(''.join([f'print("{line}")\n' for line in ["Hello world"]*4 + ["I love python"]*4]))
