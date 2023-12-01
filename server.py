from flask import Flask, render_template
from pyvis.network import Network
app = Flask(__name__)

def create_graph():
    net = Network(notebook=True, cdn_resources="remote")
    net.add_nodes([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
    net.add_edges([(1, 2), (1, 3), (2, 4), (2, 5), (3,6), (3,7),(4,8),(4,9),(5,10),(5,11),(6,12),(6,13),(7,14),(7,15)])
net.show("templates/index.html")

@app.route("/")
def index():
    create_graph()
    return render_template('index.html')
if __name__ == "__main__":
    app.run(debug=True)
