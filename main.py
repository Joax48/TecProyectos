from typing import List, Tuple

values = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
values_l = [2,3,4,5,6,7,8,9,10,10,10,11]

def is_straight_flush(hand: List[str]) -> Tuple[bool, List[int]]:
    # Verifica si la mano es un flush y un straight al mismo tiempo
    es_flush, _ = is_flush(hand)
    es_straight, valores_cartas = is_straight(hand)

    # Si la mano es un flush y un straight, es un straight flush
    if es_flush and es_straight:
        return True, valores_cartas

    # Si no es un straight flush, devuelve False y una lista vacía
    return False, []

def is_four_of_a_kind(hand: List[str]) -> Tuple[bool, List[int]]:
    # Contador para contar la ocurrencia de cada valor de carta en la mano
    contador_valores = {}

    # Determina la ocurrencia de cada valor de carta en la mano
    for carta in hand:
        valor = carta[:-1]
        contador_valores[valor] = contador_valores.get(valor, 0) + 1

    # Busca un valor que tenga cuatro ocurrencias en la mano
    for valor, cantidad in contador_valores.items():
        if cantidad == 4:
            # Si se encuentra un valor con cuatro ocurrencias, determina los valores de las cartas en la mano
            valores_cartas = [values.index(carta[:-1]) for carta in hand]
            # Ordena los valores de manera descendente
            valores_cartas.sort(reverse=True)
            return True, valores_cartas

    # Si no se encuentra ningún valor con cuatro ocurrencias, devuelve False y una lista vacía
    return False, []


def is_full_house(hand: List[str]) -> Tuple[bool, List[int]]:
    # Contador para contar la ocurrencia de cada valor de carta en la mano
    contador_valores = {}

    # Determina la ocurrencia de cada valor de carta en la mano
    for carta in hand:
        valor = carta[:-1]
        contador_valores[valor] = contador_valores.get(valor, 0) + 1

    # Busca un trío y un par en el contador de valores
    trio = None
    par = None
    for valor, cantidad in contador_valores.items():
        if cantidad == 3:
            trio = values.index(valor)
        elif cantidad == 2:
            par = values.index(valor)

    # Si se encuentra un trío y un par, es un full house
    if trio is not None and par is not None:
        # Retorna los valores ordenados de manera descendente
        return True, [trio, par]

    # Si no se encuentra un trío y un par, no es un full house
    return False, []



def is_flush(hand: List[str]) -> Tuple[bool, List[int]]:
    # Verifica si todas las cartas en la mano tienen el mismo palo
    palo = hand[0][-1]
    for carta in hand[1:]:
        if carta[-1] != palo:
            # Si encuentra una carta con un palo diferente, la mano no es un Flush
            return False, []

    # Si todas las cartas tienen el mismo palo, determina los valores de las cartas en la mano
    valores_cartas = [values.index(carta[:-1]) for carta in hand]
    # Ordena los valores de manera descendente
    valores_cartas.sort(reverse=True)

    # Retorna True si es un Flush y la lista de valores de las cartas
    return True, valores_cartas


def is_straight(hand: List[str]) -> Tuple[bool, List[int]]:
    # Ordena los valores de las cartas en la mano
    valores_cartas = sorted([values.index(carta[:-1]) for carta in hand])

    # Verifica si las diferencias entre los valores son todas iguales a 1
    for i in range(len(valores_cartas) - 1):
        if valores_cartas[i + 1] - valores_cartas[i] != 1:
            return False, []

    # Si las diferencias son todas iguales a 1, es una escalera
    # Devuelve True y la lista de valores de las cartas ordenados de manera descendente
    valores_cartas.sort(reverse=True)
    return True, valores_cartas


def is_three_of_a_kind(hand: List[str]) -> Tuple[bool, List[int]]:
    # Contador para contar la ocurrencia de cada valor de carta en la mano
    contador_valores = {}

    # Determina la ocurrencia de cada valor de carta en la mano
    for carta in hand:
        valor = carta[:-1]
        contador_valores[valor] = contador_valores.get(valor, 0) + 1

    # Busca un valor de carta que aparezca tres veces (trío)
    for valor, cantidad in contador_valores.items():
        if cantidad == 3:
            # Si se encuentra un trío, determina los valores de las tres cartas
            valores_cartas = [values.index(carta[:-1]) for carta in hand if carta[:-1] == valor]
            # Ordena los valores de manera descendente
            valores_cartas.sort(reverse=True)
            return True, valores_cartas

    # Si no se encuentra ningún trío, devuelve False y una lista vacía
    return False, []



def is_two_pairs(hand: List[str]) -> Tuple[bool, List[int]]:
    # Contador para contar la ocurrencia de cada valor de carta en la mano
    contador_valores = {}

    # Determina la ocurrencia de cada valor de carta en la mano
    for carta in hand:
        valor = carta[:-1]
        contador_valores[valor] = contador_valores.get(valor, 0) + 1

    # Encuentra los valores que aparecen dos veces (pares)
    pares = [valor for valor, cantidad in contador_valores.items() if cantidad == 2]

    # Verifica que haya exactamente dos pares en la mano
    if len(pares) == 2:
        # Ordena los pares encontrados en orden descendente
        pares.sort(key=lambda x: values.index(x), reverse=True)
        valores_cartas = [values.index(carta[:-1]) for carta in hand]

        # Encuentra la carta restante
        carta_restante = [values.index(carta[:-1]) for carta in hand if carta[:-1] not in pares]
        # Ordena los valores de manera descendente
        carta_restante.sort(reverse=True)

        return True, pares + carta_restante

    # Si no se encuentran dos pares, devuelve False y una lista vacía
    return False, []


def is_pair(hand: List[str]) -> Tuple[bool, List[int]]:
    # Contador para contar la ocurrencia de cada valor de carta en la mano
    contador_valores = {}

    # Determina la ocurrencia de cada valor de carta en la mano
    for carta in hand:
        valor = carta[:-1]
        contador_valores[valor] = contador_valores.get(valor, 0) + 1

    # Busca un par de cartas con el mismo valor
    for valor, cantidad in contador_valores.items():
        if cantidad == 2:
            # Si se encuentra un par, determina los valores de las cartas en la mano
            valores_cartas = [values.index(carta[:-1]) for carta in hand]
            # Ordena los valores de manera descendente
            valores_cartas.sort(reverse=True)
            return True, valores_cartas

    # Si no se encuentra ningún par, devuelve False y una lista vacía
    return False, []


def is_high_card(hand: List[str]) -> Tuple[bool, List[int]]:
    # Determina los valores de las cartas en la mano
    valores_cartas = [values.index(carta[:-1]) for carta in hand]
    # Ordena los valores de las cartas de manera descendente
    valores_cartas.sort(reverse=True)

    # Retorna True junto con la lista de valores de las cartas
    return True, valores_cartas

def tryCards(hand: List[str]) -> Tuple[int, List[int]]:

    es_straight_flush, valores_cartas_str = is_straight_flush(hand)
    if es_straight_flush:
        #        print("Es straight flush")
        #        print("Valores de las cartas:", valores_cartas_str)
        return 9,valores_cartas_str

    es_four_kind, valoresFour = is_four_of_a_kind(hand)
    if es_four_kind:
        #        print("Es four kind")
        #        print("Valores de las cartas:", valoresFour)
        return 8,valoresFour

    es_full_house, valores_full_house = is_full_house(hand)
    if es_full_house:
        #        print("Es full house")
        #        print("Valores de las cartas:", valores_full_house)
        return 7,valores_full_house

    es_flush, valores_cartas = is_flush(hand)
    if es_flush:
        #        print("Es Flush")
        #        print("Valores de las cartas:", valores_cartas)
        return 6,valores_cartas

    es_straight, valor_es_straight = is_straight(hand)
    if es_straight:
        #        print("Es straight ")
        #        print("Valores de las cartas:", valor_es_straight)
        return 5,valor_es_straight

    es_three,valores_cartas_three = is_three_of_a_kind(hand)
    if es_three:
        #        print("Es three")
        #        print("Valores de las cartas:", valores_cartas_three)
        return 4,valores_cartas_three

    es_dos_pairs, valores_cartas_two_pairs = is_two_pairs(hand)
    if es_dos_pairs:
        #        print("Es two pair")
        #        print("Valores de las cartas:", valores_cartas_two_pairs)
        return 3,valores_cartas_two_pairs

    es_pair, valores_cartas_pair = is_pair(hand)
    if es_pair:
        #        print("Es pair")
        #        print("Valores de las cartas:", valores_cartas_pair)
        return 2,valores_cartas_pair

    es_high_card, valores_high = is_high_card(hand)
    if es_high_card:
       # print("Es high card")
       # print("Valores de las cartas:", valores_high)
        return 1,valores_high

    # Si no es ninguno de los casos anteriores, devuelve 0
    return (999,[999])

def resolve_tie(case: int, hand1: List[int], hand2: List[int], is_flush: bool) -> int:
    try:
        if case == 1:  # High Card
            for i in range(len(hand1)):
                if hand1[i] > hand2[i]:
                    return 1
                if hand1[i] < hand2[i]:
                    return 2
            return 3  # Empate
        elif case == 2:  # Pair
            # Obtener el valor del par para cada mano
            pair_val_hand1 = max(hand1, key=hand1.count)
            pair_val_hand2 = max(hand2, key=hand2.count)
            # Si los valores del par son diferentes, determinar el ganador
            if pair_val_hand1 != pair_val_hand2:
                return 1 if values.index(pair_val_hand1) > values.index(pair_val_hand2) else 2
            # Si los valores del par son iguales, determinar el ganador según las cartas restantes
            else:
                # Obtener las cartas que no forman el par para cada mano
                remaining_hand1 = [card for card in hand1 if card[:-1] != pair_val_hand1]
                remaining_hand2 = [card for card in hand2 if card[:-1] != pair_val_hand2]
                # Comparar las cartas restantes en orden descendente
                for i in range(len(remaining_hand1)):
                    if values.index(remaining_hand1[i][:-1]) > values.index(remaining_hand2[i][:-1]):
                        return 1
                    elif values.index(remaining_hand1[i][:-1]) < values.index(remaining_hand2[i][:-1]):
                        return 2
            return 3  # Empate
        elif case == 3:  # Two Pairs
            # Obtener los valores de los dos pares para cada mano
            pairs_hand1 = [card for card in hand1 if hand1.count(card[:-1]) == 2]
            pairs_hand2 = [card for card in hand2 if hand2.count(card[:-1]) == 2]
            # Ordenar los pares de cada mano
            pairs_hand1.sort(key=lambda x: values.index(x[:-1]), reverse=True)
            pairs_hand2.sort(key=lambda x: values.index(x[:-1]), reverse=True)
            # Comparar los pares más altos
            if values.index(pairs_hand1[0][:-1]) != values.index(pairs_hand2[0][:-1]):
                return 1 if values.index(pairs_hand1[0][:-1]) > values.index(pairs_hand2[0][:-1]) else 2
            # Si los pares más altos son iguales, comparar los pares más bajos
            elif values.index(pairs_hand1[1][:-1]) != values.index(pairs_hand2[1][:-1]):
                return 1 if values.index(pairs_hand1[1][:-1]) > values.index(pairs_hand2[1][:-1]) else 2
            # Si ambos pares son iguales, comparar la quinta carta
            else:
                fifth_card_hand1 = [card for card in hand1 if card[:-1] not in pairs_hand1]
                fifth_card_hand2 = [card for card in hand2 if card[:-1] not in pairs_hand2]
                if values.index(fifth_card_hand1[0][:-1]) != values.index(fifth_card_hand2[0][:-1]):
                    return 1 if values.index(fifth_card_hand1[0][:-1]) > values.index(fifth_card_hand2[0][:-1]) else 2
            return 3  # Empate
        elif case == 4:  # Three of a Kind
            # Obtener el valor del trío para cada mano
            trio_val_hand1 = max(hand1, key=hand1.count)
            trio_val_hand2 = max(hand2, key=hand2.count)
            # Comparar los valores del trío
            if trio_val_hand1 != trio_val_hand2:
                return 1 if values.index(trio_val_hand1) > values.index(trio_val_hand2) else 2
            # Si los valores del trío son iguales, comparar las cartas restantes
            else:
                remaining_hand1 = [card for card in hand1 if card[:-1] != trio_val_hand1]
                remaining_hand2 = [card for card in hand2 if card[:-1] != trio_val_hand2]
                for i in range(len(remaining_hand1)):
                    if values.index(remaining_hand1[i][:-1]) != values.index(remaining_hand2[i][:-1]):
                        return 1 if values.index(remaining_hand1[i][:-1]) > values.index(remaining_hand2[i][:-1]) else 2
            return 3  # Empate
        elif case == 5:  # Straight
            # Compara las manos directamente, ya que la carta más alta decide el ganador
            if hand1[0] != hand2[0]:
                return 1 if hand1[0] > hand2[0] else 2
            return 3  # Empate
        elif case == 6:  # Flush
            # Si es un flush, utiliza la función resolve_tie para High Card
            if is_flush:
                return resolve_tie(1, hand1, hand2, False)
            return 3  # Empate
        elif case == 7:  # Full House
            trio1= values_l[hand1[0]-1]
            trio2= values_l[hand2[0]-1]
            doble1 = values_l[hand1[1]-1]
            doble2 = values_l[hand2[1]-1]
            if trio1!=trio2:
                return 1 if trio1>trio2 else 2
            elif doble1!=doble2:
                return 1 if doble1 > doble2 else 2
            else:
                return 3  # Empate
        elif case == 8:  # Four of a Kind
            # Obtener el valor del cuarteto para cada mano
            cuarteto_val_hand1 = max(hand1, key=hand1.count)
            cuarteto_val_hand2 = max(hand2, key=hand2.count)
            # Comparar los valores del cuarteto
            if cuarteto_val_hand1 != cuarteto_val_hand2:
                return 1 if values.index(cuarteto_val_hand1) > values.index(cuarteto_val_hand2) else 2
            # Si los valores del cuarteto son iguales, comparar la quinta carta
            else:
                remaining_hand1 = [card for card in hand1 if card[:-1] != cuarteto_val_hand1]
                remaining_hand2 = [card for card in hand2 if card[:-1] != cuarteto_val_hand2]
                return 1 if values.index(remaining_hand1[0][:-1]) > values.index(remaining_hand2[0][:-1]) else 2
        elif case == 9:  # Straight Flush
            # Compara las manos directamente, ya que la carta más alta decide el ganador
            if hand1[0] != hand2[0]:
                return 1 if hand1[0] > hand2[0] else 2
            return 3  # Empate
        else:
            return 0  # Caso no reconocido

    except ValueError as e:
        print("Error:", e)
        return 0  # Devuelve 0 en caso de error


def leer_cartas(archivo_entrada, archivo_salida):
    with open(archivo_entrada, 'r') as file_in, open(archivo_salida, 'w') as file_out:
        for linea in file_in:
            cartas = linea.split()
            mitad = len(cartas) // 2
            score1, list1 = tryCards(cartas[:mitad])
            score2, list2 = tryCards(cartas[mitad:])

            if score1 > score2:
                file_out.write("El negro gana.\n")
            elif score1 < score2:
                file_out.write("El blanco gana.\n")
            else:
                resolution = resolve_tie(score1, list1, list2, False)
                if resolution == 1:
                    file_out.write("El negro gana.\n")
                elif resolution == 2:
                    file_out.write("El blanco gana.\n")
                else:
                    file_out.write("Empate.\n")



def main():
    archivo_entrada = "problema.txt"  # Nombre del archivo de entrada
    archivo_salida = "solucion.txt"  # Nombre del archivo de salida
    leer_cartas(archivo_entrada, archivo_salida)


if __name__ == "__main__":
    main()