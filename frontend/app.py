from flask import Flask, render_template, abort
from flask import request  # tambahin ini di atas

app = Flask(__name__, template_folder='templates', static_folder='static')

penyakit_data = {
     "ringworm": {
        "kucing": {
            "nama": "Ringworm pada Kucing",
            "alias": "Dermatofitosis (Kurap Kucing)",
            "emoji": "🐱🍄",
            "deskripsi": " adalah infeksi jamur superfisial pada kulit, bulu, dan cakar kucing yang paling sering disebabkan oleh jamur Microsporum canis. Jamur ini tidak disebabkan oleh cacing, melainkan hidup dengan memetabolisme protein keratin pada jaringan kulit mati, bulu, dan cakar kucing.",

            "tags": ["🔴 Sangat Menular", "⚠️ Zoonosis Tinggi", "🐱 Kucing", "⏳ Terapi Jangka Panjang"],

            "gejala": [
                "Pitak melingkar di wajah, telinga, kaki, atau ekor",
                "Kulit kering, bersisik, dan kemerahan",
                "Bulu rapuh, patah, dan mudah rontok",
                "Gatal ringan hingga sedang",
                "Kuku dapat menebal atau kusam bila terinfeksi"
            ],

            "penyebab": [
                "Infeksi jamur Microsporum canis",
                "Lingkungan lembap dan kurang bersih",
                "Daya tahan tubuh lemah, terutama pada anak kucing"
            ],

            "penularan": [
                "Kontak langsung dengan kucing terinfeksi",
                "Melalui kandang, sisir, alas tidur, atau bulu rontok",
                "Dapat menular ke manusia"
            ],

            "pencegahan": [
                "Menjaga kebersihan lingkungan dan kandang",
                "Mengisolasi kucing yang terinfeksi",
                "Membersihkan bulu rontok secara rutin",
                "Mendisinfeksi perlengkapan kucing"
            ],

            "medis": [
                "Lesi menyebar ke banyak bagian tubuh",
                "Muncul luka terbuka atau infeksi sekunder",
                "Kucing terus menggaruk atau tampak lemas"
            ],

            "pengobatan": [
                "Mandi dengan sampo antijamur",
                "Pemberian obat antijamur oral sesuai resep",
                "Pencukuran bulu pada area tertentu bila perlu",
                "Terapi dilanjutkan hingga infeksi benar-benar hilang"
            ],

            "gambar": "info.jpg"

        },

        "anjing": {
            "nama": "Ringworm pada Anjing",
            "alias": "Dermatofitosis (Kurap Anjing)",
            "emoji": "🐶🍄",
            "deskripsi": " adalah infeksi jamur superfisial pada kulit dan bulu anjing yang memicu peradangan pada folikel rambut. Berbeda dengan kucing, anjing hampir selalu menunjukkan gejala klinis yang jelas.",
            "tags": ["🟠 Menular", "⚠️ Zoonosis", "🐶 Anjing", "🔥 Inflamasi Tinggi"],

             "gejala": [
                "Pitak melingkar kemerahan",
                "Bulu mudah patah",
                "Kulit bersisik atau bernanah",
                "Gatal ringan hingga berat"
            ],

            "penyebab": [
                "Infeksi jamur dermatofit",
                "Luka kecil pada kulit",
                "Stres atau imun lemah"
            ],

            "penularan": [
                "Kontak dengan hewan terinfeksi",
                "Melalui kandang atau alat grooming",
                "Dapat menular ke manusia"
            ],

            "pencegahan": [
                "Membersihkan alat grooming",
                "Mengisolasi hewan terinfeksi",
                "Menjaga kandang tetap kering",
                "Mencuci alas tidur rutin"
            ],

            "medis": [
                "Lesi menyebar cepat",
                "Muncul luka bernanah",
                "Garukan berlebihan"
            ],

            "pengobatan": [
                "Mandi sampo antijamur",
                "Obat oral sesuai resep dokter",
                "Antibiotik bila perlu",
                "Terapi hingga sembuh total"
            ],

            "gambar": "info.jpg"
        }
    },

    "scabies": {
    "kucing": {
        "nama": "Scabies",
        "jenis": "Kucing",
        "alias": "Feline Scabies (Kudis Kucing / Kudis Notoedrik)",
        "emoji": "🐱🦠",

        "deskripsi": "/Mange pada kucing adalah penyakit kulit parasitik yang disebabkan oleh infestasi tungau mikroskopis. Tungau hidup di permukaan kulit atau menggali terowongan pada lapisan kulit luar sehingga memicu peradangan dan rasa gatal yang sangat hebat.",

        "tags": [
            "🔴 Sangat Menular",
            "⚠️ Zoonosis",
            "🐱 Kucing",
            "🔥 Gatal Ekstrem"
        ],

        "gejala": [
            "Bulu rontok disertai keropeng tebal berwarna abu-abu kekuningan di wajah",
            "Kotoran telinga hitam pekat menyerupai bubuk kopi",
            "Kucing sering menggelengkan kepala atau mencakar telinga hingga berdarah",
            "Gatal hebat disertai kebotakan luas"
        ],

        "penyebab": [
            "Infestasi tungau Notoedres cati",
            "Infestasi tungau telinga Otodectes cynotis",
            "Kontak fisik dengan kucing terinfeksi"
        ],

        "penularan": [
            "Kontak langsung dengan kucing sakit",
            "Melalui kasur, kandang, atau sisir",
            "Dapat menular sementara ke manusia"
        ],

        "pencegahan": [
            "Mengarantina kucing yang terinfeksi",
            "Menggunakan obat antiparasit rutin",
            "Mencuci perlengkapan dengan air panas",
            "Menjaga kebersihan lingkungan"
        ],

        "medis": [
            "Gatal ekstrem hingga melukai diri sendiri",
            "Keropeng menyebar ke seluruh tubuh",
            "Telinga bernanah atau berbau busuk",
            "Kucing lesu dan tidak mau makan"
        ],

        "pengobatan": [
            "Mandi lime sulfur dip 2%",
            "Obat tetes telinga khusus",
            "Pembersihan liang telinga",
            "Antibiotik bila ada infeksi sekunder"
        ],

        "gambar": "scabies.gif"
    },

    "anjing": {
        "nama": "Scabies",
        "jenis": "Anjing",
        "alias": "Canine Scabies (Kudis Sarkoptik / Demodex)",
        "emoji": "🐶🪳",

        "deskripsi": "/Mange pada anjing adalah infeksi kulit akibat tungau parasit mikroskopis. Bentuk utamanya adalah scabies sarkoptik yang sangat menular serta demodex yang berkaitan dengan penurunan sistem imun.",

        "tags": [
            "🔴 Sangat Menular",
            "⚠️ Risiko ke Manusia",
            "🐶 Anjing",
            "🚨 Butuh Penanganan Cepat"
        ],

        "gejala": [
            "Gatal mendadak yang sangat hebat",
            "Keropeng tebal dan kulit kemerahan",
            "Kulit menebal dan menghitam pada kasus kronis",
            "Kebotakan meluas",
            "Bau tidak sedap akibat infeksi sekunder"
        ],

        "penyebab": [
            "Infestasi tungau Sarcoptes scabiei",
            "Demodex akibat gangguan imun",
            "Kontak dengan anjing terinfeksi"
        ],

        "penularan": [
            "Kontak langsung antar anjing",
            "Melalui kandang atau tempat tidur",
            "Dapat menyebabkan iritasi sementara pada manusia"
        ],

        "pencegahan": [
            "Menghindari kontak dengan anjing liar",
            "Obat antiparasit bulanan",
            "Membersihkan kandang dan perlengkapan"
        ],

        "medis": [
            "Kulit bernanah dan bengkak",
            "Anjing demam atau lemas",
            "Infeksi meluas cepat"
        ],

        "pengobatan": [
            "Obat spot-on seperti Selamectin",
            "Imidacloprid-Moxidectin",
            "Antibiotik untuk infeksi sekunder",
            "Mandi antiseboroik",
            "Hindari ivermectin dosis tinggi pada ras sensitif"
        ],

        "gambar": "scabies.gif"
    }
},

    "hot-spot": {
        "nama": "Hot Spot",
        "alias": "Acute Moist Dermatitis",
        "emoji": "🐶🔥",

        "deskripsi": " adalah peradangan kulit akut yang umum terjadi pada anjing dan jarang ditemukan pada kucing. Kondisi ini ditandai dengan luka merah, basah, terasa gatal, dan dapat berkembang sangat cepat akibat anjing terus menjilat, menggaruk, atau menggigit area kulit yang mengalami iritasi. Jika tidak ditangani, peradangan dapat meluas dan menyebabkan infeksi sekunder.",

        "tags": [
            "🐶 Anjing",
            "🔥 Peradangan Akut",
            "⚠️ Gatal Intens",
            "🚨 Perlu Penanganan Cepat"
        ],

        "gejala": [
            "Luka merah dan basah pada kulit",
            "Rambut rontok di sekitar area luka",
            "Gatal dan sering dijilat atau digaruk",
            "Kulit terasa hangat dan nyeri",
            "Dapat mengeluarkan cairan atau berbau"
        ],

        "penyebab": [
            "Gigitan kutu atau alergi kulit",
            "Kelembapan berlebih pada bulu",
            "Infeksi bakteri sekunder",
            "Menjilat atau menggaruk berlebihan"
        ],

        "penularan": [
            "Tidak menular antar hewan",
            "Tidak menular ke manusia",
            "Terjadi akibat iritasi atau masalah kulit yang mendasari"
        ],

        "pencegahan": [
            "Menjaga kebersihan kulit dan bulu",
            "Mengendalikan kutu dan parasit",
            "Mengeringkan bulu setelah mandi",
            "Segera menangani alergi atau iritasi kulit"
        ],

        "medis": [
            "Luka membesar dengan cepat",
            "Muncul nanah atau bau menyengat",
            "Anjing tampak kesakitan atau lesu",
            "Tidak membaik dalam beberapa hari"
        ],

        "pengobatan": [
            "Mencukur bulu di sekitar area luka",
            "Membersihkan luka dengan antiseptik",
            "Pemberian antibiotik sesuai anjuran dokter hewan",
            "Menggunakan pelindung leher agar tidak dijilat"
        ],

        "gambar": "hotspot.jpg"
    },

    # "malassezia": {
    #     "nama": "Infeksi Malassezia",
    #     "alias": "Yeast Infection",
    #     "emoji": "🧴",
    #     "deskripsi": " adalah kondisi akibat pertumbuhan berlebih jamur ragi Malassezia yang sebenarnya normal ada di kulit hewan. Kondisi ini biasanya terjadi ketika lingkungan kulit menjadi lembap atau sistem imun menurun. Infeksi ini tidak terlalu menular tetapi dapat menyebabkan iritasi dan bau yang khas.",
    #     "tags": ["🟢 Penularan: Rendah", "🐶🐱 Umum"],
    #     "gejala": [
    #         "Kulit berminyak",
    #         "Bau apek menyengat",
    #         "Kulit menghitam atau menebal",
    #         "Gatal dan iritasi"
    #     ],
    #     "penyebab": [
    #         "Pertumbuhan berlebih jamur Malassezia",
    #         "Kondisi kulit lembap",
    #         "Alergi atau imun lemah"
    #     ],
    #     "penularan": [
    #         "Jarang menular",
    #         "Biasanya akibat faktor internal"
    #     ],
    #     "pencegahan": [
    #         "Keringkan bulu setelah mandi",
    #         "Jaga kebersihan kulit",
    #         "Hindari kelembapan berlebih"
    #     ],
    #     "medis": [
    #         "Bau semakin parah",
    #         "Kulit menebal",
    #         "Tidak membaik dengan perawatan biasa"
    #     ],
    #     "pengobatan": [
    #         "Sampo chlorhexidine/ketoconazole",
    #         "Obat topikal",
    #         "Perawatan rutin kulit"
    #     ], 
    #     "gambar": "malassezia.jpg"
    # },

    # "flea_allergy": {
    #     "nama": "Flea Allergy Dermatitis",
    #     "alias": "Dermatitis Alergi Pinjal",
    #     "emoji": "🦟",
    #     "deskripsi": " adalah reaksi alergi terhadap air liur kutu (pinjal). Bahkan satu gigitan kutu dapat memicu reaksi gatal hebat pada hewan yang sensitif. Kondisi ini sangat umum terjadi pada anjing dan kucing yang tidak rutin diberi perlindungan anti kutu.",
    #     "tags": ["🟡 Penularan: Sedang", "🐶🐱 Umum"],
    #     "gejala": [
    #         "Gatal intens terutama di ekor/paha",
    #         "Bintik merah",
    #         "Adanya kotoran kutu (hitam)",
    #         "Sering menggigit tubuh sendiri"
    #     ],
    #     "penyebab": [
    #         "Gigitan kutu (pinjal)",
    #         "Reaksi alergi terhadap air liur kutu"
    #     ],
    #     "penularan": [
    #         "Tidak langsung menular",
    #         "Kutu bisa berpindah antar hewan"
    #     ],
    #     "pencegahan": [
    #         "Obat kutu rutin (spot-on/tablet)",
    #         "Membersihkan lingkungan",
    #         "Cuci tempat tidur hewan"
    #     ],
    #     "medis": [
    #         "Gatal ekstrem",
    #         "Kulit luka akibat garukan",
    #         "Infeksi sekunder"
    #     ],
    #     "pengobatan": [
    #         "Obat anti kutu",
    #         "Antihistamin",
    #         "Perawatan luka"
    #     ],
    #     "gambar": "dermatitis.jpg"
    # }
}

@app.route("/detail/<nama>")
def detail(nama):
    data = penyakit_data.get(nama)

    if not data:
        abort(404)

    confidence = request.args.get("confidence")
    from_detect = request.args.get("from")
    species = request.args.get("species")
    img = request.args.get("img")

    # kalau data punya versi kucing & anjing
    if isinstance(data, dict) and "kucing" in data and "anjing" in data:

        # dari halaman detect → pilih sesuai species
        if species == "cat":
            data = data["kucing"]
        elif species == "dog":
            data = data["anjing"]

        # dari Wikipet → tampil versi umum
        else:
            data = {
                "nama": nama.capitalize(),
                "alias": f"{data['kucing']['alias']} / {data['anjing']['alias']}",
                "emoji": "🐶🐱",
                "deskripsi": data["kucing"]["deskripsi"],
                "tags": ["🐶 Anjing", "🐱 Kucing"],

                "gejala": {
                    "anjing": data["anjing"]["gejala"],
                    "kucing": data["kucing"]["gejala"]
                },
                "penyebab": {
                    "anjing": data["anjing"]["penyebab"],
                    "kucing": data["kucing"]["penyebab"]
                },
                "penularan": {
                    "anjing": data["anjing"]["penularan"],
                    "kucing": data["kucing"]["penularan"]
                },
                "pencegahan": {
                    "anjing": data["anjing"]["pencegahan"],
                    "kucing": data["kucing"]["pencegahan"]
                },
                "medis": {
                    "anjing": data["anjing"]["medis"],
                    "kucing": data["kucing"]["medis"]
                },
                "pengobatan": {
                    "anjing": data["anjing"]["pengobatan"],
                    "kucing": data["kucing"]["pengobatan"]
                },

                "gambar": data["kucing"]["gambar"]
            }

    return render_template(
        "detail.html",
        data=data,
        confidence=confidence,
        from_detect=from_detect,
        species=species,
        img=img
    )

# route lain tetap
@app.route("/")
def index():
    return render_template("index.html")

@app.route('/detect')
def detect():
    return render_template('detect.html')

@app.route('/info')
def info():
    return render_template('info.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5001)
