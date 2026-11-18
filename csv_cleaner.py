import pandas as pd

def clean_csv(input_file, output_file):
    """
    Читает CSV, удаляет дубликаты и пустые строки, фильтрует по цене > 1000.
    """
    try:
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        print("Файл не найден!")
        return

    # Удаляем дубликаты
    df = df.drop_duplicates()
    
    # Удаляем строки, где все значения пустые (NaN)
    df = df.dropna(how='all')
    
    # Пример фильтрации: оставляем только строки, где цена > 1000
    if 'price' in df.columns:
        df = df[df['price'] > 1000]
    
    # Сохраняем результат
    df.to_csv(output_file, index=False)
    print(f"Готово! Очищенные данные сохранены в {output_file}")

if __name__ == '__main__':
    # Пример: input.csv должен лежать в папке со скриптом
    clean_csv('input.csv', 'output.csv')
