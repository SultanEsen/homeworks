def questionnaire():
    q1 = "Какую функцию выполняет запрос SQL CREATE?\n" + input("Какую функцию выполняет запрос SQL CREATE?\nВаш ответ: ")
    q2 = "\nКакую функцию выполняет запрос SQL INSERT?\n" + input("Какую функцию выполняет запрос SQL INSERT?\nВаш ответ: ")
    q3 = "\nКакую функцию выполняет запрос SQL SELECT?\n" + input("Какую функцию выполняет запрос SQL SELECT?\nВаш ответ: ")
    q4 = "\nКакую функцию выполняет запрос SQL UPDATE?\n" + input("Какую функцию выполняет запрос SQL UPDATE?\nВаш ответ: ")
    q5 = "\nКакую функцию выполняет запрос SQL DROP?\n" + input("Какую функцию выполняет запрос SQL DROP?\nВаш ответ: ")
    with open('docs.txt', 'w', encoding='utf-8') as f:
        f.write(f'{q1}\n{q2}\n{q3}\n{q4}\n{q5}')


questionnaire()