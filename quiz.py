import streamlit as st
import random

# Sayfa başlık ve stil ayarları
st.set_page_config(page_title="İngilizce Quiz", page_icon="📘", layout="centered")

st.markdown("""
    <style>
    .stApp {
        background-color: #30353d;
        color: white;
    }
    .main {
        background-color: #30353d;
        padding: 2rem;
        border-radius: 15px;
        color: white;
    }
    .stButton > button {
        background-color: #0098b3;
        color: white;
        padding: 12px 20px;
        border-radius: 10px;
        font-size: 18px;
        margin-top: 20px;
    }
    .stTextInput > div > input {
        padding: 12px;
        border-radius: 10px;
        font-size: 18px;
        background-color: #3b3f4a;
        color: white;
        border: 1px solid #adacbf;
        margin-top: 20px;
    }
    .stTextInput > div > input:focus {
        border-color: #6e6e73;
    }
    .stMarkdown, .stSuccess, .stWarning, .stInfo, .stCaption {
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# === Kelime verisi (zorluk seviyelerine göre) ===
word_bank = {
    "1.ünite": {
        "Tall": "Uzun",
        "Slim": "Zayıf",
        "Friendly": "Arkadaş canlısı",
        "Honest": "dürüst",
        "Curly": "kıvırcık"
    },
    "2.ünite": {
       "Basketball": "basketbol",
        "Tennis": "tenis",
        "Coach": "antrenör",
        "Net": "File",
        "ball": "top"
    },
    "3.ünite": {
        "Born": "doğmak",
"Die": "ölmek",
"Famous": "ünlü",
"Inventor": "mucit",
"Success": "başarı",
 
    },
    "4.ünite": {
    "Lion": "aslan",

"Elephant": "fil",

"Tiger": "kaplan",

"Dangerous": "tehlikeli",

"Habitat": "yaşam alanı",
},
"5.ünite": {
    "Cartoon": "çizgi film",

"News": "haberler",

"Reality show": "gerçeklik programı",

"Remote control": "kumanda",

"Channel": "kanal",
},
"6.ünite": {
    "Birthday": "doğum günü",

"Wedding": "düğün",

"Cake": "pasta",

"Gift": "hediye",

"Invitation": "davetiye",
},
"7.ünite": {
    "Dream": "hayal",

"Future": "gelecek",

"Job": "iş",

"Pilot": "pilot",

"Achieve": "başarmak",
},
"8.ünite" : {
    "Hospital": "hastane",

"Police station": "karakol",

"Museum": "müze",

"Fire station": "itfaiye",

"Library": "kütüphane",
},
"9.ünite" : {
    "Pollution": "kirlilik",

"Recycle": "geri dönüştürmek",

"Nature": "doğa",

"Forest": "orman",

"Climate": "iklim",

},

}

# === Başlık ve tanıtım ===
st.title("📘 İngilizce Kelime Quiz")
st.markdown("""
    🔍 **Kelime Ezberleme Asistanı'na** hoş geldiniz. 
    Aşağıya seçtiğiniz üniteye göre quiz başlatabilirsiniz.
""")

# === Zorluk Seçimi ===
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
        user_input = st.text_input("Cevabınızı girin:", key=st.session_state.index).strip().lower()

        if st.button("✅ Cevabı Kontrol Et"):
            if user_input == english:
                st.success("✅ Doğru!")
                st.session_state.score += 1
            else:
                st.error(f"❌ Yanlış! Doğru cevap: {english}")
            st.session_state.index += 1
            st.experimental_rerun()

else:
    st.success(f"🎉 Quiz Bitti! Skorunuz: {st.session_state.score}/{len(st.session_state.word_list)}")
    if st.session_state.score == 4:
        st.balloons()
    st.session_state.started = False



st.markdown("---")
st.caption("Aykut ATAK / 518 *(2025)*")
