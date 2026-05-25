from flask import Flask, render_template, abort
from flask import request  # tambahin ini di atas

app = Flask(__name__, template_folder='templates', static_folder='static')

penyakit_data = {
     "ringworm": {
        "kucing": {
            "nama": "Ringworm pada Kucing",
            "alias": "Dermatofitosis (Kurap Kucing)",
            "emoji": "🐱🍄",
            "deskripsi": "Ringworm adalah infeksi jamur superfisial pada kulit, bulu, dan cakar kucing yang paling sering disebabkan oleh jamur Microsporum canis. Jamur ini tidak disebabkan oleh cacing, melainkan hidup dengan memetabolisme protein keratin pada jaringan kulit mati, bulu, dan cakar kucing.",

            "tags": ["🔴 Sangat Menular", "⚠️ Zoonosis Tinggi", "🐱 Kucing", "⏳ Terapi Jangka Panjang"],

            "gejala": [
                "Kebotakan atau pitak melingkar, terutama di area wajah, ujung telinga, kaki, dan ekor",
                "Kulit kering dan bersisik halus yang tampak mirip abu rokok",
                "Bulu di sekitar lesi menjadi rapuh, patah, dan sangat mudah rontok",
                "Kucing berbulu panjang seperti ras Persia sering menjadi pembawa spora tanpa gejala (carrier)",
                "Cakar menebal, rapuh, mengalami perubahan bentuk atau warna kusam jika kuku terinfeksi"
            ],

            "penyebab": [
                "Infeksi jamur Microsporum canis",
                "Kondisi lingkungan yang lembap, kotor, atau kebersihan kandang yang buruk",
                "Sistem kekebalan tubuh yang lemah, terutama pada anak kucing atau kucing stres"
            ],

            "penularan": [
                "Kontak fisik langsung dengan kucing sakit atau carrier",
                "Kontak tidak langsung melalui kandang, sisir, kasur, karpet, atau sofa",
                "Dapat menular sangat mudah ke manusia, khususnya anak-anak dan lansia"
            ],

            "pencegahan": [
                "Menjaga kebersihan lingkungan rumah dan memastikan sirkulasi udara tidak lembap",
                "Segera mengisolasi kucing yang sakit selama masa pengobatan",
                "Membersihkan bulu rontok dengan vakum",
                "Mendisinfeksi permukaan keras dengan larutan pemutih yang diencerkan"
            ],

            "medis": [
                "Kebotakan menyebar cepat ke area tubuh lain",
                "Muncul luka terbuka atau bernanah",
                "Kucing lemas, kehilangan nafsu makan, atau terus menggaruk"
            ],

            "pengobatan": [
                "Memandikan kucing dengan lime sulfur dip 2% atau sampo miconazole + chlorhexidine",
                "Pemberian obat antijamur oral seperti Itraconazole dengan dosis dokter hewan",
                "Pencukuran bulu pada kasus tertentu",
                "Terapi harus dilanjutkan sampai hasil pemeriksaan negatif"
            ],

            "gambar": "info.jpg"
        },

        "anjing": {
            "nama": "Ringworm pada Anjing",
            "alias": "Dermatofitosis (Kurap Anjing)",
            "emoji": "🐶🍄",
            "deskripsi": "Ringworm adalah infeksi jamur superfisial pada kulit dan bulu anjing yang memicu peradangan pada folikel rambut. Berbeda dengan kucing, anjing hampir selalu menunjukkan gejala klinis yang jelas.",
            "tags": ["🟠 Menular", "⚠️ Zoonosis", "🐶 Anjing", "🔥 Inflamasi Tinggi"],

             "gejala": [
                "Pitak melingkar dengan tepi kemerahan meradang",
                "Bulu patah tepat di atas permukaan kulit",
                "Muncul papula atau pustula",
                "Bekas melingkar dengan pinggiran bersisik",
                "Gatal bervariasi, bisa berat jika ada infeksi sekunder"
            ],

           "penyebab": [
                "Infeksi dermatofit",
                "Luka goresan kecil pada kulit",
                "Usia muda, stres, penyakit penyerta"
            ],

            "penularan": [
                "Kontak langsung dengan hewan terinfeksi",
                "Kontak melalui sisir, handuk, kandang, tempat tidur",
                "Dapat menular ke manusia"
            ],

            "pencegahan": [
                "Membersihkan alat grooming rutin",
                "Mengisolasi anjing terinfeksi",
                "Menjaga kandang tetap kering",
                "Mencuci alas tidur secara berkala"
            ],

            "medis": [
                "Lesi meluas cepat",
                "Bisul bernanah dalam",
                "Anjing terus menggaruk atau tampak terganggu"
            ],

            "pengobatan": [
                "Mandi dengan sampo antijamur",
                "Obat oral seperti Itraconazole / Terbinafine sesuai resep dokter",
                "Antibiotik jika ada infeksi sekunder",
                "Pengobatan dilanjutkan sampai hasil evaluasi negatif"
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

        "deskripsi": "Mange pada kucing adalah penyakit kulit parasitik yang disebabkan oleh infestasi tungau mikroskopis. Tungau hidup di permukaan kulit atau menggali terowongan pada lapisan kulit luar sehingga memicu peradangan dan rasa gatal yang sangat hebat.",

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

        "deskripsi": "Mange pada anjing adalah infeksi kulit akibat tungau parasit mikroskopis. Bentuk utamanya adalah scabies sarkoptik yang sangat menular serta demodex yang berkaitan dengan penurunan sistem imun.",

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
}

    "malassezia": {
        "nama": "Infeksi Malassezia",
        "alias": "Yeast Infection",
        "emoji": "🧴",
        "deskripsi": " adalah kondisi akibat pertumbuhan berlebih jamur ragi Malassezia yang sebenarnya normal ada di kulit hewan. Kondisi ini biasanya terjadi ketika lingkungan kulit menjadi lembap atau sistem imun menurun. Infeksi ini tidak terlalu menular tetapi dapat menyebabkan iritasi dan bau yang khas.",
        "tags": ["🟢 Penularan: Rendah", "🐶🐱 Umum"],
        "gejala": [
            "Kulit berminyak",
            "Bau apek menyengat",
            "Kulit menghitam atau menebal",
            "Gatal dan iritasi"
        ],
        "penyebab": [
            "Pertumbuhan berlebih jamur Malassezia",
            "Kondisi kulit lembap",
            "Alergi atau imun lemah"
        ],
        "penularan": [
            "Jarang menular",
            "Biasanya akibat faktor internal"
        ],
        "pencegahan": [
            "Keringkan bulu setelah mandi",
            "Jaga kebersihan kulit",
            "Hindari kelembapan berlebih"
        ],
        "medis": [
            "Bau semakin parah",
            "Kulit menebal",
            "Tidak membaik dengan perawatan biasa"
        ],
        "pengobatan": [
            "Sampo chlorhexidine/ketoconazole",
            "Obat topikal",
            "Perawatan rutin kulit"
        ], 
        "gambar": "malassezia.jpg"
    },

    "flea_allergy": {
        "nama": "Flea Allergy Dermatitis",
        "alias": "Dermatitis Alergi Pinjal",
        "emoji": "🦟",
        "deskripsi": " adalah reaksi alergi terhadap air liur kutu (pinjal). Bahkan satu gigitan kutu dapat memicu reaksi gatal hebat pada hewan yang sensitif. Kondisi ini sangat umum terjadi pada anjing dan kucing yang tidak rutin diberi perlindungan anti kutu.",
        "tags": ["🟡 Penularan: Sedang", "🐶🐱 Umum"],
        "gejala": [
            "Gatal intens terutama di ekor/paha",
            "Bintik merah",
            "Adanya kotoran kutu (hitam)",
            "Sering menggigit tubuh sendiri"
        ],
        "penyebab": [
            "Gigitan kutu (pinjal)",
            "Reaksi alergi terhadap air liur kutu"
        ],
        "penularan": [
            "Tidak langsung menular",
            "Kutu bisa berpindah antar hewan"
        ],
        "pencegahan": [
            "Obat kutu rutin (spot-on/tablet)",
            "Membersihkan lingkungan",
            "Cuci tempat tidur hewan"
        ],
        "medis": [
            "Gatal ekstrem",
            "Kulit luka akibat garukan",
            "Infeksi sekunder"
        ],
        "pengobatan": [
            "Obat anti kutu",
            "Antihistamin",
            "Perawatan luka"
        ],
        "gambar": "dermatitis.jpg"
    }
}

@app.route("/detail/<nama>")
def detail(nama):
    data = penyakit_data.get(nama)
    if not data:
        abort(404)

    confidence = request.args.get("confidence")
    from_detect = request.args.get("from")
    species = request.args.get("species")

    return render_template(
        "detail.html",
        data=data,
        confidence=confidence,
        from_detect=from_detect,
        species=species
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
    app.run(debug=True, port=5001)