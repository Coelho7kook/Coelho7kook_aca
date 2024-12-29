from flask import Flask, render_template_string

app = Flask(__name__)

# Código HTML embutido diretamente no Python
html_code = """
<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reprodutor de Música</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            background-color: #f0f0f0;
            margin: 0;
            padding: 0;
        }
        button {
            padding: 10px 20px;
            margin: 20px;
            font-size: 16px;
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
        iframe {
            display: none;  /* O vídeo ficará invisível */
        }
    </style>
</head>
<body>
    <h1>Reprodutor de Música Aleatória</h1>
    
    <!-- Botões para selecionar o idioma -->
    <button onclick="tocarMusicaAleatoria()">Tocar Música</button>
    
    <!-- O iframe será usado para tocar o áudio do YouTube -->
    <iframe id="player" width="560" height="315" 
            src="" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
    </iframe>

    <script>
        const musicasLinks = [
            "https://www.youtube.com/embed/s7RRgF5Ve_E?autoplay=1",  // Música 1
            "https://www.youtube.com/embed/InkKkTcw9_A?autoplay=1",  // Música 2
            "https://www.youtube.com/embed/v9l52KilyLU?autoplay=1",  // Música 3
            "https://www.youtube.com/embed/8FuRsZ7U4BU?autoplay=1",  // Música 4
            "https://www.youtube.com/embed/AvaLLgG8yaE?autoplay=1",  // Música 5
        ];

        // Função para tocar música aleatória ao clicar no botão
        function tocarMusicaAleatoria() {
            const randomIndex = Math.floor(Math.random() * musicasLinks.length);
            const iframe = document.getElementById("player");
            iframe.src = musicasLinks[randomIndex];  // Muda o src do iframe para o link escolhido
        }

        // Tocar música automaticamente ao carregar a página
        window.onload = function() {
            tocarMusicaAleatoria();  // Inicia a música aleatória assim que a página carrega
        };
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(html_code)  # Carrega o HTML diretamente do Python

if __name__ == '__main__':
    app.run(debug=True)  # Roda o servidor Flask
