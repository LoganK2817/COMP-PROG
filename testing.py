import ROZLAND as roz



codedPhrase = "pnhoe"

decodeKey = 2

buffer = ""

buffer1 = ""

for run in range(decodeKey):
    if run == 0:
        buffer = roz.main(codedPhrase)
    else:
        buf = roz.main(buffer)
        buffer = buf
        
print(buffer)