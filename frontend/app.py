from flask import Flask, render_template, abort
from flask import request  # tambahin ini di atas

app = Flask(__name__, template_folder='templates', static_folder='static')

penyakit_data = {
    "ringworm": {
        "nama": "Ringworm",
        "alias": "Dermatofitosis (Kurap)",
        "emoji": "🦠",
        "deskripsi": " atau dermatofitosis adalah infeksi jamur pada kulit yang disebabkan oleh kelompok jamur dermatofit seperti Microsporum dan Trichophyton. Meskipun disebut 'worm', penyakit ini sama sekali bukan disebabkan oleh cacing. Jamur ini hidup dengan memakan keratin pada kulit, bulu, dan kuku, sehingga menyebabkan kerusakan jaringan dan munculnya lesi khas berbentuk lingkaran. Infeksi ini umum terjadi pada kucing dan anjing, terutama yang memiliki sistem imun lemah atau hidup di lingkungan lembap.",
        "tags": ["🟡 Penularan: Tinggi", "⚠️ Zoonosis", "🐶 Kucing & Anjing", "⏳ 2–6 minggu"],
        "gejala": [
            "Pitak berbentuk lingkaran kemerahan",
            "Kulit bersisik atau berkerak",
            "Bulu rapuh dan mudah rontok",
            "Kadang disertai gatal ringan"
        ],
        "penyebab": [
            "Infeksi jamur dermatofit (Microsporum/Trichophyton)",
            "Lingkungan lembap dan kurang higienis",
            "Kontak dengan hewan terinfeksi",
            "Sistem imun lemah"
        ],
        "penularan": [
            "Kontak langsung dengan hewan terinfeksi",
            "Spora jamur pada kandang, sisir, atau kain",
            "Dapat menular ke manusia (zoonosis tinggi)"
        ],
        "pencegahan": [
            "Menjaga kebersihan kandang dan lingkungan",
            "Rutin menjemur hewan di bawah sinar matahari",
            "Mengisolasi hewan yang terinfeksi",
            "Membersihkan alat grooming secara rutin"
        ],
        "medis": [
            "Lesi menyebar luas",
            "Tidak membaik dalam 2–3 minggu",
            "Infeksi terlihat parah atau bernanah"
        ],
        "pengobatan": [
            "Salep antijamur (miconazole/ketoconazole)",
            "Obat oral untuk kasus berat",
            "Sampo khusus (lime sulfur/antifungal)",
            "Perawatan rutin hingga sembuh total"
        ],
        "gambar": "info.jpg"
    },

    "scabies": {
        "nama": "Scabies",
        "alias": "Kudis Sarcoptic",
        "emoji": "🪳",
        "deskripsi": " adalah penyakit kulit akibat infestasi tungau Sarcoptes scabiei yang menggali terowongan di bawah lapisan kulit. Aktivitas tungau ini memicu reaksi alergi hebat sehingga menyebabkan rasa gatal yang ekstrem. Penyakit ini sangat menular antar hewan dan dapat menular sementara ke manusia, meskipun tungau tidak berkembang biak di kulit manusia.",
        "tags": ["🔴 Penularan: Tinggi", "⚠️ Zoonosis", "🐶 Anjing dominan"],
        "gejala": [
            "Gatal sangat hebat",
            "Kerak tebal di telinga, siku, kaki",
            "Kulit merah dan luka akibat garukan",
            "Bulu rontok di area tertentu"
        ],
        "penyebab": [
            "Infestasi tungau Sarcoptes scabiei",
            "Kontak dengan hewan terinfeksi",
            "Lingkungan kotor"
        ],
        "penularan": [
            "Kontak langsung antar hewan",
            "Bisa menular ke manusia (sementara)",
            "Melalui tempat tidur atau kandang"
        ],
        "pencegahan": [
            "Hindari kontak dengan hewan liar",
            "Gunakan obat anti-parasit rutin",
            "Jaga kebersihan kandang"
        ],
        "medis": [
            "Gatal ekstrem tidak terkendali",
            "Luka terbuka akibat garukan",
            "Hewan gelisah atau stres"
        ],
        "pengobatan": [
            "Suntikan ivermectin",
            "Obat spot-on anti tungau",
            "Mandi sulfur"
        ],
        "gambar": "scabies.gif"
    },

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

    return render_template(
        "detail.html",
        data=data,
        confidence=confidence,
        from_detect=from_detect
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