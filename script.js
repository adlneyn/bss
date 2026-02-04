// =====================================
// DATA ARTIKEL (EDIT DI SINI)
// =====================================
const articles = {
  artikel1: {
    title: "Best Student",
    image: "images/student.jpg",
    text: [
      "Penghargaan Best Student diberikan kepada siswa dengan prestasi akademik terbaik.",
      "Siswa ini menunjukkan dedikasi tinggi dalam belajar dan disiplin luar biasa."
    ]
  },

  artikel2: {
    title: "Best Reaction",
    image: "images/reaction.jpg",
    text: [
      "Kategori Best Reaction diberikan kepada siswa dengan respon tercepat dan paling aktif.",
      "Selalu bersemangat dalam setiap kegiatan kelas."
    ]
  },

  artikel3: {
    title: "Best Artikel",
    image: "images/artikel.jpg",
    text: [
      "Best Artikel diberikan kepada siswa dengan tulisan terbaik.",
      "Artikel dinilai dari kreativitas, struktur, dan isi."
    ]
  },

  artikel4: {
    title: "King and Queen",
    image: "images/kingqueen.jpg",
    text: [
      "King and Queen adalah penghargaan untuk siswa paling inspiratif.",
      "Mereka menjadi teladan bagi teman-temannya."
    ]
  }
};

// =====================================
// PINDAH HALAMAN
// =====================================
function showPage(pageId) {
  document.querySelectorAll('.page').forEach(page => page.classList.remove('active'));
  document.getElementById(pageId).classList.add('active');
}

// =====================================
// LOAD ARTIKEL
// =====================================
function loadArticle(id) {
  document.getElementById(`title-${id}`).innerText = articles[id].title;
  document.getElementById(`img-${id}`).src = articles[id].image;

  const textContainer = document.getElementById(`text-${id}`);
  textContainer.innerHTML = "";

  articles[id].text.forEach(paragraph => {
    const p = document.createElement("p");
    p.innerText = paragraph;
    textContainer.appendChild(p);
  });
}

// LOAD SEMUA
loadArticle("artikel1");
loadArticle("artikel2");
loadArticle("artikel3");
loadArticle("artikel4");