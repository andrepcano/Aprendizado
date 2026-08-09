from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def inicio():
    nome = request.args.get("nome")

    if nome:
        return f"<h1>Olá, {nome}!</h1><p>Você criou sua primeira página com Flask.</p>"

    return """
    <h1>Programa com Flask</h1>
    <form>
        <label>Digite seu nome:</label>
        <input type="text" name="nome">
        <button type="submit">Enviar</button>
    </form>
    """


if __name__ == "__main__":
    app.run(debug=True)
