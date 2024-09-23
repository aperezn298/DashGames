import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Cargar el dataset
url = 'https://raw.githubusercontent.com/aperezn298/DatasetsPUJC/refs/heads/main/games_sales_data.csv'
df = pd.read_csv(url)

# Filtrar por el año 2008 y las plataformas PSP, Wii, X360
filtered_data = df[(df['Year_of_Release'] == 2008) & 
                   (df['Platform'].isin(['PSP', 'Wii', 'X360']))]

# Filtrar valores nulos en ventas globales
ejercicio01 = filtered_data.dropna(subset=['Global_Sales'])

# Ordenar el dataset por ventas globales en orden descendente
top_10 = ejercicio01.sort_values(by='Global_Sales', ascending=False).head(10)

# Calcular las ventas del top 10
top_10_sales = top_10['Global_Sales'].sum()

# Calcular las ventas del resto de los videojuegos filtrados
total_sales = filtered_data['Global_Sales'].sum()
rest_sales = total_sales - top_10_sales

# Crear el gráfico de barras horizontales con valores en las columnas
bar_chart = px.bar(top_10, 
                   x='Global_Sales', 
                   y='Name', 
                   orientation='h', 
                   labels={'Global_Sales': 'Ventas Globales (millones)', 'Name': 'Video Juego'},
                   color_discrete_sequence=['#3498db'])  # Color original

# Agregar valores a cada barra
bar_chart.update_traces(text=top_10['Global_Sales'], textposition='auto')
bar_chart.write_html('top_10_games.html')

# Crear el gráfico de pastel
pie_chart = go.Figure(data=[go.Pie(
    labels=['Top 10', 'Resto Juegos'],
    values=[top_10_sales, rest_sales],
    hole=.3,
    marker_colors=['#3498db', '#f39c12']  # Colores originales
)])
pie_chart.write_html('sales_distribution.html')

# Crear el gráfico de barras para la distribución de ventas con nombres de ejes en español
sales_data = pd.DataFrame({
    'Category': ['Top 10', 'Resto Juegos'],
    'Sales': [top_10_sales, rest_sales]
})

bar_total_sales = px.bar(
    sales_data,
    x='Category',
    y='Sales',
    text=sales_data['Sales'],
    labels={'Category': 'Video Juegos', 'Sales': 'Ventas (millones)'},  # Nombres de ejes en español
    color_discrete_sequence=['#3498db', '#f39c12']  # Colores originales
)

# Formato de los valores en las barras
bar_total_sales.update_traces(texttemplate='%{text:.2f}M', textposition='outside')
bar_total_sales.write_html('sales_total.html')