// JAVASCRIPT LOGIC (DISATUKAN DI SINI)
function showPage(pageId) {
    document.querySelectorAll('.page').forEach(page => page.classList.remove('active'));
    const targetPage = document.getElementById(pageId);
    if (targetPage) targetPage.classList.add('active');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  // DATA ARTIKEL - EDIT_DI_SINI: Ganti link Pinterest untuk halaman detail
  const articles = {
    best_student: {
      title: "Best Student Bulan Ini",
      tag: "Prestasi",
      image: "https://i.pinimg.com/originals/gambar_1.jpg", 
      content: ["Selamat kepada murid terbaik atas dedikasi akademik yang luar biasa."]
    },
    best_reaction: {
      title: "Best Reaction: Aura Positif",
      tag: "Karakter",
      image: "https://i.pinimg.com/originals/gambar_2.jpg",
      content: ["Karakter yang kuat terpancar dari cara kita menghargai orang lain."]
    },
    best_artikel: {
      title: "Best Artikel: Literasi Kreatif",
      tag: "Kreativitas",
      image: "https://i.pinimg.com/originals/gambar_3.jpg",
      content: ["Menulis adalah cara terbaik untuk mengabadikan pemikiran."]
    },
    king_queen: {
      title: "King & Queen: Ikon BSS",
      tag: "Favorit",
      image: "https://i.pinimg.com/originals/gambar_4.jpg",
      content: ["Sosok King dan Queen menjadi teladan integritas bagi semua murid."]
    }
  };

  function viewArticle(id) {
    const data = articles[id];
    if (!data) return;
    const detailDiv = document.getElementById('article-content');
    detailDiv.innerHTML = `
      <div class="mb-12">
        <span class="bg-blue-100 text-blue-700 px-4 py-2 rounded-xl text-xs font-black uppercase tracking-widest">${data.tag}</span>
        <h2 class="text-4xl md:text-6xl font-black text-slate-900 mt-6 leading-tight tracking-tight">${data.title}</h2>
      </div>
      <div class="relative mb-12">
        <img src="${data.image}" class="w-full h-96 md:h-[500px] object-cover rounded-[3rem] shadow-2xl border-8 border-white" onerror="this.src='https://via.placeholder.com/800x500'">
      </div>
      <div class="prose prose-2xl max-w-none text-slate-700 leading-relaxed font-medium italic">
        ${data.content.map(p => `<p class="mb-6">"${p}"</p>`).join('')}
      </div>
    `;
    showPage('detail');
  }

  document.addEventListener('DOMContentLoaded', () => showPage('home'));