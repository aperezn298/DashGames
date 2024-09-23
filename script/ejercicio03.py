import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Cargar el dataset
url = 'https://raw.githubusercontent.com/aperezn298/DatasetsPUJC/refs/heads/main/games_sales_data.csv'
df = pd.read_csv(url)

# Filtrar los datos para los años deseados
years = [2000, 2005, 2010, 2015]
df_filtered = df[df['Year_of_Release'].isin(years)]

# Calcular las ventas globales por año
sales_distribution = df_filtered.groupby('Year_of_Release')['Global_Sales'].sum()

# Crear el gráfico de pastel
pie_chart = go.Figure(data=[go.Pie(
    labels=sales_distribution.index,
    values=sales_distribution,
    textinfo='label+percent',  # Mostrar etiqueta y porcentaje
    hole=.3,  # Para hacer un gráfico de dona
    marker=dict(colors=['#1b4f72', '#85c1e9', '#d35400', '#f39c12'])  # Colores personalizados
)])

# Actualizar el diseño del gráfico
pie_chart.update_layout(
    # title='Distribución porcentual de ventas globales (2000, 2005, 2010, 2015)',
    title=' ',
    template='plotly_white'
)

# Guardar el gráfico en formato HTML
pie_chart.write_html('sales_distribution_years.html')


# :::::::::::::::::


# Filtrar los datos para los años deseados
years = [2000, 2005, 2010, 2015]
df_filtered = df[df['Year_of_Release'].isin(years)]

# Agrupar por año y género, y sumar las ventas globales
sales_by_genre = df_filtered.groupby(['Year_of_Release', 'Genre'])['Global_Sales'].sum().unstack()

# Calcular el porcentaje de ventas por género para cada año
sales_percentage = sales_by_genre.div(sales_by_genre.sum(axis=1), axis=0)

# Crear el gráfico de barras apiladas
bar_chart = go.Figure()

# Añadir trazas para cada género
for genre in sales_percentage.columns:
    bar_chart.add_trace(go.Bar(
        x=sales_percentage.index,
        y=sales_percentage[genre],
        name=genre
    ))

# Actualizar el diseño del gráfico
bar_chart.update_layout(
    # title='Porcentaje de ventas globales por género (2000, 2005, 2010, 2015)',
    title=' ',
    xaxis_title='Año',
    yaxis_title='Porcentaje de Ventas',
    barmode='stack',
    template='plotly_white'
)

# Guardar el gráfico en formato HTML
bar_chart.write_html('sales_percentage_by_genre_years.html')


# :::::::::::::


# Filtrar los datos para los años 2000 a 2010 y los géneros deseados
years = list(range(2000, 2011))
genres = ['Action', 'Shooter', 'Sports']
df_filtered = df[(df['Year_of_Release'].isin(years)) & (df['Genre'].isin(genres))]

# Agrupar por año y género, y sumar las ventas globales
sales_trend = df_filtered.groupby(['Year_of_Release', 'Genre'])['Global_Sales'].sum().unstack()

# Crear el gráfico de línea
line_chart = go.Figure()

# Añadir trazas para cada género
for genre in sales_trend.columns:
    line_chart.add_trace(go.Scatter(
        x=sales_trend.index,
        y=sales_trend[genre],
        mode='lines+markers',
        name=genre
    ))

# Actualizar el diseño del gráfico
line_chart.update_layout(
    # title='Tendencia de Ventas Globales por Género (2000-2010)',
    title=' ',
    xaxis_title='Año',
    yaxis_title='Ventas Globales (millones)',
    template='plotly_white',
    xaxis=dict(tickmode='linear'),
    yaxis=dict(showgrid=True)
)

# Guardar el gráfico en formato HTML
line_chart.write_html('sales_trend_by_genre_2000_2010.html')