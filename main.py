

def separar_letras(frase):
    lista_letras = []

    for letra in frase:
        lista_letras.append(letra)

    return lista_letras

def converter_para_braille(texto):
    mapeamento_braille_brasileiro = {
        'a': '⠈', 'á': '⠘', 'à': '⠠', 'ã': '⠐',
        'b': '⠃', 'c': '⠉', 'ç': '⠡',
        'd': '⠙',
        'e': '⠑', 'é': '⠹', 'è': '⠰',
        'f': '⠋',
        'g': '⠛',
        'h': '⠓',
        'i': '⠊', 'í': '⠏',
        'j': '⠚',
        'k': '⠅',
        'l': '⠇',
        'm': '⠍',
        'n': '⠝',
        'o': '⠕', 'ó': '⠥', 'õ': '⠧', 'ô': '⠵',
        'p': '⠏',
        'q': '⠟',
        'r': '⠗',
        's': '⠎',
        't': '⠞',
        'u': '⠥', 'ú': '⠳',
        'v': '⠧',
        'w': '⠺',
        'x': '⠭',
        'y': '⠽',
        'z': '⠵',
        'A': '⠈', 'Á': '⠘', 'À': '⠠', 'Ã': '⠐',
        'B': '⠃', 'C': '⠉', 'Ç': '⠡',
        'D': '⠙',
        'E': '⠑', 'É': '⠹', 'È': '⠰',
        'F': '⠋',
        'G': '⠛',
        'H': '⠓',
        'I': '⠊', 'Í': '⠏',
        'J': '⠚',
        'K': '⠅',
        'L': '⠇',
        'M': '⠍',
        'N': '⠝',
        'O': '⠕', 'Ó': '⠥', 'Õ': '⠧', 'Ô': '⠵',
        'P': '⠏',
        'Q': '⠟',
        'R': '⠗',
        'S': '⠎',
        'T': '⠞',
        'U': '⠥', 'Ú': '⠳',
        'V': '⠧',
        'W': '⠺',
        'X': '⠭',
        'Y': '⠽',
        'Z': '⠵',
        '0': '⠚',
        '1': '⠈',
        '2': '⠂',
        '3': '⠄',
        '4': '⠈',
        '5': '⠐',
        '6': '⠠',
        '7': '⠤',
        '8': '⠬',
        '9': '⠼',
        '.': '⠲',
        ',': '⠐',
        ';': '⠒',
        ':': '⠓',
        '!': '⠮',
        '?': '⠢',
        '-': '⠤',
        '(': '⠶',
        ')': '⠶',
        '[': '⠶',
        ']': '⠶',
        '{': '⠶',
        '}': '⠶',
        '<': '⠦',
        '>': '⠴',
        '/': '⠤',
        '|': '⠸',
        '\\': '⠸',
        '@': '⠈⠹',
        '&': '⠈⠯',
        '#': '⠼⠲',
        '*': '⠐⠶⠐',
        '+': '⠤⠤',
        '=': '⠐⠤⠐',
        '%': '⠌⠈⠤⠐⠂',
        '$': '⠈⠒⠚',
        '_': '⠤⠤⠤⠤⠤⠤',
        ' ': ' ',
    }

    texto_braille = [mapeamento_braille_brasileiro.get(char.lower(), char) for char in texto]

    return ''.join(texto_braille)

if __name__ == "__main__":

    frase_ia = input("Digite uma frase: ")

    lista_separada = separar_letras(frase_ia)
    print("Lista de letras:", lista_separada)

    texto_braille = converter_para_braille(frase_ia)
    print("Texto em Braille:", texto_braille)

    lista_separada = separar_letras(texto_braille)
    print("Lista de letras braille:",lista_separada)
