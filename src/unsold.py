import numpy as np

def calculate_top_div_bot(a, b, x, y):
    top = (a - x) * (b - y)
    bot = (5 * a - 150) * (5 * b - 150)
    return top / bot

def calculate_z_probability(part1):
    i, start = 1, 0
    zLaw = []

    for x in range(2, 11):
        res = sum(part1[start:start+4*i:4])
        zLaw.append(res)
        start += 1 if x < 6 else 5
        i += 1 if x < 6 else -1
    return zLaw

def unsold(a, b):
    part1 = [calculate_top_div_bot(int(a), int(b), x * 10, y * 10) for y in range(1, 6) for x in range(1, 6)]
    y_l = [sum(part1[i:i+5]) for i in range(0, 25, 5)]
    x_l = [sum(part1[i:i+1]) + sum(part1[i+5:i+6]) + sum(part1[i+10:i+11]) + sum(part1[i+15:i+16]) + sum(part1[i+20:i+21]) for i in range(0, 5)]
    z_law = calculate_z_probability(part1)
    e_x = sum(i * 10 * x_l[i - 1] for i in range(1, 6))
    e_y = sum(i * 10 * y_l[i - 1] for i in range(1, 6))
    e_z = e_x + e_y
    v_x = sum((i * 10 - e_x) ** 2 * x_l[i - 1] for i in range(1, 6))
    v_y = sum((i * 10 - e_y) ** 2 * y_l[i - 1] for i in range(1, 6))
    v_z = v_x + v_y
    print("------------------------------------------------------------------------------")
    print("\tX=10\tX=20\tX=30\tX=40\tX=50\tY law")
    for i in range(5):
        print(f"Y={10*(i+1)}\t" + "\t".join(f"{part1[j+5*i]:.3f}" for j in range(5)) + f"\t{y_l[i]:.3f}")
    print("X law\t" + "\t".join(f"{x_l[i]:.3f}" for i in range(5)))
    print("------------------------------------------------------------------------------")
    print("z\t20\t30\t40\t50\t60\t70\t80\t90\t100")
    print("p(Z=z)\t" + "\t".join(f"{z_law[i]:.3f}" for i in range(9)))
    print("------------------------------------------------------------------------------")
    print(f"expected value of X:\t{e_x:.1f}")
    print(f"variance of X:\t\t{v_x:.1f}")
    print(f"expected value of Y:\t{e_y:.1f}")
    print(f"variance of Y:\t\t{v_y:.1f}")
    print(f"expected value of Z:\t{e_z:.1f}")
    print(f"variance of Z:\t\t{v_z:.1f}")
    print("------------------------------------------------------------------------------")
