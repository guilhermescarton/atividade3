#coding: UTF-8
from flask import Flask, render_template, request

app =  Flask(__name__)

@app.route("/")
def pagina_index():
    ip_do_visitante = request.remote_addr
    return render_template("index.html", **locals() )
	

@app.route("/metodo1/", methods=["GET"])
def dados():
    nome =  request.args.get("nome")
    email = request.args.get("email")
    telefone = request.args.get("telefone")
    return render_template("dados.html", **locals() )
	

@app.route("/metodo2/")
def metodo2():
    return render_template("dados.html", **locals())

@app.route("/metodo2/", methods=["POST"])
def dados2():
    nome =  request.form.get("nome")
    email = request.form.get("email")
    telefone = request.form.get("telefone")
    return render_template("dados.html", **locals() )
	
	
@app.route("/")
def dados3():
    return render_template("dados.html")
	
@app.route("/metodo3/<nome>/<email>/<telefone>/")
def dados_3(nome,email,telefone):
	return render_template("dados.html",**locals())
	

	




	
	
	
