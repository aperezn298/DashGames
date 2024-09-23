import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Cargar el dataset
url = 'https://raw.githubusercontent.com/aperezn298/DatasetsPUJC/refs/heads/main/games_sales_data.csv'
df = pd.read_csv(url)


# Agrupar por año y plataforma, y contar el número de juegos
games_per_year_platform = df.groupby(['Year_of_Release', 'Platform']).size().unstack(fill_value=0)

# Crear el gráfico de barras apiladas
bar_chart = go.Figure()

# Añadir trazas para cada plataforma
for platform in games_per_year_platform.columns:
    bar_chart.add_trace(go.Bar(
        x=games_per_year_platform.index,
        y=games_per_year_platform[platform],
        name=platform
    ))

# Actualizar el diseño del gráfico
bar_chart.update_layout(
    # title='Número de Juegos por Año y Plataforma',
    title=' ',
    xaxis_title='Año',
    yaxis_title='Número de Juegos',
    barmode='stack',
    template='plotly_white'
)

# Guardar el gráfico en formato HTML
bar_chart.write_html('games_per_year_platform.html')


# ::::::::::::



# Contar el número de juegos por publicador y seleccionar los 10 principales
games_per_publisher = df['Publisher'].value_counts().head(10)

# Crear el gráfico de barras horizontales
barh_chart = go.Figure()

barh_chart.add_trace(go.Bar(
    y=games_per_publisher.index,
    x=games_per_publisher.values,
    orientation='h'  # Gráfico horizontal
))

# Actualizar el diseño del gráfico
barh_chart.update_layout(
    # title='Número de Juegos por Publicador',
    title=' ',
    xaxis_title='Número de Juegos',
    yaxis_title='Publicador',
    template='plotly_white'
)

# Guardar el gráfico en formato HTML
barh_chart.write_html('games_per_publisher.html')