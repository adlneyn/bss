# File ini berfungsi sebagai "Database" sederhana agar kamu mudah mengubah isi kontennya.

def get_profile_data():
    return {
        "group_name": "Byte Syntech Official",
        "description": """
            Byte Syntech School adalah sebuah grup pembelajaran yang berfokus pada pengembangan
            dan pemahaman AI serta teknologi modern, dengan penekanan utama pada kecerdasan buatan,
            yang menjadi wadah kolaboratif bagi para peserta untuk belajar, berbagi insight, mengasah keterampilan,
            dan mengikuti perkembangan teknologi masa depan secara kreatif dan inovatif.
.
        """,
        "image_url": "dwonload/Gemini_Generated_Image_id44k7id44k7id44.jpg"  # Ganti dengan path file foto kamu, misal: "assets/foto_grup.jpg"
    }

def get_articles_data(page_number):
    # Simulasi data artikel untuk setiap halaman (2, 3, 4, 5)
    # Kamu bisa menambahkan lebih banyak artikel di dalam list ini.
    
    all_pages = {
        1: [ # Halaman 2
            {
                "title": "Artikel NN",
                "summary": "Deskripsi singkat tentang artikel NN...",
                "full_content": "Ini adalah isi lengkap dari artikel murid A yang sangat panjang dan detail.",
                "image_url": "https://via.placeholder.com/300"
            },
            {
                "title": "Karya Literasi Murid B",
                "summary": "Ringkasan singkat tentang karya B...",
                "full_content": "Ini adalah detail dari karya literasi murid B.",
                "image_url": "https://via.placeholder.com/300"
            }
        ],
        2: [ # Halaman 3
            {
                "title": "Artikel NN",
                "summary": "Deskripsi singkat tentang artikel NN...",
                "full_content": "Ini adalah isi lengkap dari artikel murid A yang sangat panjang dan detail.",
                "image_url": "https://via.placeholder.com/300"
            },
            {
                "title": "Karya Literasi Murid B",
                "summary": "Ringkasan singkat tentang karya B...",
                "full_content": "Ini adalah detail dari karya literasi murid B.",
                "image_url": "https://via.placeholder.com/300"
            }
        ],
        3: [ # Halaman 4
             {
                "title": "Artikel NN",
                "summary": "Deskripsi singkat tentang artikel NN...",
                "full_content": "Ini adalah isi lengkap dari artikel murid A yang sangat panjang dan detail.",
                "image_url": "https://via.placeholder.com/300"
            },
            {
                "title": "Karya Literasi Murid B",
                "summary": "Ringkasan singkat tentang karya B...",
                "full_content": "Ini adalah detail dari karya literasi murid B.",
                "image_url": "https://via.placeholder.com/300"
            }
        ],
        4: [ # Halaman 5
             {
                "title": "Artikel NN",
                "summary": "Deskripsi singkat tentang artikel NN...",
                "full_content": "Ini adalah isi lengkap dari artikel murid A yang sangat panjang dan detail.",
                "image_url": "https://via.placeholder.com/300"
            },
            {
                "title": "Karya Literasi Murid B",
                "summary": "Ringkasan singkat tentang karya B...",
                "full_content": "Ini adalah detail dari karya literasi murid B.",
                "image_url": "https://via.placeholder.com/300"
            }
        ]
    }
    return all_pages.get(page_number, [])

def get_thanks_data():
    return {
        "message": "Terima kasih telah berkunjung ke website kami!",
        "whatsapp_link": "https://whatsapp.com/channel/xxxxxx" # Ganti dengan link channel WA kamu
    }