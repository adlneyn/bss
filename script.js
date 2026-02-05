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
      tag: "Kategori 01",
      image: "", 
      content: ["[nanti bakal ada chara'nn dan foto bukti dari best student]."]
    },
    best_reaction: {
      title: "Best Reaction Bulan Ini",
      tag: "Kategori 02",
      image: "", 
      content: ["[nanti bakal ada chara'nn dan foto bukti dari best reaction]."]
    },
    best_artikel: {
      title: "Best Artikel Bulan Ini",
      tag: "Kategori 03",
      image: "", 
      content: ["[nanti bakal ada chara'nn dan foto bukti dari best artikel]."]
    },
    king_queen: {
      title: "King and Queen Bulan Ini",
      tag: "Kategori 04",
      image: "", 
      content: ["[nanti bakal ada chara'nn dan foto bukti dari king dan queen]."]
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