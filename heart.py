<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Abrindo Google e Coração ❤️</title>
<meta http-equiv="refresh" content="3; url=https://www.google.com">
<style>
  html, body {
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
    background-color: black;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .heart {
    position: relative;
    width: 100px;
    height: 90px;
    background: red;
    transform: rotate(-45deg) scale(0);
    animation: beat 3s ease-in-out forwards;
  }

  .heart::before,
  .heart::after {
    content: "";
    position: absolute;
    width: 100px;
    height: 90px;
    background: red;
    border-radius: 50%;
  }

  .heart::before {
    top: -50px;
    left: 0;
  }

  .heart::after {
    left: 50px;
    top: 0;
  }

  @keyframes beat {
    0% {
      transform: rotate(-45deg) scale(0);
    }
    100% {
      transform: rotate(-45deg) scale(1);
    }
  }
</style>
</head>
<body>
  <div class="heart"></div>
</body>
</html>

