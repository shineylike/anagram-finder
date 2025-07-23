from collections import defaultdict

def gaseste_anagrame(nume_fisier):
    grupuri = defaultdict(list)

    with open(nume_fisier, 'r') as fisier:
        for linie in fisier:
            cuvant = linie.strip()
            cheie = ''.join(sorted(cuvant))
            grupuri[cheie].append(cuvant)

    for grup in grupuri.values():
        print(' '.join(grup))

if __name__ == "__main__":
    gaseste_anagrame("sample.txt")
