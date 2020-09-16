a = 1
b = 2
print(a)
print(B)




pylint pylint_ut.py
************* Module pylint_ut
pylint_ut.py:4:0: C0304: Final newline missing (missing-final-newline)
pylint_ut.py:1:0: C0114: Missing module docstring (missing-module-docstring)
pylint_ut.py:1:0: C0103: Constant name "a" doesn't conform to UPPER_CASE naming style (invalid-name)
pylint_ut.py:2:0: C0103: Constant name "b" doesn't conform to UPPER_CASE naming style (invalid-name)
pylint_ut.py:4:6: E0602: Undefined variable 'B' (undefined-variable)

-------------------------------------
Your code has been rated at -12.50/10