with open('resource/input.txt', 'w', encoding='utf-8') as file:
    file.write("Начало\n")
    file.write("Это строка здесь просто так\n")
    file.write("Очень важная строка\n")
    file.write("Перевод\n")

with open('resource/input.txt', 'r') as file:
    content = file.readlines()
    num_lines = len(content)
    words = sum(len(line.split()) for line in content)

with open("resource/statistics.txt", "w", encoding='utf-8') as file:
    file.write(str(f"количество строк: {num_lines}"))
    file.write("\n")
    file.write(str(f"количество слов: {words}"))
