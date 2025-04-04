import ROZLAND_MRK2_Lib as roz

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import artifact as ark


while True:
    print(roz.main(input("enter: ")))