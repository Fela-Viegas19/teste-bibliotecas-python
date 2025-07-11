import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Criar um DataFrame de exemplo
dados = pd.DataFrame({
    'Dia': ['Seg', 'Ter', 'Qua', 'Qui', 'Sex'],
    'Levantamentos': [120, 230, 180, 260, 150]
})

print("📊 Dados carregados:")
print(dados)

# Gráfico simples com matplotlib
plt.figure(figsize=(8, 4))
sns.barplot(x='Dia', y='Levantamentos', data=dados)
plt.title("Levantamentos Diários nos TPAs")
plt.ylabel("Valor (Kz)")
plt.xlabel("Dia da Semana")
plt.show()