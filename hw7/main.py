def questionnaire():
    q1 = "Что такое структуры данных?\n" + input("Что такое структуры данных?\nВаш ответ: ")
    q2 = "\nЗачем они нужны?\n" + input("Зачем они нужны?\nВаш ответ: ")
    q3 = "\nЧто такое Hash Map?\n" + input("Что такое Hash Map?\nВаш ответ: ")
    q4 = "\nЧто такое Linked List?\n" + input("Что такое Linked List?\nВаш ответ: ")
    q5 = "\nВ каких случаях использовать Linked List и Hash Map?\n" + input("В каких случаях использовать Linked List и Hash Map?\nВаш ответ: ")
    with open('docs.txt', 'w', encoding='utf-8') as f:
        f.write(f'{q1}\n{q2}\n{q3}\n{q4}\n{q5}')


questionnaire()
