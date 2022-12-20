# the function calculated the finite product

def endProduct(s, e):
    product = 0
    for i in range(s, e):
        product = product + e
    if s < 0 or e < 0:
        return 0
    elif s == 0 or e == 0:
        return 0
    if e < s:
        s, e = e, s
    print(product)


# main ---------------------------------------------------------------------

endProduct(1, 6)
