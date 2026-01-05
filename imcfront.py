<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Calculadora de IMC</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f4f4f4;
      text-align: center;
      margin-top: 100px;
    }
    .container {
      background: white;
      width: 300px;
      margin: auto;
      padding: 20px;
      border-radius: 10px;
      box-shadow: 0px 0px 10px #aaa;
    }
    input {
      width: 90%;
      padding: 8px;
      margin: 5px 0;
      border-radius: 5px;
      border: 1px solid #ccc;
    }
    button {
      padding: 10px 20px;
      background-color: #007bff;
      color: white;
      border: none;
      border-radius: 5px;
      cursor: pointer;
    }
    button:hover {
      background-color: #0056b3;
    }
  </style>
</head>
<body>

  <div class="container">
    <h2>Calculadora de IMC</h2>
    <input type="number" id="peso" placeholder="Peso (kg)">
    <input type="number" id="altura" placeholder="Altura (m)">
    <button onclick="calcularIMC()">Calcular</button>
    <p id="resultado"></p>
  </div>

  <script>
    function calcularIMC() {
      const peso = parseFloat(document.getElementById("peso").value);
      const altura = parseFloat(document.getElementById("altura").value);
      const imc = peso / (altura * altura);
      let categoria = "";

      if (imc < 18.5) categoria = "Abaixo do peso";
      else if (imc < 25) categoria = "Peso normal";
      else if (imc < 30) categoria = "Sobrepeso";
      else if (imc < 35) categoria = "Obesidade grau I";
      else if (imc < 40) categoria = "Obesidade grau II";
      else categoria = "Obesidade grau III (mórbida)";

      document.getElementById("resultado").innerHTML =
        `Seu IMC é ${imc.toFixed(2)} — ${categoria}`;
    }
  </script>

</body>
</html>