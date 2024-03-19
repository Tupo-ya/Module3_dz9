import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(open('ds_salaries.csv', 'rb'), sep=',')
#? Выводим первые 5 строк
print(df.head())

#? Состовляем barplot
df_grouped = df.groupby('job_title')['salary_in_usd'].mean().reset_index()
plt.figure(figsize=(16, 8))
sns.barplot(x='job_title', y='salary_in_usd', data=df_grouped)
plt.xticks(rotation=45)
plt.xlabel('Профессия')
plt.ylabel('Доход в USD')
plt.title('Уровень дохода')
plt.grid(True)
plt.tight_layout()
plt.show()


#? Строим линейную диаграмму по столбам
plt.figure(figsize=(15, 8))
for column in df.columns:
#     # ? Заносим значения только из чисел
    if df[column].dtype in [np.int64, np.float64]:
        plt.plot(df.index, df[column], label=column)
plt.ylabel('Значение')
plt.title('Линейные графики')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

#? Диаграмма рассеяния
# ? Ещё лучше я сделать не могу. Там слишком много профессий
plt.figure(figsize=(15, 8))
sns.scatterplot(x='salary_in_usd', y='job_title', data=df, hue='job_title', palette='Set1', s=100)
plt.xlabel('Заработная плата в USD')
plt.ylabel('Должность')
plt.grid(True)
plt.title('Диаграмма рассеяния')
plt.legend(title='Должность', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()


#? Линейный график зависимости денег от региона
df_grouped_region = df.groupby('company_location')['salary_in_usd'].mean().reset_index()
plt.figure(figsize=(15, 8))
sns.lineplot(x='company_location', y='salary_in_usd', data=df_grouped_region)
plt.xlabel('Регион')
plt.ylabel('Средняя зарплата в USD')
plt.title('Зависимость уровня зарплаты от региона')
plt.xticks(rotation=-45)
plt.grid(True)
plt.tight_layout()
plt.show()

