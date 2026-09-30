def mystery(n):
    if n == 0:
        print("Done")
    else:
        print("Start", n)
        mystery(n - 1)
        print("End")
mystery(3)
