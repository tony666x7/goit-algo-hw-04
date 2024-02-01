def get_cats_info(path):
    cats_info_list =[]

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')

                cat_info = {
                    "id": parts[0],
                    "name": parts[1],
                    "age": parts[2]
                }

                cats_info_list.append(cat_info)



    except FileNotFoundError:
        print(f"Помилка: Файл '{path}' не знайдено. ") 
    except Exception as e:
        print(f"Помилка при обробці файлу: {e}")

    return cats_info_list




cats_info = get_cats_info("/Users/antonstoliarchuk/Desktop/My_repo/goit-algo-hw-04/ex2/cats_list.txt")
print(cats_info)