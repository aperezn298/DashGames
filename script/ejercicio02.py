import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Cargar el dataset
url = 'https://raw.githubusercontent.com/aperezn298/DatasetsPUJC/refs/heads/main/games_sales_data.csv'
df = pd.read_csv(url)

# Sumar las ventas por región
total_jp_sales = df['JP_Sales'].sum()
total_na_sales = df['NA_Sales'].sum()
total_eu_sales = df['EU_Sales'].sum()

# Calcular el total de ventas combinadas de las tres regiones
total_sales = total_jp_sales + total_na_sales + total_eu_sales

# Calcular los porcentajes
jp_percentage = (total_jp_sales / total_sales) * 100
na_percentage = (total_na_sales / total_sales) * 100
eu_percentage = (total_eu_sales / total_sales) * 100

# Crear una lista con los porcentajes
percentages = [na_percentage, eu_percentage, jp_percentage]
regions = ['USA', 'Europa', 'Japon']

# Crear el gráfico de pastel con Plotly
pie_chart = go.Figure(data=[go.Pie(
    labels=regions,
    values=percentages,
    hole=0.3,
    marker_colors=['#1b4f72', '#85c1e9', '#d35400'],  # Colores originales
    hoverinfo='label+percent',
    textinfo='percent',
    textfont_size=15
)])

# Guardar el gráfico en formato HTML
pie_chart.write_html('sales_by_region.html')

# ::::::::::::::::

# Filtrar datos entre los años 2009 y 2020
df_filtered = df[(df['Year_of_Release'] >= 2009) & (df['Year_of_Release'] <= 2020)]

# Agrupar las ventas por año para cada región
sales_by_year = df_filtered.groupby('Year_of_Release').sum()[['NA_Sales', 'EU_Sales', 'JP_Sales']]

# Crear la gráfica de líneas usando Plotly
line_chart = go.Figure()

# Añadir la línea para North America Sales
line_chart.add_trace(go.Scatter(
    x=sales_by_year.index, 
    y=sales_by_year['NA_Sales'], 
    mode='lines+markers', 
    name='North America Sales', 
    line=dict(color='#1b4f72'),  # Azul oscuro
    marker=dict(size=8)
))

# Añadir la línea para Europe Sales
line_chart.add_trace(go.Scatter(
    x=sales_by_year.index, 
    y=sales_by_year['EU_Sales'], 
    mode='lines+markers', 
    name='Europe Sales', 
    line=dict(color='#85c1e9'),  # Azul claro
    marker=dict(size=8)
))

# Añadir la línea para Japan Sales
line_chart.add_trace(go.Scatter(
    x=sales_by_year.index, 
    y=sales_by_year['JP_Sales'], 
    mode='lines+markers', 
    name='Japan Sales', 
    line=dict(color='#d35400'),  # Naranja
    marker=dict(size=8)
))

# Configurar los ejes y el título
line_chart.update_layout(
    # title='Ventas Totales en NA, EU y JP (2009-2020)',
    title=' ',
    xaxis_title='Año de Lanzamiento',
    yaxis_title='Ventas Totales (en millones)',
    xaxis=dict(tickmode='linear'),
    legend_title_text='Región',
    hovermode="x unified",
    template="plotly_white"
)

# Guardar el gráfico en formato HTML
line_chart.write_html('sales_by_year_region.html')

# :::::::::::::::::

# Filtrar por años (2009-2020) y géneros (Action, Role-Playing, Strategy, Misc)
filtered_genres = ['Action', 'Role-Playing', 'Strategy', 'Misc']
df_filtered = df[(df['Year_of_Release'] >= 2009) & 
                 (df['Year_of_Release'] <= 2020) & 
                 (df['Genre'].isin(filtered_genres))]

# Agrupar las ventas por año y género, sumando NA_Sales, EU_Sales, JP_Sales
sales_by_year_genre = df_filtered.groupby(['Year_of_Release', 'Genre']).sum()[['NA_Sales', 'EU_Sales', 'JP_Sales']].reset_index()

# Pivotar los datos para tener los géneros como columnas
pivot_sales = sales_by_year_genre.pivot(index='Year_of_Release', columns='Genre', values=['NA_Sales', 'EU_Sales', 'JP_Sales']).fillna(0)

# Crear la gráfica de barras apiladas usando Plotly
stacked_bar_chart = go.Figure()

# Añadir las barras apiladas para North America (NA)
stacked_bar_chart.add_trace(go.Bar(
    x=pivot_sales.index, 
    y=pivot_sales['NA_Sales']['Action'], 
    name='NA Action', 
    marker_color='skyblue'
))
stacked_bar_chart.add_trace(go.Bar(
    x=pivot_sales.index, 
    y=pivot_sales['NA_Sales']['Role-Playing'], 
    name='NA Role-Playing', 
    marker_color='lightgreen'
))
stacked_bar_chart.add_trace(go.Bar(
    x=pivot_sales.index, 
    y=pivot_sales['NA_Sales']['Strategy'], 
    name='NA Strategy', 
    marker_color='lightcoral'
))
stacked_bar_chart.add_trace(go.Bar(
    x=pivot_sales.index, 
    y=pivot_sales['NA_Sales']['Misc'], 
    name='NA Misc', 
    marker_color='orange'
))

# Añadir las barras apiladas para Europe (EU)
stacked_bar_chart.add_trace(go.Bar(
    x=pivot_sales.index, 
    y=pivot_sales['EU_Sales']['Action'], 
    name='EU Action', 
    marker_color='blue',
    opacity=0.6
))
stacked_bar_chart.add_trace(go.Bar(
    x=pivot_sales.index, 
    y=pivot_sales['EU_Sales']['Role-Playing'], 
    name='EU Role-Playing', 
    marker_color='green',
    opacity=0.6
))
stacked_bar_chart.add_trace(go.Bar(
    x=pivot_sales.index, 
    y=pivot_sales['EU_Sales']['Strategy'], 
    name='EU Strategy', 
    marker_color='red',
    opacity=0.6
))
stacked_bar_chart.add_trace(go.Bar(
    x=pivot_sales.index, 
    y=pivot_sales['EU_Sales']['Misc'], 
    name='EU Misc', 
    marker_color='darkorange',
    opacity=0.6
))

# Añadir las barras apiladas para Japan (JP)
stacked_bar_chart.add_trace(go.Bar(
    x=pivot_sales.index, 
    y=pivot_sales['JP_Sales']['Action'], 
    name='JP Action', 
    marker_color='navy',
    opacity=0.4
))
stacked_bar_chart.add_trace(go.Bar(
    x=pivot_sales.index, 
    y=pivot_sales['JP_Sales']['Role-Playing'], 
    name='JP Role-Playing', 
    marker_color='darkgreen',
    opacity=0.4
))
stacked_bar_chart.add_trace(go.Bar(
    x=pivot_sales.index, 
    y=pivot_sales['JP_Sales']['Strategy'], 
    name='JP Strategy', 
    marker_color='maroon',
    opacity=0.4
))
stacked_bar_chart.add_trace(go.Bar(
    x=pivot_sales.index, 
    y=pivot_sales['JP_Sales']['Misc'], 
    name='JP Misc', 
    marker_color='orangered',
    opacity=0.4
))

# Configurar los ejes y el título
stacked_bar_chart.update_layout(
    barmode='stack',
    #title='Ventas Totales por Género en NA, EU y JP (2009-2020)',
    title=' ',
    xaxis_title='Año de Lanzamiento',
    yaxis_title='Ventas Totales (en millones)',
    legend_title='Región y Género',
    template="plotly_white",
    xaxis=dict(tickmode='linear', tickangle=45)
)

# Guardar el gráfico en formato HTML
stacked_bar_chart.write_html('sales_by_year_genre_region.html')