# Sandbox file for quick and dirty tests
# -----------------------------------------------------------------------------

# First, moving path to src directory, allowing for direct import of package

import os
import sys

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, "src"))

# -----------------------------------------------------------------------------
# Now we can import minimalpackage as per the below; without the above, we
# would have needed to use: import src.minimalpackage as minimalpackage

import minimalpackage

# -----------------------------------------------------------------------------
# Some tests:

# version
print("# version")
print()
print(f"minimalpackage version: {minimalpackage.__version__}")
print()

# functions
print("# functions")
print()
print(f"minimalpackage.module1.function1(): {minimalpackage.module1.function1()}")
print(f"minimalpackage.module2.function2(): {minimalpackage.module2.function2()}")
print()

# classes
c1 = minimalpackage.module1.Class1()
c2 = minimalpackage.module2.Class2()
print("# classes")
print()
print("c1 = minimalpackage.module1.Class1()")
print("c2 = minimalpackage.module2.Class2()")
print()
print(f"c1.some_method(): {c1.some_method()}")
print(f"c1.some_attribute: {c1.some_attribute}")
print(f"c2.some_method(): {c2.some_method()}")
print(f"c2.some_attribute: {c2.some_attribute}")
