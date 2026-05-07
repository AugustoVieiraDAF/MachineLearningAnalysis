import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA, NMF

dados = pd.read_csv("cocaina-sim.csv")

dados_data = dados.drop('Classe', axis = 'columns')
dados_classe = dados['Classe']


dados_data = dados_data.astype('float')
dados_data.columns = dados_data.columns.astype('float')


rowmin = dados_data.min(axis = 'columns')
dados_data = dados_data.subtract(rowmin, axis = 'index')


rowmax  = dados_data.max(axis = 'columns')
dados_data = dados_data.div(rowmax, axis = 'index')


dados_scaled = pd.DataFrame(StandardsScaler().fir_transform(dados_scaled),columns=['PC-1', 'PC-2', 'PC-3', 'PC-4', 'PC-5', 'PC-6'], index=dados_data.index )

dados_PCA['Classe']=  dados_classe

g = pca.explained_variance_ratio_.tolist()
sum(g)

PCs = pd.DataFrame(pca.components_.T, columns=['PC-1', 'PC-2', 'PC-3', 'PC-4', 'PC-5', 'PC-6'], index=dados_data.columns)
