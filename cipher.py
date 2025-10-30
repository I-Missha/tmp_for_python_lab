def caesar_cipher(text, shift, language):

    if language == 'ru':
        alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
        alphabet_upper = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    else:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    result = ""

    for char in text:
        if char in alphabet:
            old_index = alphabet.index(char)
            new_index = (old_index + shift) % len(alphabet)
            result += alphabet[new_index]

        elif char in alphabet_upper:
            old_index = alphabet_upper.index(char)
            new_index = (old_index + shift) % len(alphabet_upper)
            result += alphabet_upper[new_index]

        else:
            result += char

    return result


print("Шифрование текста шифром Цезаря")

input_file = input("Введите путь к файлу с текстом: ")
while True:
    try:
        shift = int(input("Введите сдвиг (целое число): "))
        break
    except:
        print("Ошибка: введите целое число!")

while True:
    language = input("Введите язык (ru - русский, en - английский): ").lower()
    if language in ['ru', 'en']:
        break
    print("Ошибка: введите 'ru' или 'en'!")

try:
    text = open(input_file, 'r', encoding='utf-8').read()

except:
    print("Ошибка при чтении файла")
    exit()

encrypted_text = caesar_cipher(text, shift, language)

output_file = "encrypted_" + input_file.split("/")[-1].split("\\")[-1]

try:
    file = open(output_file, 'r', encoding='utf-8').write(encrypted_text)

    print(f"Текст успешно зашифрован и сохранен в файл: {output_file}")
except Exception as e:
    print(f"Ошибка при записи файла: {e}")
