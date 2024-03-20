from flask import Flask, render_template
import pandas as pd
import plotly.graph_objs as go

app = Flask(__name__)

# Load your dataset
df = pd.read_csv('synthetic_disaster_data.csv')

# Example visualization function using Plotly
def generate_visualization():
    data = [
        go.Bar(
            x=['A', 'B', 'C', 'D'],
            y=[10, 20, 30, 40]
        )
    ]
    layout = go.Layout(title='Example Visualization')
    fig = go.Figure(data=data, layout=layout)
    return fig.to_html(full_html=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/visualizations')
def visualizations():
    # Generate visualization
    graph = generate_visualization()
    return render_template('visualization.html', graph=graph)

if __name__ == '__main__':
    app.run(debug=True)
