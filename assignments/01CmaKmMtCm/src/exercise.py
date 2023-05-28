def main():
    # Escribe tu código abajo de esta línea
    n = int(input('Introduce los cm: '))
    kilometros = n // 10000
    metros = (n // 100) % 1000
    centimetros = n % 100
    print("Resultado:")
    if kilometros != 0 :
        print("km:", kilometros)
    if metros != 0:
        print("m:", metros)
    if centimetros != 0:
            print("cm:", centimetros)

if __name__ == '__main__':
    main()
