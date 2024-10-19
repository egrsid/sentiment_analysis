import pickle
import argparse

def main():
    # Создаем парсер для аргументов командной строки
    parser = argparse.ArgumentParser(description="Пример обработки аргументов")

    # Добавляем аргумент --text, используя nargs для приема нескольких слов
    parser.add_argument('--text', type=str, nargs='+', help='Текстовая строка для обработки (через пробел)')

    # Парсим аргументы
    args = parser.parse_args()
    # Проверяем, что аргумент передан
    if args.text:
        message = ' '.join(args.text)
        with open(fr'result_model_pileline.pickle', 'rb') as handle:
            model = pickle.load(handle)

        proba = model.predict_proba([message])
        predict = model.predict([message])
        print(f"[{message}]: {'good' if predict else 'bad'} mood with the probability of {max(proba[0])}")
    else:
        print("Аргумент --text не был передан")
main()