# Coelho7kook_aca
echo "# Coelho7kook_aca" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Coelho7kook/Coelho7kook_aca.git
git push -u origin main

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Site Interativo</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background: url('background.jpg') no-repeat center center fixed;
            background-size: cover;
            color: white;
            text-align: center;
        }
        .container {
            padding: 20px;
        }
        .btn {
            background-color: #007BFF;
            color: white;
            border: none;
            padding: 10px 20px;
            margin: 10px;
            cursor: pointer;
            border-radius: 5px;
        }
        .btn:hover {
            background-color: #0056b3;
        }
        .hidden {
            display: none;
        }
        .language-selector {
            margin: 10px 0;
        }
        .text-container {
            margin: 20px;
            font-size: 18px;
        }
        .arrow {
            font-size: 24px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Site Interativo</h1>
        <div class="language-selector">
            <button class="btn" onclick="changeLanguage('pt')">Português</button>
            <button class="btn" onclick="changeLanguage('en')">Inglês</button>
            <button class="btn" onclick="changeLanguage('jp')">Japonês</button>
        </div>

        <div id="text1" class="text-container">
            <p id="text-content">Seja bem-vindo ao nosso site interativo.</p>
        </div>

        <div id="text2" class="text-container hidden">
            <p id="text-content-2">Obrigado por explorar este conteúdo especial.</p>
        </div>

        <div>
            <span class="arrow" onclick="toggleText()">➡️</span>
        </div>

        <div>
            <button class="btn" onclick="playMusic()">Tocar Música</button>
            <button class="btn" onclick="changeMusic()">Mudar Música</button>
        </div>
    </div>

    <iframe id="music-player" width="0" height="0" style="border: none;" allow="autoplay"></iframe>

    <script>
        const texts = {
            pt: [
                "Seja bem-vindo ao nosso site interativo.",
                "Obrigado por explorar este conteúdo especial."
            ],
            en: [
                "Welcome to our interactive site.",
                "Thank you for exploring this special content."
            ],
            jp: [
                "私たちのインタラクティブなサイトへようこそ。",
                "この特別なコンテンツを探索していただきありがとうございます。"
            ]
        };

        const musicTracks = [
            "https://www.youtube.com/embed/s7RRgF5Ve_E?autoplay=1",
            "https://www.youtube.com/embed/Wnv1eTH2BaA?autoplay=1"
        ];

        let currentText = 0; // 0 for text1, 1 for text2
        let currentLanguage = 'pt';
        let currentMusicIndex = 0;

        function changeLanguage(language) {
            currentLanguage = language;
            updateText();
        }

        function updateText() {
            const text1 = document.getElementById('text1');
            const text2 = document.getElementById('text2');

            if (currentText === 0) {
                text1.querySelector('#text-content').textContent = texts[currentLanguage][0];
            } else {
                text2.querySelector('#text-content-2').textContent = texts[currentLanguage][1];
            }
        }

        function toggleText() {
            currentText = (currentText === 0) ? 1 : 0;
            document.getElementById('text1').classList.toggle('hidden');
            document.getElementById('text2').classList.toggle('hidden');
            updateText();
        }

        function playMusic() {
            const musicPlayer = document.getElementById('music-player');
            musicPlayer.src = musicTracks[currentMusicIndex];
        }

        function changeMusic() {
            const musicPlayer = document.getElementById('music-player');
            currentMusicIndex = (currentMusicIndex + 1) % musicTracks.length;
            musicPlayer.src = musicTracks[currentMusicIndex];
        }
    </script>
</body>
</html>
