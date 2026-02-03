import streamlit as st
import os
import sys

# Try to import page_content; if not available, try adding project dir to sys.path
try:
    from pages_content import get_profile_data, get_articles_data, get_thanks_data
except Exception:
    # Attempt to add current file directory to sys.path and retry
    current_dir = os.path.dirname(os.path.abspath(__file__))
    if current_dir not in sys.path:
        sys.path.insert(0, current_dir)
    try:
        from pages_content import get_profile_data, get_articles_data, get_thanks_data
    except Exception:
        # Fallback stub implementations to avoid import errors during linting/IDE inspection
        def get_profile_data():
            return {
                "image_url": "https://images.pexels.com/photos/3184418/pexels-photo-3184418.jpeg",
                "group_name": "Bytesyntech",
                "description": "Deskripsi grup belum tersedia."
            }

        def get_articles_data(page_idx):
            # Return empty list by default
            return []

        def get_thanks_data():
            return {"message": "Terima kasih!", "whatsapp_link": "#"}

# Konfigurasi Halaman
st.set_page_config(page_title="Official Byte Syntech", layout="wide")

# Styling Custom (CSS ini membantu tampilan Streamlit lebih mirip dengan UI index.html)
st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        transition: all 0.3s;
    }
    .article-card {
        padding: 20px;
        border-radius: 12px;
        background-color: white;
        border: 1px solid #e2e8f0;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    # Sidebar Navigasi - Disamakan dengan index.html
    st.sidebar.title("Bytesyntech")
    menu = [
        "Profil Grup", 
        "Artikel Murid (1)", 
        "Artikel Murid (2)", 
        "Artikel Murid (3)", 
        "Artikel Murid (4)", 
        "Artikel Murid (5)",
        "Terima Kasih"
    ]
    choice = st.sidebar.radio("Navigasi:", menu)

    # Logika Navigasi
    if choice == "Profil Grup":
        show_profile()
    elif "Artikel Murid" in choice:
        # Map choice ke index 1, 2, 3, 4 sesuai database page_content
        import re
        try:
            page_num = int(re.search(r'\((\d+)\)', choice).group(1))
            show_article_page(page_num, choice)
        except:
            st.error("Halaman tidak ditemukan")
    elif choice == "Terima Kasih":
        show_thanks()

def show_profile():
    data = get_profile_data()
    st.title("👤 Profil & Deskripsi Grup")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        # Gunakan fallback jika image path salah
        try:
            st.image(data["image_url"], caption="Foto Grup / Profil", use_container_width=True)
        except:
            st.image("https://images.pexels.com/photos/3184418/pexels-photo-3184418.jpeg", caption="Foto Grup (Placeholder)", use_container_width=True)
    with col2:
        st.subheader(data["group_name"])
        st.info(data["description"])

def show_article_page(page_idx, title):
    st.title(f"📚 {title}")
    articles = get_articles_data(page_idx)
    
    # State management untuk detail
    if f"detail_{page_idx}" not in st.session_state:
        st.session_state[f"detail_{page_idx}"] = None

    if st.session_state[f"detail_{page_idx}"] is None:
        if not articles:
            st.warning("Belum ada artikel di halaman ini.")
            return

        # Tampilan Grid List (Mirip index.html)
        cols = st.columns(2)
        for idx, art in enumerate(articles):
            with cols[idx % 2]:
                st.markdown(f"""
                <div class="article-card">
                    <img src="{art['image_url']}" style="width:100%; border-radius:8px; height:180px; object-fit:cover;">
                    <h4 style="margin-top:10px;">{art['title']}</h4>
                    <p style="color:#64748b; font-size:0.9em;">{art['summary']}</p>
                </div>
                """, unsafe_allow_html=True)
                if st.button(f"Baca Detail: {art['title']}", key=f"btn_{page_idx}_{idx}"):
                    st.session_state[f"detail_{page_idx}"] = idx
                    st.rerun()
    else:
        # Tampilan Detail
        idx = st.session_state[f"detail_{page_idx}"]
        art = articles[idx]
        
        if st.button("⬅️ Kembali ke Daftar"):
            st.session_state[f"detail_{page_idx}"] = None
            st.rerun()
            
        st.header(art["title"])
        st.image(art["image_url"], use_container_width=True)
        st.markdown("---")
        st.markdown(art["full_content"])

def show_thanks():
    data = get_thanks_data()
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.balloons()
    
    # UI Box Terima Kasih disamakan dengan index.html
    st.markdown(f"""
    <div style="text-align: center; padding: 40px; background-color: white; border-radius: 20px; border: 1px solid #e2e8f0; shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);">
        <h1 style="color: #2563eb;">🙏 Terima Kasih!</h1>
        <p style="font-size: 1.2em; color: #475569;">{data['message']}</p>
        <br>
        <a href="{data['whatsapp_link']}" target="_blank" style="text-decoration: none;">
            <div style="background-color: #25D366; color: white; padding: 15px 30px; border-radius: 50px; font-weight: bold; display: inline-block; cursor: pointer;">
                Buka Channel WhatsApp
            </div>
        </a>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()