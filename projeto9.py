from flask import Flask, request, jsonify

app = Flask(__name__)

itens = [
    {
        "id":1,
        "nome": "Arroz 5kg",
        "quantidade": 2,
        "categoria": "Alimentos",
        "propriedade": "alta",
        "comprado": False
    }
]

@app.route("/items", methods=["GET"])
def listar_itens():
    return jsonify(itens)

@app.route("/items/<id>", methods=["GET"])
def buscar_item(id):
    item = next((i for i in itens if i ["id"] == id), None)
    if not item:
        return jsonify({"erro": "Item não encontrado."}), 404

    return jsonify(item)

@app.route("/items", methods=["POST"])
def add_item():
    dados = request.get_json()
    novo_item = { 
        "id":len(itens) + 1,
        "nome": dados["nome"],
        "quantidade": dados["quantidade"],
        "categoria": dados["categoria"],
        "propriedade": dados["prioridades"],
        "comprado": dados["comprado"]
    }
    itens.append(novo_item)
    return jsonify(novo_item)

@app.route("/items/<id>", methods=["PUT"])
def atualizar_item():
    item = next((i for i in itens if i["id"] == id), None)
    if not item:
        return jsonify({"erro": "item não encontrado!"}), 404

    dados = request.get_json()
    item["nome"] = dados.get('nome', dados["nome"])
    item["quantidade"] = dados.get('quantidade', dados["quantidades"])
    item["categoria"] = dados.get('categoria', dados["categoria"]) 
    item["prioridade"] = dados.get('priordade', dados["prioridade"])
    item["comprado"] = dados.get('comprado', dados["comprado"])

    return jsonify(item)

@app.route("/items/<id>", methods=["DELETE"])
def excluir_item(id):
    global itens
    item = next((i for i in itens if i["id"] == id), None)
    if not item:
            return jsonify({"erro": "item não encontrado!"}), 404

    itens = [i for i in itens if i["id"] != id]
    return jsonify({"mensagem": "item excluido com sucesso!"})

if __name__ == "__main__":
     app.run(debug=True)