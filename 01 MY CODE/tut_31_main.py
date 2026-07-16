import tut_31_1_main as e
print(e.int(42))
# Got it. The problem is the file names.

# In Python, module names (the part after import) must follow identifier rules:
#
# Only letters, digits, and _
#
# Cannot start with a digit
#
# Cannot contain ., spaces, or special characters
#
# Your files are named:
#
# 31.1ifmain.py
#
# 31.ifmain.py
#
# Those names are invalid as importable modules. That’s why your editor shows red lines and autocomplete doesn’t work.