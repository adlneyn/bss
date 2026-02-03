# File ini berfungsi sebagai "Database" sederhana.

def get_profile_data():
    return {
        "group_name": "Byte Syntech Official",
        "description": """
            Byte Syntech School adalah sebuah grup pembelajaran yang berfokus pada pengembangan
            dan pemahaman AI serta teknologi modern. Kami menjadi wadah kolaboratif bagi para 
            peserta untuk belajar, berbagi insight, mengasah keterampilan,
            dan mengikuti perkembangan teknologi masa depan secara kreatif dan inovatif.
.
        """,
        # Pastikan file ini ada di folder yang sama atau gunakan URL internet
        "image_url": "download/c:\\Users\\ACER\\Downloads\\Gemini_Generated_Image_kb0hkdkb0hkdkb0h.png" 
    }

def get_articles_data(page_number):
    # page_number 1-4 sesuai dengan Artikel Murid (1) s/d (4)
    all_pages = {
        1: [
            {
                "title": "",
                "summary": "Bagaimana AI mengubah cara kita belajar di kelas.",
                "full_content": "Kecerdasan Buatan (AI) kini bukan lagi masa depan, melainkan masa kini. Di sekolah, AI membantu guru menilai tugas lebih cepat dan membantu siswa memahami materi lewat personalisasi pembelajaran.",
                "image_url": "https://images.pexels.com/photos/2599244/pexels-photo-2599244.jpeg"
            },
            {
                "title": "Best Artikel",
                "summary": "Pentingnya menyaring informasi di internet.",
                "full_content": "Literasi digital adalah kemampuan untuk memahami dan menggunakan informasi dari berbagai sumber digital secara efektif dan etis.",
                "image_url": "https://images.pexels.com/photos/159866/books-book-pages-read-literature-159866.jpeg"
            },
        ],
        2: [
            {
                "title": "Best Student",
                "summary": "Melihat teknologi yang akan populer di 2030.",
                "full_content": "Dari Quantum Computing hingga mobil terbang, masa depan tampak sangat cerah bagi para pengembang teknologi.",
                "image_url": "https://images.pexels.com/photos/3861969/pexels-photo-3861969.jpeg"
            },
        ],
        3: [
            {
                "title": "Best Reaction",
                "summary": "Melihat teknologi yang akan populer di 2030.",
                "full_content": "Dari Quantum Computing hingga mobil terbang, masa depan tampak sangat cerah bagi para pengembang teknologi.",
                "image_url": "https://images.pexels.com/photos/3861969/pexels-photo-3861969.jpeg"
            },
        ],
        4: [
            {
                "title": "King and Queen",
                "summary": "Melihat teknologi yang akan populer di 2030.",
                "full_content": "Dari Quantum Computing hingga mobil terbang, masa depan tampak sangat cerah bagi para pengembang teknologi.",
                "image_url": "https://images.pexels.com/photos/3861969/pexels-photo-3861969.jpeg"
            },
        ]
    }
    return all_pages.get(page_number, [])

def get_thanks_data():
    return {
        "message": "Terima kasih telah berkunjung ke Official Website Bytesyntech. Kami sangat menghargai dukungan Anda!",
        "whatsapp_link": "https://whatsapp.com/channel/xxxxxx" 
    }