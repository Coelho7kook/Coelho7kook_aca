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
    <title>Texto com Tradução de Idiomas</title>
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
    <audio autoplay loop>
        <source src="https://www.youtube.com/watch?v=s7RRgF5Ve_E&si=WTVDMJoNlHWg0ZIS" type="audio/mpeg">
        <source src="https://www.youtube.com/watch?v=Wnv1eTH2BaA&si=s3NwNy4DBJM3F2Cb" type="audio/mpeg">
    </audio>

    <div class="text-content">
        <p>Para Minha Amiga,  
        Mesmo quando o mundo parece pesado, quero que saibas que não estás sozinha. O caminho pode ser difícil, e as sombras podem parecer mais profundas, mas a tua força é maior do que imaginas.</p>

        <p>Assim como Miquella enfrenta suas batalhas, tu também és forte o suficiente para atravessar qualquer tempestade. Os momentos de dor são passageiros, e mesmo nos dias mais sombrios, há luz esperando para brilhar novamente.</p>

        <p>Não deixe que a tristeza te domine, pois cada lágrima é um passo para o reencontro com tua paz interior. A vida, com suas incertezas, nos desafia, mas cada desafio nos ensina a valorizar ainda mais as pequenas coisas que trazem alegria.</p>

        <p>Acredite em ti mesma, mesmo quando as palavras parecem falhar e o silêncio tenta preencher o vazio. Estamos todos conectados por sentimentos genuínos, e tua existência é um presente único.</p>

        <p>Por isso, não temas seguir em frente, pois há sempre uma mão estendida, uma palavra de carinho, e um coração que sente profundamente a tua dor. Você é forte. Você é amada.</p>
    </div>

    <button class="button-play" onclick="toggleText()">Por favor, clique aqui para algo especial</button>

    <div>
        <button class="button-language" onclick="setLanguage('pt')">Português</button>
        <button class="button-language" onclick="setLanguage('en')">Inglês</button>
        <button class="button-language" onclick="setLanguage('ja')">Japonês</button>
        <button class="button-language" onclick="setLanguage('ru')">Russo</button>
    </div>

    <script>
        function toggleText() {
            const textContent = document.querySelector('.text-content');
            textContent.style.display = 'block';
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
                    "自分自身を信じてください、言葉が失敗するようなときでも、沈黙が空白を埋めようとするときでも。私たちは真の感情でつながっていますし、あなたの存在は唯一の贈り物です。",
                    "だから、前進することを恐れないでください、いつでも助けの手があり、親切な言葉があり、あなたの痛みに深く寄り添う心があります。あなたは強い。あなたは愛されています。"
                ],
                ru: [
                    "Для моего друга, Даже когда мир кажется тяжелым, я хочу, чтобы ты знал, что ты не один. Пути могут быть трудными, и тени могут казаться глубже, но твоя сила гораздо больше, чем ты думаешь.",
                    "Как Микелла сталкивается с её сражениями, ты также силен, чтобы преодолеть любую бурю. Моменты боли мимолетны, и даже в самые темные дни есть свет, который снова готов сиять.",
                    "Не позволяй печали овладеть тобой, ведь каждая слеза — это шаг к воссоединению с твоим внутренним спокойствием. Жизнь с её неуверенностями бросает вызов нам, но каждый вызов учит ценить даже маленькие вещи, приносящие радость.",
                    "Верь в себя, даже когда слова кажутся бессильными, а молчание пытается заполнить пустоту. Мы связаны искренними чувствами, и твое существование — это уникальный дар.",
                    "Поэтому не бойся идти вперед, ведь всегда есть протянутая рука помощи, доброе слово и сердце, которое глубоко чувствует твою боль. Ты сильный. Тебя любят."
                ]
            };
            
            const textContent = document.querySelector('.text-content');
            textContent.innerHTML = texts[lang].map(text => <p>${text}</p>).join('');
            textContent.style.display = 'block';
        }
    </script>
</body>
</html>
