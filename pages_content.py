# File ini berfungsi sebagai "Database" sederhana agar kamu mudah mengubah isi kontennya.

def get_profile_data():
    return {
        "group_name": "Nama Grup Kamu Di Sini",
        "description": """
            Tuliskan deskripsi grup kamu di sini. 
            Kamu bisa menceritakan tentang visi, misi, atau kegiatan rutin yang dilakukan.
            Ini adalah tempat untuk memperkenalkan siapa kalian kepada pengunjung.
        """,
        "image_url": "https://via.placeholder.com/400" # Ganti dengan path file foto kamu, misal: "assets/foto_grup.jpg"
    }

def get_articles_data(page_number):
    # Simulasi data artikel untuk setiap halaman (2, 3, 4, 5)
    # Kamu bisa menambahkan lebih banyak artikel di dalam list ini.
    
    all_pages = {
        1: [ # Halaman 2
            {
                "title": "Artikel Terbaik Murid A",
                "summary": "Ringkasan singkat tentang artikel ini...",
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
                "title": "Karya Kreatif Hal 3",
                "summary": "Deskripsi singkat...",
                "full_content": "Isi lengkap konten halaman 3.",
                "image_url": "https://via.placeholder.com/300"
            }
        ],
        3: [ # Halaman 4
             {
                "title": "Inspirasi Pagi",
                "summary": "Deskripsi singkat...",
                "full_content": "Isi lengkap konten halaman 4.",
                "image_url": "https://via.placeholder.com/300"
            }
        ],
        4: [ # Halaman 5
             {
                "title": "Catatan Akhir Pekan",
                "summary": "Deskripsi singkat...",
                "full_content": "Isi lengkap konten halaman 5.",
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