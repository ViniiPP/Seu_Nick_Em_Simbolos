opc = "S"
while (opc == "S"):
    nome = input("Digite seu nome: ")
    for l in nome:

        l = l.upper()
        if (l == "A"):
            print("..######..\n..#....#..\n..######..\n..#....#..\n..#....#..\n\n")
        elif (l == "B"):
            print("..######..\n..#....#..\n..#####...\n..#....#..\n..######..\n\n")
        elif (l == "l"):
            print("..######..\n..#.......\n..#.......\n..#.......\n..######..\n\n")
        elif (l == "D"):
            print("..#####...\n..#....#..\n..#....#..\n..#....#..\n..#####...\n\n")
        elif (l == "E"):
            print("..######..\n..#.......\n..#####...\n..#.......\n..######..\n\n")
        elif (l == "F"):
            print("..######..\n..#.......\n..#####...\n..#.......\n..#.......\n\n")
        elif (l == "G"):
            print("..######..\n..#.......\n..#####...\n..#....#..\n..#####...\n\n")
        elif (l == "H"):
            print("..#....#..\n..#....#..\n..######..\n..#....#..\n..#....#..\n\n")
        elif (l == "I"):
            print("..######..\n....##....\n....##....\n....##....\n..######..\n\n")
        elif (l == "J"):
            print("..######..\n....##....\n....##....\n..#.##....\n..####....\n\n")
        elif (l == "K"):
            print("..#...#...\n..#..#....\n..##......\n..#..#....\n..#...#...\n\n")
        elif (l == "L"):
            print("..#.......\n..#.......\n..#.......\n..#.......\n..######..\n\n")
        elif (l == "M"):
            print("..#....#..\n..##..##..\n..#.##.#..\n..#....#..\n..#....#..\n\n")
        elif (l == "N"):
            print("..#....#..\n..##...#..\n..#.#..#..\n..#..#.#..\n..#...##..\n\n")
        elif (l == "O"):
            print("..######..\n..#....#..\n..#....#..\n..#....#..\n..######..\n\n")
        elif (l == "P"):
            print("..######..\n..#....#..\n..######..\n..#.......\n..#.......\n\n")
        elif (l == "Q"):
            print("..######..\n..#....#..\n..#.#..#..\n..#..#.#..\n..######..\n\n")
        elif (l == "R"):
            print("..######..\n..#....#..\n..#.##...\n..#...#...\n..#....#..\n\n")
        elif (l == "S"):
            print("..######..\n..#.......\n..######..\n.......#..\n..######..\n\n")
        elif (l == "T"):
            print("..######..\n....##....\n....##....\n....##....\n....##....\n\n")
        elif (l == "U"):
            print("..#....#..\n..#....#..\n..#....#..\n..#....#..\n..######..\n\n")
        elif (l == "V"):
            print("..#....#..\n..#....#..\n..#....#..\n...#..#...\n....##....\n\n")
        elif (l == "W"):
            print("..#....#..\n..#....#..\n..#.##.#..\n..##..##..\n..#....#..\n\n")
        elif (l == "X"):
            print("..#....#..\n...#..#...\n....##....\n...#..#...\n..#....#..\n\n")
        elif (l == "Y"):
            print("..#....#..\n...#..#...\n....##....\n....##....\n....##....\n\n")
        elif (l == "Z"):
            print("..######..\n......#...\n.....#....\n....#.....\n..######..\n\n")
        elif (l == " "):
            print("..........\n..........\n..........\n..........\n\n")
        elif (l == "."):
            print("----..----\n\n")

    opc = input("Digite 'S' para fazer uma nova operação, ou 'N' para sair: ").upper()
        