// script.js
const audioLinks = [
  "https://www.youtube.com/embed/s7RRgF5Ve_E?autoplay=1", // Música 1
  "https://www.youtube.com/embed/InkKkTcw9_A?autoplay=1", // Música 2
  "https://www.youtube.com/embed/v9l52KilyLU?autoplay=1", // Música 3
  "https://www.youtube.com/embed/8FuRsZ7U4BU?autoplay=1", // Música 4
  "https://www.youtube.com/embed/AvaLLgG8yaE?autoplay=1"  // Música 5
];

const buttons = document.querySelectorAll(".play-button");
const audioPlayer = document.getElementById("audio-player");
const playPauseBtn = document.getElementById("playPauseBtn");
const nextBtn = document.getElementById("nextBtn");
let currentSongIndex = -1;
let isPlaying = false;

buttons.forEach(button => {
  button.addEventListener("click", function() {
    const songId = this.getAttribute("data-id");
    playMusic(songId);
  });
});

function playMusic(songId) {
  currentSongIndex = songId;
  const selectedLink = audioLinks[songId];
  audioPlayer.src = selectedLink;
  audioPlayer.style.display = "block"; // Exibe o player invisível (música carregada)

  if (!isPlaying) {
    playPauseBtn.innerText = "Pause";
    isPlaying = true;
  }
}

function togglePlayPause() {
  if (isPlaying) {
    audioPlayer.src = "";  // Para a música
    playPauseBtn.innerText = "Play";
    isPlaying = false;
  } else {
    playMusic(currentSongIndex); // Retoma a última música
  }
}

function nextSong() {
  currentSongIndex = (currentSongIndex + 1) % audioLinks.length; // Avança para a próxima música
  playMusic(currentSongIndex);
}
