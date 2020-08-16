import pandas as pd
import plotly.express as px


wine_names = ['Class', 'Alcohol', 'MalicAcid', 'Ash', 'Alc.Ash', 'Magnesium', 'TotalPhenols', \
              'Flavanoids', 'Nonflav.Phenols', 'Proanthocyanins', 'ColorIntensity', 'Hue', 'OD280/OD315',\
              'Proline']
wine_df = pd.DataFrame(pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data', names = wine_names)) 
wine_df.Class = wine_df.Class - 1
wine_df.Class = wine_df.Class.astype('object')

nino_names = ['bouy','day', 'latitude', 'longitude', 'zon.winds', 'mer.winds', 'humidity', 'air.temp', 's.s.temp']
nino_df = pd.DataFrame(pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/el_nino-mld/elnino.gz',
                                   header = None,na_values = '.', sep = '\s+', names = nino_names))

nino_df = nino_df.loc[nino_df['day'] == 3, ['bouy','latitude', 'longitude', 's.s.temp']].dropna()


fig = px.scatter(wine_df, x="Alcohol", y='OD280/OD315', color="Class", marginal_y="box",
           marginal_x="box")
fig.show()

fig = px.scatter_geo(nino_df, lat='latitude', lon='longitude', locations=None, locationmode=None, 
     color='s.s.temp', text=None, hover_name='bouy', 
     color_discrete_map={}, color_continuous_scale='bluered', projection='orthographic')
fig.show()