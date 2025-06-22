import streamlit as st
import pandas as pd
import os
from datetime import datetime
import speech_recognition as sr
from pydub import AudioSegment
import tempfile

# ========== Streamlit Page Config ==========
st.set_page_config(
    page_title="Meri Kahaani Zinda Hai",
    page_icon="🕊️",
    layout="centered"
)

# ========== CSV Storage ==========
CSV_FILE = "anonymous_stories.csv"

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

# ========== Convert any audio to WAV ==========
def convert_to_wav(uploaded_file):
    audio_format = uploaded_file.type.split("/")[-1]
    temp_input = tempfile.NamedTemporaryFile(delete=False, suffix="." + audio_format)
    temp_input.write(uploaded_file.read())
    temp_input.flush()

    audio = AudioSegment.from_file(temp_input.name)
    temp_wav = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    audio.export(temp_wav.name, format="wav")
    return temp_wav.name

# ========== Transcribe Hindi Audio ==========
def transcribe_audio(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)
        return recognizer.recognize_google(audio_data, language="hi-IN")

# ========== Multi-Language Dictionary ==========
language = st.selectbox("🌐 Choose Language / भाषा चुनें", ["English", "Hindi", "Tamil", "Bengali"])

translations = {
    "English": {
        "title": "I Am Shakti",
        "subtitle": "A safe space for your voice",
        "upload_audio": "Upload your voice (MP3, WAV, M4A)",
        "write_story": "Write your story",
        "submit": "Submit",
        "success": "Your story has been saved. Thank you!",
        "error": "Please do not submit an empty story.",
        "transcribed": "Transcribed Text (editable):"
    },
    "Hindi": {
        "title": "मैं शक्ति हूँ",
        "subtitle": "आपकी आवाज़ के लिए एक सुरक्षित स्थान",
        "upload_audio": "अपनी आवाज़ अपलोड करें (MP3, WAV, M4A)",
        "write_story": "अपनी कहानी लिखें",
        "submit": "सबमिट करें",
        "success": "आपकी कहानी सेव हो गई है। धन्यवाद!",
        "error": "कृपया खाली कहानी सबमिट न करें।",
        "transcribed": "बदला गया टेक्स्ट (संपादन करें):"
    },
    "Tamil": {
        "title": "நான் சக்தி",
        "subtitle": "உங்கள் குரலுக்கான பாதுகாப்பான இடம்",
        "upload_audio": "உங்கள் குரலை பதிவேற்றவும் (MP3, WAV, M4A)",
        "write_story": "உங்கள் கதையை எழுதுங்கள்",
        "submit": "சமர்ப்பிக்கவும்",
        "success": "உங்கள் கதை சேமிக்கப்பட்டது. நன்றி!",
        "error": "காலியான கதையை சமர்ப்பிக்க வேண்டாம்.",
        "transcribed": "மாற்றிய உரை (திருத்தக்கூடியது):"
    },
    "Bengali": {
        "title": "আমি শক্তি",
        "subtitle": "আপনার কণ্ঠের জন্য একটি নিরাপদ স্থান",
        "upload_audio": "আপনার কণ্ঠ আপলোড করুন (MP3, WAV, M4A)",
        "write_story": "আপনার গল্প লিখুন",
        "submit": "জমা দিন",
        "success": "আপনার গল্প সংরক্ষিত হয়েছে। ধন্যবাদ!",
        "error": "অনুগ্রহ করে খালি গল্প জমা দেবেন না।",
        "transcribed": "লিপ্যন্তরিত পাঠ্য (সম্পাদনাযোগ্য):"
    }
}

T = translations[language]  # selected language text

# ========== Header ==========
st.markdown(f"""
    <div style='text-align: center; padding: 10px;'>
        <h1 style='color:#6b0f1a;'>🕊️ {T['title']}</h1>
        <h4 style='color:#333;'>{T['subtitle']}</h4>
    </div>
""", unsafe_allow_html=True)
st.markdown("---")

# ========== Audio Upload ==========
st.subheader("🎙️ " + T['upload_audio'])
uploaded_audio = st.file_uploader(label="", type=["mp3", "wav", "m4a", "ogg"])

story = ""

if uploaded_audio:
    st.info("⏳ Transcribing audio...")
    try:
        wav_path = convert_to_wav(uploaded_audio)
        text = transcribe_audio(wav_path)
        st.success("✅ Transcription successful!")
        story = st.text_area(T["transcribed"], value=text, height=200)
    except Exception as e:
        st.error(f"⚠️ Error: {e}")
        story = ""

# ========== Text Input ==========
st.subheader("✍️ " + T['write_story'])
story_text = st.text_area(label="", value="", height=300)

if not story and story_text:
    story = story_text

# ========== Submit Button ==========
if st.button("📤 " + T['submit']):
    if story.strip():
        save_story(story)
        st.success("✅ " + T['success'])
    else:
        st.warning("⚠️ " + T['error'])

st.markdown("---")
st.caption("🔐 No personal data is collected. All stories are anonymous.")
