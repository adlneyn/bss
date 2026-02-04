// =====================================
// DATA ARTIKEL (EDIT SEMUA DI SINI)
// =====================================

const articles = {
  artikel1: {
    title: "Kegiatan Belajar Coding",
    image: "https://picsum.photos/800/400?random=1", // GANTI LINK FOTO DI SINI
    text: [
      "Hari ini kami belajar dasar-dasar pemrograman web.",
      "Materi yang dipelajari meliputi HTML, CSS, dan JavaScript.",
      "Semua murid sangat antusias mengikuti kegiatan ini."
    ]
  },

  artikel2: {
    title: "Proyek Website Pertama",
    image: "https://picsum.photos/800/400?random=2", // GANTI LINK FOTO DI SINI
    text: [
      "Murid-murid membuat website sederhana sebagai proyek pertama.",
      "Website berisi profil, galeri, dan artikel kegiatan.",
      "Proyek ini membantu memahami struktur halaman web."
    ]
  }
};

// =====================================
// FUNGSI PINDAH HALAMAN
// =====================================
function showPage(pageId) {
  document.querySelectorAll('.page').forEach(page => page.classList.remove('active'));
  document.getElementById(pageId).classList.add('active');
}

// =====================================
// FUNGSI MENAMPILKAN ARTIKEL
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

// Load semua artikel saat halaman dibuka
loadArticle("Best Student");
loadArticle("Best Reaction");
loadArticle("Best Artikel");
loadArticle("King and Queen");