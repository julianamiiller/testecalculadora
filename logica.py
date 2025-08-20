valores = [0, 1]

print("a\tb\ta and b\ta or b\tnot a\tnot b")
print("-" * 50)

for a in valores:
    for b in valores:

        a_bool = bool(a)
        b_bool = bool(b)

        resultado_and = int(a_bool and b_bool)
        resultado_or = int(a_bool or b_bool)
        not_a = int(not a_bool)
        not_b = int(not b_bool)

        print(f"{a}\t{b}\t{resultado_and}\t{resultado_or}\t{not_a}\t{not_b}")
