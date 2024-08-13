import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    # animals = animals[animals['weight'] > 100]
    # animals.sort_values(by='weight', ascending=False, inplace=True)
    # animals.drop(columns=['species', 'age', 'weight'], inplace=True)
    # return animals
    return animals[animals['weight'] > 100].sort_values('weight', ascending=False)[
        ['name']
    ]