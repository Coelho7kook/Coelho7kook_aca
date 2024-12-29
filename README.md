# Coelho7kook_aca
echo "# Coelho7kook_aca" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Coelho7kook/Coelho7kook_aca.git
git push -u origin main

<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Texto com Tradução de Idiomas e Música</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            background: url('https://truth.bahamut.com.tw/artwork/202210/c4b979ce2108d38e2e4a015fe8763082.GIF?w=1000') no-repeat center center fixed;
            background-size: cover;
            color: white;
            font-family: Arial, Helvetica, sans-serif;
            text-align: center;
            display: flex;
            flex-direction: column;
            justify-content: center;
            height: 100vh;
            overflow: hidden;
        }

        .text-content {
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            background-color: rgba(0, 0, 0, 0.6);
            border-radius: 10px;
            display: none; /* Oculta o texto inicialmente */
        }

        audio {
            display: none;
        }

        .button-play {
            background-color: #ffb3d9; /* Rosa Claro Fofo */
            color: white;
            font-size: 20px;
            padding: 15px 30px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            margin-top: 20px;
        }

        .button-play:hover {
            background-color: #ff69b4; /* Rosa mais intenso */
        }

        .button-language {
            margin: 5px;
            padding: 10px 15px;
            cursor: pointer;
            border-radius: 5px;
            color: white;
            background-color: #6a1b9a; /* Cores distintas para cada idioma */
            font-size: 14px;
            text-transform: uppercase;
        }

        .button-language:hover {
            background-color: #4a148c;
        }
    </style>
</head>
<body>
    <audio id="audio-player" autoplay loop>
        <!-- Áudio será carregado aleatoriamente -->
    </audio>

    <div class="text-content" id="text-content-pt">
        <p>Para Minha Amiga,  
        Mesmo quando o mundo parece pesado, quero que saibas que não estás sozinha. O caminho pode ser difícil, e as sombras podem parecer mais profundas, mas a tua força é maior do que imaginas.</p>

        <p>Assim como Miquella enfrenta suas batalhas, tu também és forte o suficiente para atravessar qualquer tempestade. Os momentos de dor são passageiros, e mesmo nos dias mais sombrios, há luz esperando para brilhar novamente.</p>

        <p>Não deixe que a tristeza te domine, pois cada lágrima é um passo para o reencontro com tua paz interior. A vida, com suas incertezas, nos desafia, mas cada desafio nos ensina a valorizar ainda mais as pequenas coisas que trazem alegria.</p>

        <p>Acredite em ti mesma, mesmo quando as palavras parecem falhar e o silêncio tenta preencher o vazio. Estamos todos conectados por sentimentos genuínos, e tua existência é um presente único.</p>

        <p>Por isso, não temas seguir em frente, pois há sempre uma mão estendida, uma palavra de carinho, e um coração que sente profundamente a tua dor. Você é forte. Você é amada.</p>
    </div>

    <div class="text-content" id="text-content-en">
        <p>To My Friend,  
        Even when the world seems heavy, I want you to know you're not alone. The path might be difficult, and the shadows may seem deeper, but your strength is greater than you realize.</p>

        <p>Just like Miquella faces her battles, you are strong enough to overcome any storm. The moments of pain are fleeting, and even in the darkest days, there is light waiting to shine again.</p>

        <p>Don't let sadness consume you, for every tear is a step towards reconnecting with your inner peace. Life, with its uncertainties, challenges us, but each challenge teaches us to cherish the little things that bring joy.</p>

        <p>Believe in yourself, even when words seem to fail and silence tries to fill the void. We are all connected by genuine feelings, and your existence is a unique gift.</p>

        <p>So, don't fear moving forward, as there is always a helping hand, a kind word, and a heart that deeply feels your pain. You are strong. You are loved.</p>
    </div>

    <div class="text-content" id="text-content-ja">
        <p>私の友へ、世界が重く感じられるときでも、あなたがひとりではないことを知ってほしい。道は難しいかもしれませんし、影がより深く感じられるかもしれませんが、あなたの強さは想像以上です。</p>

        <p>ミケラが直面する戦いのように、あなたもあらゆる嵐を乗り越える力があります。痛みの瞬間は一時的であり、最も暗い日々でも再び輝き始める光が待っています。</p>

        <p>悲しみがあなたを支配させてはならない、それぞれの涙はあなたの内なる平和に再接続するための一歩です。人生は不確実であり、それに挑戦しますが、各挑戦はさらに多くの楽しさをもたらす小さなことに価値を見出させます。</p>

        <p>自分自身を信じてください、言葉が失敗するようなときでも、沈黙が空白を埋めようとするときでも。私たちは真の感情でつながっていますし、あなたの存在は唯一の贈り物です。</p>

        <p>だから、前進することを恐れないでください、いつでも助けの手があり、親切な言葉があり、あなたの痛みに深く寄り添う心があります。あなたは強い。あなたは愛されています。</p>
    </div>

    <div class="text-content" id="text-content-ru">
        <p>Для моего друга, Даже когда мир кажется тяжелым, я хочу, чтобы ты знал, что ты не один. Пути могут быть трудными, и тени могут казаться глубже, но твоя сила гораздо больше, чем ты думаешь.</p>

        <p>Как Микелла сталкивается с её сражениями, ты также силен, чтобы преодолеть любую бурю. Моменты боли мимолетны, и даже в самых темных днях есть свет, который снова засияет.</p>

        <p>Не позволяй грусти поглотить тебя, потому что каждая слеза — это шаг к возвращению к своему внутреннему покою. Жизнь с её неопределенностями ставит перед нами вызовы, но каждый вызов учит нас ценить маленькие вещи, которые приносят радость.</p>

        <p>Верь в себя, даже когда слова кажутся недостаточными, и тишина пытается заполнить пустоту. Мы все связаны искренними чувствами, и твоё существование — это уникальный дар.</p>

        <p>Поэтому не бойся идти вперёд, потому что всегда есть протянутая рука, доброе слово и сердце, которое глубоко ощущает твою боль. Ты силён. Ты любим.</p>
    </div>

    <button class="button-play" onclick="toggleText('pt')">Português</button>
    <button class="button-play" onclick="toggleText('en')">Inglês</button>
    <button class="button-play" onclick="toggleText('ja')">Japonês</button>
    <button class="button-play" onclick="toggleText('ru')">Russo</button>

    <script>
        const audioLinks = [
            "https://www.youtube.com/watch?v=s7RRgF5Ve_E",  // Exemplo de link de áudio
            "https://www.youtube.com/watch?v=InkKkTcw9_A",
            "https://www.youtube.com/watch?v=v9l52KilyLU",
            "https://www.youtube.com/watch?v=8FuRsZ7U4BU",
            "https://www.youtube.com/watch?v=AvaLLgG8yaE"
        ];

        function playRandomAudio() {
            const audioPlayer = document.getElementById('audio-player');
            const randomAudio = audioLinks[Math.floor(Math.random() * audioLinks.length)];
            audioPlayer.src = randomAudio;
            audioPlayer.play(); // Toca o áudio aleatoriamente
        }

        function toggleText(lang) {
            // Esconde todos os textos
            const allTexts = document.querySelectorAll('.text-content');
            allTexts.forEach(text => text.style.display = 'none');
            
            // Exibe o texto correspondente ao idioma
            const textContent = document.getElementById('text-content-' + lang);
            textContent.style.display = 'block';

            // Toca um áudio aleatório ao clicar
            playRandomAudio();
        }
    </script>
</body>
</html>

<!DOCTYPE html>
<html lang="pt">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Reprodutor de Música Aleatório</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
      background-color: #f4f4f4;
    }
    .button-container {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .button {
      padding: 10px 20px;
      background-color: #007bff;
      color: white;
      border: none;
      cursor: pointer;
      font-size: 16px;
      border-radius: 5px;
    }
    .button:hover {
      background-color: #0056b3;
    }
    #audio {
      display: none;
    }
  </style>
</head>
<body>

  <div class="button-container">
    <button class="button" onclick="playRandomMusic()">Clique para Reproduzir Música</button>
  </div>

  <!-- Áudio invisível -->
  <audio id="audio" autoplay>
    <source id="audioSource" src="" type="audio/mpeg">
  </audio>

  <script>
    // URLs das músicas (vídeos do YouTube convertidos em áudio)
    const musicUrls = [
      "https://www.youtube.com/watch?v=s7RRgF5Ve_E", // Exemplo 1
      "https://www.youtube.com/watch?v=InkKkTcw9_A", // Exemplo 2
      "https://www.youtube.com/watch?v=v9l52KilyLU", // Exemplo 3
      "https://www.youtube.com/watch?v=8FuRsZ7U4BU", // Exemplo 4
      "https://www.youtube.com/watch?v=AvaLLgG8yaE"  // Exemplo 5
    ];

    // Função para tocar uma música aleatória
    function playRandomMusic() {
      // Gerar um índice aleatório para escolher uma música
      const randomIndex = Math.floor(Math.random() * musicUrls.length);
      
      // URL do vídeo aleatório
      const randomMusicUrl = musicUrls[randomIndex];
      
      // Atualiza a fonte de áudio com o link escolhido
      const audio = document.getElementById('audio');
      const audioSource = document.getElementById('audioSource');
      
      // Alterar para um link de áudio (convertido de YouTube, com a estrutura adequada)
      const audioFileUrl = randomMusicUrl.replace("watch?v=", "v/").concat("/audio.mp3");
      
      audioSource.src = audioFileUrl;
      audio.load(); // Carrega o novo áudio
      audio.play(); // Reproduz o áudio
    }

    // Reproduz o áudio automaticamente quando a página carregar
    window.onload = function() {
      playRandomMusic();  // Reproduz a música aleatória automaticamente ao carregar
    };
  </script>
  <script>
        // Lista de URLs de áudio para reprodução aleatória
        const audioLinks = [
            "https://m.youtube.com/watch?v=s7RRgF5Ve_E&pp=ygUgdW5kZXJ0YWxlIG51c2ljIG9uY2UgdXBvbiBhIHRpbWU%3D",
            "https://m.youtube.com/watch?v=InkKkTcw9_A&pp=ygUiemVsZGEgb2NhcmluYSBvZiB0aW1lIGVuZGluZyB0aGVtZQ%3D%3D",
            "https://m.youtube.com/watch?v=v9l52KilyLU&pp=ygUSemVsZGEgc29uZyBoZWFsaW5n",
            "https://m.youtube.com/watch?v=8FuRsZ7U4BU",
            "https://m.youtube.com/watch?v=AvaLLgG8yaE&pp=ygULZmFsbGVuIGRvd24%3D"
        ];

        // Função para tocar áudio aleatório
        function playRandomAudio() {
            const randomIndex = Math.floor(Math.random() * audioLinks.length);
            const audioPlayer = document.getElementById('audio-player');
            const audioSource = document.getElementById('audio-source');
            audioSource.src = audioLinks[randomIndex];
            audioPlayer.load();
            audioPlayer.play();
        }

        // Função para alternar o texto com base no idioma
        function toggleText() {
            const textContent = document.querySelector('.text-content');
            textContent.style.display = 'block';
            playRandomAudio();  // Tocar o som ao clicar no botão
        }

        function setLanguage(lang) {
            const texts = {
                pt: [
                    "Para Minha Amiga, Mesmo quando o mundo parece pesado, quero que saibas que não estás sozinha. O caminho pode ser difícil, e as sombras podem parecer mais profundas, mas a tua força é maior do que imaginas.",
                    "Assim como Miquella enfrenta suas batalhas, tu também és forte o suficiente para atravessar qualquer tempestade. Os momentos de dor são passageiros, e mesmo nos dias mais sombrios, há luz esperando para brilhar novamente.",
                    "Não deixe que a tristeza te domine, pois cada lágrima é um passo para o reencontro com tua paz interior. A vida, com suas incertezas, nos desafia, mas cada desafio nos ensina a valorizar ainda mais as pequenas coisas que trazem alegria.",
                    "Acredite em ti mesma, mesmo quando as palavras parecem falhar e o silêncio tenta preencher o vazio. Estamos todos conectados por sentimentos genuínos, e tua existência é um presente único.",
                    "Por isso, não temas seguir em frente, pois há sempre uma mão estendida, uma palavra de carinho, e um coração que sente profundamente a tua dor. Você é forte. Você é amada."
                ],
                en: [
                    "To My Friend, Even when the world seems heavy, I want you to know you're not alone. The path might be difficult, and the shadows may seem deeper, but your strength is greater than you realize.",
                    "Just like Miquella faces her battles, you are strong enough to overcome any storm. The moments of pain are fleeting, and even in the darkest days, there is light waiting to shine again.",
                    "Don't let sadness consume you, for every tear is a step towards reconnecting with your inner peace. Life, with its uncertainties, challenges us, but each challenge teaches us to cherish the little things that bring joy.",
                    "Believe in yourself, even when words seem to fail and silence tries to fill the void. We are all connected by genuine feelings, and your existence is a unique gift.",
                    "So, don't fear moving forward, as there is always a helping hand, a kind word, and a heart that deeply feels your pain. You are strong. You are loved."
                ],
                ja: [
                    "私の友へ、世界が重く感じられるときでも、あなたがひとりではないことを知ってほしい。道は難しいかもしれませんし、影がより深く感じられるかもしれませんが、あなたの強さは想像以上です。",
                    "ミケラが直面する戦いのように、あなたもあらゆる嵐を乗り越える力があります。痛みの瞬間は一時的であり、最も暗い日々でも再び輝き始める光が待っています。",
                    "悲しみがあなたを支配させてはならない、それぞれの涙はあなたの内なる平和に再接続するための一歩です。人生は不確実であり、それに挑戦しますが、各挑戦はさらに多くの楽しさをもたらす小さなことに価値を見出させます。",
                    "自分自身を信じてください、言葉が失われ、沈黙が空虚を満たそうとする時でさえ。私たちは皆、真実の感情で繋がっており、あなたの存在は唯一無二の贈り物です。",
                    "だから、前進することを恐れないでください。いつでも手を差し伸べる手があり、優しい言葉があり、あなたの痛みを深く感じる心があります。あなたは強い。あなたは愛されています。"
                ],
                ru: [
                    "Для моей подруги, Даже когда мир кажется тяжёлым, я хочу, чтобы ты знала, что ты не одна. Путь может быть трудным, а тени могут казаться более глубокими, но твоя сила гораздо больше, чем ты думаешь.",
                    "Как и Микелла, сталкивающаяся со своими битвами, ты тоже достаточно сильна, чтобы преодолеть любую бурю. Моменты боли мимолётны, и даже в самые тёмные дни есть свет, который снова засияет.",
                    "Не позволяй грусти овладеть тобой, потому что каждая слеза — это шаг к воссоединению с твоим внутренним миром. Жизнь полна неопределенности, она ставит перед нами испытания, но каждое испытание учит нас ценить ещё больше те маленькие вещи, которые приносят радость.",
                    "Верь в себя, даже когда слова, кажется, не могут помочь, и тишина пытается заполнить пустоту. Мы все связаны искренними чувствами, и твоё существование — это уникальный подарок.",
                    "Так что не бойся двигаться вперёд, потому что всегда есть протянутая рука, тёплое слово и сердце, которое глубоко чувствует твою боль. Ты сильная. Ты любима."
                ]
            };

            // Apresenta o texto correspondente ao idioma escolhido
            const textContent = document.querySelector('.text-content');
            textContent.innerHTML = texts[lang].map(p => `<p>${p}</p>`).join('');
            playRandomAudio();  // Toca o áudio aleatório ao mudar o idioma
        }

        // Toca o áudio aleatório quando a página é carregada
        window.onload = function() {
            playRandomAudio();
        }
    </script>

    </body>
</html>
