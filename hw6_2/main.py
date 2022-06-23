import module1

answer = 0
while True:
    answer = int(input('\nChoose an option:\n'
          '1 - read names of persons\n'
          '2 - read emails of persons\n'
          '3 - read names of files\n'
          '4 - read codes of colors\n'
          '5 - exit\n'
                   'enter your choise: '))

    if answer == 1:
        module1.read_names()

    if answer == 2:
          module1.read_emails()

    if answer == 3:
          module1.read_names_of_files()

    if answer == 4:
        module1.read_codes_of_colors()

    if answer == 5:
          print(f'bye...')
          break






