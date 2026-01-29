import streamlit as st
from pages_content import get_profile_data, get_articles_data, get_thanks_data

# Konfigurasi Halaman
st.set_page_config(page_title="Web Grup & Artikel", layout="wide")

# Styling Custom untuk Sidebar dan Detail
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .article-card {
        padding: 20px;
        border-radius: 10px;
        background-color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        cursor: pointer;
        transition: 0.3s;
    }
    .article-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    # Sidebar Navigasi
    st.sidebar.title("📌 Navigasi")
    menu = ["Profil Grup", "Artikel Terpopuler (Hal 2)", "Karya Murid (Hal 3)", 
            "Inspirasi (Hal 4)", "Catatan Kelas (Hal 5)", "Terima Kasih"]
    choice = st.sidebar.radio("Pilih Halaman:", menu)

    # Logika Navigasi
    if choice == "Profil Grup":
        show_profile()
    elif "Artikel" in choice or "Karya" in choice or "Inspirasi" in choice or "Catatan" in choice:
        # Kita gunakan logika yang sama untuk hal 2-5 sesuai permintaanmu
        page_idx = menu.index(choice)
        show_article_page(page_idx, choice)
    elif choice == "Terima Kasih":
        show_thanks()

def show_profile():
    data = get_profile_data()
    st.title("👤 Profil & Deskripsi Grup")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        # Placeholder Foto Profil
        st.image(data["image_url"], caption="Foto Grup / Profil", use_container_width=True)
    with col2:
        st.subheader(data["group_name"])
        st.write(data["description"])

def show_article_page(page_idx, title):
    st.title(f"📚 {title}")
    articles = get_articles_data(page_idx)
    
    # Cek apakah kita sedang melihat detail atau list
    if f"detail_{page_idx}" not in st.session_state:
        st.session_state[f"detail_{page_idx}"] = None

    if st.session_state[f"detail_{page_idx}"] is None:
        # Tampilan List Artikel
        for idx, art in enumerate(articles):
            with st.container():
                col_img, col_txt = st.columns([1, 3])
                with col_img:
                    st.image(art["image_url"], use_container_width=True)
                with col_txt:
                    st.subheader(art["title"])
                    st.write(art["summary"])
                    if st.button(f"Baca Detail: {art['title']}", key=f"btn_{page_idx}_{idx}"):
                        st.session_state[f"detail_{page_idx}"] = idx
                        st.rerun()
                st.markdown("---")
    else:
        # Tampilan Detail Halaman Baru
        idx = st.session_state[f"detail_{page_idx}"]
        art = articles[idx]
        
        if st.button("⬅️ Kembali ke Daftar"):
            st.session_state[f"detail_{page_idx}"] = None
            st.rerun()
            
        st.header(art["title"])
        st.image(art["image_url"], width=500)
        st.write("### Isi Lengkap Artikel")
        st.write(art["full_content"])

def show_thanks():
    data = get_thanks_data()
    st.title("🙏 Terima Kasih")
    st.balloons()
    
    st.markdown(f"""
    <div style="text-align: center; padding: 50px;">
        <h2>{data['message']}</h2>
        <p>Klik tombol di bawah untuk bergabung ke channel kami:</p>
        <a href="{data['whatsapp_link']}" target="_blank">
            <button style="background-color: #25D366; color: white; padding: 15px 30px; border: none; border-radius: 5px; font-size: 18px; cursor: pointer;">
                Buka Channel WhatsApp
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()