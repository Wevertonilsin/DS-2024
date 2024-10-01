from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['GET','POST'])
def calcular_imc():
    tipo = request.form['tipo']
    sexo = request.form['sexo']
    idade = request.form['idade']
    peso = float(request.form['peso'])
    altura = float(request.form['altura'])

    # Calcula o IMC
    try:
        if altura > 0:
            imc = round (peso  / (altura** 2), 2)
    except (ValueError, TypeError):
        imc = "Valores inválidos"

    if imc <= 18.5:
        status = "Abaixo do Peso"
    elif imc <= 24.9:
        status = "Peso Normal"
    elif imc <= 34.9:
        status = "Sobrepeso"
    elif imc <= 35.9:
        status ='Obesidade grau 1'
    elif imc <= 39.9:
        status = 'Obesidade grau 2'
    else:
        status = 'Obesidade grau 3'

    caminho_arquivo = 'models/imc.txt'

    # Aqui você pode adicionar as lógicas de IMC diferentes para adultos e crianças, se necessário
    if tipo == "adulto":
        resultado = f"O seu IMC é {imc:.2f} (Adulto)"
    elif tipo == "Adolecente":
        resultado = f"O seu IMC é {imc:.2f} (Adolecente)"
    else:
        resultado = f"O seu IMC é {imc:.2f} (Criança)"

    
    with open(caminho_arquivo, 'a') as arquivo:
        arquivo.write(f"{tipo};{sexo};{idade};{peso};{altura};{imc};{status}\n")
        
    return redirect("/")



@app.route("/calcular2")
def mostrar_imc():
    dados = []
    caminho_arquivo = 'models/imc.txt'

    with open(caminho_arquivo, 'r') as arquivo:
        for linha in arquivo:
            item = linha.strip().split(';')
            dados.append({
                'tipo': item[0],
                'sexo': item[1],
                'peso': item[2],
                'altura': item[3],  
                'imc': (round(float(item[3]),2)),
                'status': item[4]
            })
        

    return render_template("/calcular.html", inf=dados,)

@app.route("/excluir_notas", methods=['GET'])
def excluir_notas():
    linha_para_excluir = int(request.args.get('linha')) 
    caminho_arquivo = 'models/imc.txt'
    
    with open(caminho_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
    
    del linhas[linha_para_excluir]  

    with open(caminho_arquivo, 'w') as arquivo:
        arquivo.writelines(linhas)

    return redirect("/calcular2") 

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80, debug=True)
