<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Sistema de Professores</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #0f4c81, #1a73e8);
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .container {
            background: white;
            color: #222;
            padding: 25px;
            border-radius: 10px;
            width: 350px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.2);
        }

        input, button {
            width: 100%;
            margin: 8px 0;
            padding: 10px;
            border-radius: 6px;
            border: 1px solid #CCC;
        }

        button {
            background: #1a73e8;
            border: none;
            color: white;
            cursor: pointer;
        }

        button:hover {
            background: #0f4c81;
        }

        .resultado {
            margin-top: 15px;
            border-top: 1px solid #ccc;
            padding-top: 10px;
        }
    </style>
</head>
<body>

<div class="container">
    <h2>Cadastro de Professor</h2>

    <input type="text" id="nome" placeholder="Nome do professor">
    <input type="text" id="materia" placeholder="Matéria">
    <input type="text" id="horario" placeholder="Horário">
    <textarea id="conteudo" placeholder="Conteúdos" rows="3"></textarea>

    <button onclick="adicionar()">Salvar</button>

    <div class="resultado" id="lista"></div>
</div>

<script src="script.js"></script>

</body>
</html>
