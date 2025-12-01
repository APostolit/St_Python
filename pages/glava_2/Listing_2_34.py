# Листинг 2.34
# Кодируем - декодируем символьную строку в набор байт
a = 'Это исходная строка'
print('Исходная строка ->', a)

# Кодируем в набор байт (кодировка UTF-8)
encoded_bytes = a.encode('utf-8', 'replace')
print('Байтовая строка в кодировке utf-8 ->', encoded_bytes)

# Декодируем в кодировку ASCII
decoded_ascii = encoded_bytes.decode('ascii', 'replace')
print('Символьная строка после декодирования в ASCII ->', decoded_ascii)

# Декодируем в кодировку utf-8
decoded_utf8 = encoded_bytes.decode('utf-8', 'replace')
print('Символьная строка после декодирования в utf-8 ->', decoded_utf8)
