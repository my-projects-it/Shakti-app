import streamlit as st
import pandas as pd
from datetime import datetime
import os
import speech_recognition as sr
from pydub import AudioSegment
import tempfile

st.set_page_config(page_title="I Am Shakti", page_icon="🇮🇳", layout="centered")

CSV_FILE = "anonymous_stories.csv"

# Save to CSV
def save_story(text):
    entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "story": text.strip()
    }
    if os.path.exists(CSV_FILE):
        df = pd.read_csv(CSV_FILE)
        df = pd.concat([df, pd.DataFrame([entry])], ignore_index=True)
    else:
        df = pd.DataFrame([entry])
    df.to_csv(CSV_FILE, index=False)

# Convert all audio to WAV for recognition
def convert_to_wav(uploaded_file):
    audio_format = uploaded_file.type.split("/")[-1]
    temp_input = tempfile.NamedTemporaryFile(delete=False, suffix="." + audio_format)
    temp_input.write(uploaded_file.read())
    temp_input.flush()

    audio = AudioSegment.from_file(temp_input.name)
    temp_wav = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    audio.export(temp_wav.name, format="wav")
    return temp_wav.name

# Transcribe Hindi audio
def transcribe_audio(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)
        return recognizer.recognize_google(audio_data, language="hi-IN")

# ================== HEADER ==================
st.markdown("""
    <div style='text-align: center; padding: 10px;'>
        <h1 style='color:#6b0f1a;'>🇮🇳 I Am Shakti</h1>
        <h4 style='color:#333;'>🚨 एक सुरक्षित प्लेटफ़ॉर्म – पहचान गुप्त, आवाज़ सम्मानित</h4>
        <p style='color:#555;'>🎙️ अपनी आवाज़ से या ✍️ लिखकर कहानी भेजें। कोई व्यक्तिगत जानकारी नहीं माँगी जाती।</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# ========== AUDIO INPUT ==========
st.subheader("🎙️ अपनी आवाज़ में कहें")

uploaded_audio = st.file_uploader(
    label="📂 अपनी आवाज़ अपलोड करें (MP3, WAV, M4A, OGG आदि)", 
    type=["mp3", "wav", "m4a", "ogg"]
)

story = ""

if uploaded_audio:
    st.info("⏳ आपकी आवाज़ को प्रोसेस किया जा रहा है...")
    try:
        wav_path = convert_to_wav(uploaded_audio)
        text = transcribe_audio(wav_path)
        st.success("✅ आवाज़ सफलतापूर्वक टेक्स्ट में बदली गई।")
        story = st.text_area("🧾 ट्रांसक्राइब की गई कहानी (ज़रूरत हो तो एडिट करें)", text, height=200)
    except Exception as e:
        st.error("❌ क्षमा करें, आपकी आवाज़ को समझा नहीं जा सका।")
        story = ""

# ========== TEXT INPUT ==========
st.subheader("✍️ खुद लिखें")

story_text = st.text_area("🧾 या यहाँ सीधे लिखें", height=300)
if not story and story_text:
    story = story_text

# ========== SUBMIT ==========
if st.button("📩 सबमिट करें / Submit"):
    if story.strip():
        save_story(story)
        st.success("🎉 आपकी कहानी सुरक्षित रूप से सेव हो गई है। धन्यवाद!")
    else:
        st.warning("⚠️ कृपया खाली कहानी सबमिट न करें।")

# ========== FOOTER ==========
st.markdown("---")
st.caption("🔐 यह प्लेटफ़ॉर्म पूरी तरह से गुप्त और सुरक्षित है।")
st.caption("💬 आपकी कहानी किसी के साथ साझा नहीं की जाएगी।")
st.caption("🌺 आप अकेली नहीं हैं – भारत आपके साथ है।")


