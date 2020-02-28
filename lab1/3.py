from scipy import stats
with open('input.txt', 'r') as f:
    file_content = f.read()

data = list(map(lambda x: float(x), file_content.replace('\n', ' ').replace(',', '.').split(' ')))

statistic, p_value = stats.normaltest(data)
alpha = 0.025

print(f'statistics: {statistic}\np_value: {p_value}')

print(f'Sample looks {"not " if p_value < alpha else ""}Gaussian')
print(f'Нулевую гипотезу опровергнуть {"" if p_value < alpha else "не "}удалось')