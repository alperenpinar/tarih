import json
import random

def generate_questions():
    questions = []
    
    # --- Genel Yetenek (60 Soru) ---
    # Türkçe (30 Soru)
    for i in range(1, 31):
        questions.append({
            "id": i,
            "category": "Genel Yetenek - Türkçe",
            "question": f"Türkçe Sorusu {i}: Aşağıdaki cümlelerin hangisinde yazım yanlışı vardır?",
            "options": [
                "Herkes buraya toplanmış.",
                "Bugün de mi gelmeyeceksin?",
                "Bir çok insan bu sorunu yaşıyor.",
                "Oysaki her şeyi planlamıştık.",
                "Sırtında ağır bir çanta vardı."
            ],
            "answer": 2 # Doğru cevap C (Bir çok -> Birçok)
        })

    # Matematik (30 Soru)
    for i in range(31, 61):
        questions.append({
            "id": i,
            "category": "Genel Yetenek - Matematik",
            "question": f"Matematik Sorusu {i-30}: 2x + 5 = 15 denkleminde x kaçtır?",
            "options": [
                "3",
                "4",
                "5",
                "6",
                "7"
            ],
            "answer": 2 # Doğru cevap 5
        })

    # --- Genel Kültür (60 Soru) ---
    # Tarih (27 Soru)
    for i in range(61, 88):
        questions.append({
            "id": i,
            "category": "Genel Kültür - Tarih",
            "question": f"Tarih Sorusu {i-60}: Osmanlı Devleti'nin kurucusu kimdir?",
            "options": [
                "Orhan Gazi",
                "Osman Gazi",
                "Ertuğrul Gazi",
                "I. Murat",
                "Yıldırım Bayezid"
            ],
            "answer": 1 # Doğru cevap Osman Gazi
        })

    # Coğrafya (18 Soru)
    for i in range(88, 106):
        questions.append({
            "id": i,
            "category": "Genel Kültür - Coğrafya",
            "question": f"Coğrafya Sorusu {i-87}: Türkiye'nin en yüksek dağı hangisidir?",
            "options": [
                "Erciyes",
                "Süphan",
                "Ağrı Dağı",
                "Uludağ",
                "Kaçkar Dağı"
            ],
            "answer": 2 # Doğru cevap Ağrı Dağı
        })

    # Vatandaşlık (9 Soru)
    for i in range(106, 115):
        questions.append({
            "id": i,
            "category": "Genel Kültür - Vatandaşlık",
            "question": f"Vatandaşlık Sorusu {i-105}: Türkiye Cumhuriyeti'nin yönetim şekli nedir?",
            "options": [
                "Monarşi",
                "Oligarşi",
                "Teokrasi",
                "Cumhuriyet",
                "Meşrutiyet"
            ],
            "answer": 3 # Doğru cevap Cumhuriyet
        })

    # Güncel Bilgiler (6 Soru)
    for i in range(115, 121):
        questions.append({
            "id": i,
            "category": "Genel Kültür - Güncel Bilgiler",
            "question": f"Güncel Bilgiler Sorusu {i-114}: 2024 Yaz Olimpiyatları hangi şehirde düzenlenmiştir?",
            "options": [
                "Tokyo",
                "Paris",
                "Londra",
                "Los Angeles",
                "Roma"
            ],
            "answer": 1 # Doğru cevap Paris
        })

    return questions

questions_data = generate_questions()

with open('questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions_data, f, ensure_ascii=False, indent=4)

print(f"Toplam {len(questions_data)} soru başarıyla questions.json dosyasına yazıldı.")
