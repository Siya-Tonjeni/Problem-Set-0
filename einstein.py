def calculate_energy(mass):
    return mass * (300000000 ** 2)

def main():
    mass = float(input("m: "))
    energy = calculate_energy(mass)
    print(f"E: {energy:.0f}")

main()