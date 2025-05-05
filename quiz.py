import streamlit as st
import random

# Seviyelere göre kelimeler
word_bank = {
    "Kolay": {
        "elma": "apple",
        "kedi": "cat",
        "su": "water",
        "ev": "house",
        "araba": "car"
    },
    "Orta": {
        "fabrika": "factory",
        "öğretmen": "teacher",
        "yolculuk": "journey",
        "bilgisayar": "computer",
        "uçak": "airplane"
    },
    "Zor": {
        "adalet": "justice",
        "özgürlük": "freedom",
        "karar": "decision",
        "başarı": "success",
        "sabır": "patience"
    }
}

st.title("📘 İngilizce Kelime Quiz")
st.write("Zorluk seviyesini seç, ardından kelimelerin İngilizcesini yaz!")

# Zorluk seçimi
difficulty = st.selectbox("Zorluk Seviyesi Seç", ["Kolay", "Orta", "Zor"])

# Oturum durumu (soru, skor)
if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.question_index = 0
    st.session_state.shuffled_words = list(word_bank[difficulty].items())
    random.shuffle(st.session_state.shuffled_words)

# Yeni oyun başlat butonu
if st.button("🔄 Yeni Oyun Başlat"):
    st.session_state.score = 0
    st.session_state.question_index = 0
    st.session_state.shuffled_words = list(word_bank[difficulty].items())
    random.shuffle(st.session_state.shuffled_words)

# Soruları sırayla göster
if st.session_state.question_index < len(st.session_state.shuffled_words):
    turkish, english = st.session_state.shuffled_words[st.session_state.question_index]
    st.subheader(f"Soru {st.session_state.question_index + 1}: '{turkish}' İngilizce'de ne demektir?")
    user_answer = st.text_input("Cevabın (küçük harf kullan):").strip().lower()

    if st.button("Cevabı Kontrol Et"):
        if user_answer == english:
            st.success("✅ Doğru!")
            st.session_state.score += 1
        else:
            st.error(f"❌ Yanlış! Doğru cevap: {english}")
        st.session_state.question_index += 1
        st.experimental_rerun()
else:
    st.balloons()
    st.success(f"🎉 Quiz Bitti! Toplam Puanın: {st.session_state.score}/{len(st.session_state.shuffled_words)}")
