import streamlit as st
import random

# === Kelime verisi (zorluk seviyelerine göre) ===
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

# === Sayfa başlığı ve yapılandırma ===
st.set_page_config(page_title="İngilizce Quiz", page_icon="🧠", layout="centered")
st.markdown("<h1 style='text-align: center;'>📘 İngilizce Kelime Quiz</h1>", unsafe_allow_html=True)
st.markdown("---")

# === Zorluk seçimi ===
difficulty = st.selectbox("Zorluk Seviyesi Seç:", list(word_bank.keys()))

# === Oyun durumu ===
if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.index = 0
    st.session_state.started = False
    st.session_state.word_list = []

# === Oyun başlat butonu ===
if st.button("▶️ Oyunu Başlat / Sıfırla"):
    st.session_state.score = 0
    st.session_state.index = 0
    st.session_state.started = True
    st.session_state.word_list = list(word_bank[difficulty].items())
    random.shuffle(st.session_state.word_list)

# === Quiz başlatıldıysa ===
if st.session_state.started:
    if st.session_state.index < len(st.session_state.word_list):
        turkish, english = st.session_state.word_list[st.session_state.index]
        st.subheader(f"Soru {st.session_state.index + 1}: '{turkish}' ne demektir?")
        user_input = st.text_input("Cevabını gir:", key=st.session_state.index).strip().lower()

        if st.button("✅ Cevabı Kontrol Et"):
            if user_input == english:
                st.success("✅ Doğru!")
                st.session_state.score += 1
            else:
                st.error(f"❌ Yanlış! Doğru cevap: {english}")
            st.session_state.index += 1
            st.experimental_rerun()
    else:
        st.balloons()
        st.success(f"🎉 Quiz Bitti! Skorun: {st.session_state.score}/{len(st.session_state.word_list)}")
        st.session_state.started = False

