def lagrange_interpolate(x, x_s, y_s, p):
    total = 0
    k = len(x_s)
    for i in range(k):
        xi, yi = x_s[i], y_s[i]
        li = 1
        for j in range(k):
            if i != j:
                xj = x_s[j]
                li *= (x - xj) * pow(xi - xj, -1, p)
                li %= p
        total += yi * li
        total %= p
    return total
