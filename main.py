import random
import time
import os

print('''
Selamat Datang
Silahkan input data diri anda
Jika anda sudah input data diri anda nanti akan ada sesi game tebak-tebakan dimana anda harus memilih pilihan yang benar.
''')

dev = "Lirhza"
name = input("Silahkan masukkan nama anda: ")
usia = input("Berapakah usia anda: ")
alasan = input(f"Sekarang beritahu alasan anda mencoba karya buatan dari {dev}: ")

kepastian = input(f"Apakah ini benar anda {name}? (Y/N): ").upper()

if kepastian == 'Y':
    print(f'''
| Selamat datang {name} | 
| Umur Anda adalah {usia} tahun |
''')
else:
    print("Silakan jalankan ulang program")
    exit()

lanjut = input(f"{name}, Apakah anda ingin melanjutkan dengan bermain game? (Y/N): ").upper()

if lanjut == 'Y':
    os.system('cls' if os.name == 'nt' else 'clear')

    print(f'''
*** Haloo {name}, selamat datang di game sederhana buatan saya ***

Disini anda akan menjadi seorang detektif yang dimana anda harus memecahkan sebuah kasus pembunuhan.
Dibawah ini ada beberapa pilihan ganda tentang kasus pembunuhan, jawab dengan benar untuk menyelesaikan kasus ini!
''')

    questions = [
        {
            "question": "Barang apa yang digunakan oleh pembunuh tersebut untuk melakukan pembunuhan?",
            "choices": ["A. Pisau", "B. Tongkat golf", "C. Palu", "D. Pistol"],
            "correct": random.choice(["Pisau", "Tongkat golf", "Palu", "Pistol"])  # Bukti yang dipilih secara acak
        },
        {
            "question": "Dimana korban ditemukan?",
            "choices": ["A. Kamar tidur", "B. Ruang tamu", "C. Dapur", "D. Garasi"],
            "correct": "Kamar tidur"
        },
        {
            "question": "Siapa yang menemukan korban?",
            "choices": ["A. Tetangga", "B. Saudara", "C. Teman", "D. Polisi"],
            "correct": "Tetangga"
        },
        {
            "question": "Apa motif pembunuhannya?",
            "choices": ["A. Cemburu", "B. Uang", "C. Dendam", "D. Tidak dikenal"],
            "correct": "Uang"
        },
        {
            "question": "Apa yang ditemukan di tangan korban?",
            "choices": ["A. Kunci", "B. Pisau", "C. Ponsel", "D. Surat"],
            "correct": "Kunci"
        },
        {
            "question": "Berapa jumlah luka yang ada pada korban?",
            "choices": ["A. 1", "B. 3", "C. 5", "D. 7"],
            "correct": "3"
        },
        {
            "question": "Apa pekerjaan korban?",
            "choices": ["A. Dokter", "B. Insinyur", "C. Pengusaha", "D. Guru"],
            "correct": "Pengusaha"
        },
        {
            "question": "Dimana tersangka terakhir terlihat?",
            "choices": ["A. Restoran", "B. Stasiun", "C. Kantor", "D. Rumah korban"],
            "correct": "Restoran"
        },
        {
            "question": "Apa jenis kendaraan yang digunakan tersangka?",
            "choices": ["A. Motor", "B. Mobil", "C. Sepeda", "D. Taksi"],
            "correct": "Mobil"
        },
        {
            "question": "Berapa usia korban?",
            "choices": ["A. 25 tahun", "B. 30 tahun", "C. 35 tahun", "D. 40 tahun"],
            "correct": "30 tahun"
        }
    ]

    random.shuffle(questions)

    for i, q in enumerate(questions[:10], 1):
        print(f"\nPertanyaan {i}: {q['question']}")
        for choice in q["choices"]:
            print(choice)

        time.sleep(1)

        pilihan_user = input("Jawaban anda (A/B/C/D): ").upper()

        pilihan_dict = {
            'A': q["choices"][0].split(". ")[1],
            'B': q["choices"][1].split(". ")[1],
            'C': q["choices"][2].split(". ")[1],
            'D': q["choices"][3].split(". ")[1],
        }

        if pilihan_dict.get(pilihan_user) == q["correct"]:
            print(f"Selamat {name}, pilihan anda benar! Jawaban yang benar adalah {q['correct']}.")
        else:
            print(f"Yahh, pilihan anda salah. Jawaban yang benar adalah {q['correct']}.")

        time.sleep(2)
else:
    print("Silakan jalankan ulang program")
