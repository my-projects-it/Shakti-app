import streamlit as st
import pandas as pd
import os
from datetime import datetime
import speech_recognition as sr
from pydub import AudioSegment
import tempfile
import uuid

if "stories" not in st.session_state:
    st.session_state.stories = []

if "comments" not in st.session_state:
    st.session_state.comments = {}

# ========== Theme Toggle ==========
if "theme" not in st.session_state:
    st.session_state.theme = "dark"  # Default to dark mode

def set_theme(theme):
    if theme == "dark":
        st.markdown("""
        <style>
            .stApp {
                background-color: #0E1117;
                color: white;
            }
            .css-1d391kg, .css-1y4p8pa, .css-1lcbm17, .css-1outpf7 {
                background-color: #0E1117 !important;
            }
            .stTextArea>div>div>textarea, .stTextInput>div>div>input {
                background-color: #262730;
                color: white;
            }
            h1, h2, h3, h4, h5, h6, p, div, span {
                color: white !important;
            }
        </style>
        """, unsafe_allow_html=True)
    else:  # black mode
        st.markdown("""
        <style>
            .stApp {
                background-color: #000000;
                color: white;
            }
            .css-1d391kg, .css-1y4p8pa, .css-1lcbm17, .css-1outpf7 {
                background-color: #000000 !important;
            }
            .stTextArea>div>div>textarea, .stTextInput>div>div>input {
                background-color: #1A1A1A;
                color: white;
            }
            h1, h2, h3, h4, h5, h6, p, div, span {
                color: white !important;
            }
        </style>
        """, unsafe_allow_html=True)

# ========== Page Config ==========
st.set_page_config(
    page_title="Shakti",
    page_icon="📖",
    layout="centered"
)

# ========== Theme Selector ==========
theme_col1, theme_col2 = st.columns([3, 1])
with theme_col2:
    theme = st.selectbox(
        "Theme",
        ["Dark", "Black"],
        index=["Dark", "Black"].index(st.session_state.theme.capitalize()),
        key="theme_select"
    )
    st.session_state.theme = theme.lower()
    set_theme(st.session_state.theme)

# [REST OF THE ORIGINAL CODE REMAINS EXACTLY THE SAME...]
# ========== CSV File Setup ==========
CSV_FILE = "anonymous_stories.csv"

def save_story(text, tags):
    entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "story": text.strip(),
        "tags": ",".join(tags)  # Save tags as comma-separated string
    }
    if os.path.exists(CSV_FILE):
        df = pd.read_csv(CSV_FILE)
        df = pd.concat([df, pd.DataFrame([entry])], ignore_index=True)
    else:
        df = pd.DataFrame([entry])
    df.to_csv(CSV_FILE, index=False)

def load_stories_from_csv():
    if os.path.exists(CSV_FILE):
        df = pd.read_csv(CSV_FILE)
        # Convert DataFrame rows into list of story dicts with tags as list
        stories = []
        for _, row in df.iterrows():
            tags = []
            if "tags" in row and pd.notna(row["tags"]):
                tags = [tag.strip() for tag in row["tags"].split(",") if tag.strip()]
            stories.append({
                "id": str(uuid.uuid4()),  # unique id for session usage
                "text": row["story"],
                "tags": tags
            })
        return stories
    return []

# Load stories from CSV into session state on app start
if not st.session_state.stories:
    st.session_state.stories = load_stories_from_csv()

# ========== Audio Conversion ==========
def convert_to_wav(uploaded_file):
    audio_format = uploaded_file.type.split("/")[-1]
    temp_input = tempfile.NamedTemporaryFile(delete=False, suffix="." + audio_format)
    temp_input.write(uploaded_file.read())
    temp_input.flush()

    audio = AudioSegment.from_file(temp_input.name)
    temp_wav = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    audio.export(temp_wav.name, format="wav")
    return temp_wav.name

# ========== Audio Transcription ==========
def transcribe_audio(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)
        return recognizer.recognize_google(audio_data, language="hi-IN")

# ========== Language Selection ==========
language = st.selectbox("🌐 Choose Language / भाषा चुनें", ["English", "Hindi", "Tamil", "Bengali"])

translations = {
    "English": {
        "title": "Shakti",
        "subtitle": "Your story is still alive",
        "upload_audio": "Upload your voice (MP3, WAV, M4A)",
        "write_story": "Write your story",
        "submit": "Submit",
        "success": "Your story has been saved. Thank you!",
        "error": "Please do not submit an empty story.",
        "transcribed": "Transcribed Text (editable):",
        "add_tags": "Add tags (e.g., #domesticviolence, #healingjourney)",
        "enter_tags": "Enter tags separated by commas:",
        "comment_placeholder": "Add a comment to this story:",
        "post_comment": "Post Comment",
        "comment_empty": "Comment cannot be empty.",
        "comment_posted": "Comment posted!",
        "no_stories": "No stories yet. Submit one above to start the conversation."
    },
    "Hindi": {
        "title": "Shakti",
        "subtitle": "हर आवाज़ अब साँस ले रही है",
        "upload_audio": "अपनी आवाज़ अपलोड करें (MP3, WAV, M4A)",
        "write_story": "अपनी कहानी लिखें",
        "submit": "सबमिट करें",
        "success": "आपकी कहानी सेव हो गई है। धन्यवाद!",
        "error": "कृपया खाली कहानी सबमिट न करें।",
        "transcribed": "बदला गया टेक्स्ट (संपादन करें):",
        "add_tags": "टैग जोड़ें (जैसे, #domesticviolence, #healingjourney)",
        "enter_tags": "कॉमा से टैग दर्ज करें:",
        "comment_placeholder": "इस कहानी पर टिप्पणी जोड़ें:",
        "post_comment": "टिप्पणी भेजें",
        "comment_empty": "टिप्पणी खाली नहीं हो सकती।",
        "comment_posted": "टिप्पणी भेजी गई!",
        "no_stories": "कोई कहानी नहीं है। ऊपर एक सबमिट करें।"
    },
    "Tamil": {
        "title": "என் கதை உயிருடன் உள்ளது",
        "subtitle": "உங்கள் கதை இன்னும் உயிருடன் உள்ளது",
        "upload_audio": "உங்கள் குரலை பதிவேற்றவும் (MP3, WAV, M4A)",
        "write_story": "உங்கள் கதையை எழுதுங்கள்",
        "submit": "சமர்ப்பிக்கவும்",
        "success": "உங்கள் கதை சேமிக்கப்பட்டது. நன்றி!",
        "error": "காலியான கதையை சமர்ப்பிக்க வேண்டாம்.",
        "transcribed": "மாற்றிய உரை (திருத்தக்கூடியது):",
        "add_tags": "டேக்கள் சேர்க்கவும் (எ.கா., #domesticviolence, #healingjourney)",
        "enter_tags": "டேக்களை கமாஸ் கொண்டு பிரித்து உள்ளிடவும்:",
        "comment_placeholder": "இந்த கதைக்கு கருத்து சேர்:",
        "post_comment": "கருத்து பதிவிடு",
        "comment_empty": "கருத்து காலியானதாக இருக்க முடியாது.",
        "comment_posted": "கருத்து பதிவிடப்பட்டது!",
        "no_stories": "கதைகள் இல்லை. மேலே ஒரு கதையை சமர்ப்பிக்கவும்."
    },
    "Bengali": {
        "title": "আমার গল্প এখনও বেঁচে আছে",
        "subtitle": "আপনার কণ্ঠ এখনো জীবিত",
        "upload_audio": "আপনার কণ্ঠ আপলোড করুন (MP3, WAV, M4A)",
        "write_story": "আপনার গল্প লিখুন",
        "submit": "জমা দিন",
        "success": "আপনার গল্প সংরক্ষিত হয়েছে। ধন্যবাদ!",
        "error": "অনুগ্রহ করে খালি গল্প জমা দেবেন না।",
        "transcribed": "লিপ্যন্তরিত পাঠ্য (সম্পাদনাযোগ্য):",
        "add_tags": "ট্যাগ যোগ করুন (যেমন, #domesticviolence, #healingjourney)",
        "enter_tags": "কমা দিয়ে ট্যাগ লিখুন:",
        "comment_placeholder": "এই গল্পে মন্তব্য যোগ করুন:",
        "post_comment": "মন্তব্য পোস্ট করুন",
        "comment_empty": "মন্তব্য খালি হতে পারে না।",
        "comment_posted": "মন্তব্য পোস্ট হয়েছে!",
        "no_stories": "কোনো গল্প নেই। উপরে একটি জমা দিন।"
    }
}

T = translations[language]

# ========== Header ==========
st.markdown(f"""
    <div style='text-align: center; padding: 10px;'>
        <h1 style='color:white;'>📖 {T['title']}</h1>
        <h4 style='color:#DDD;'>{T['subtitle']}</h4>
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

# ========== Text Area ==========
st.subheader("✍️ " + T['write_story'])
story_text = st.text_area(label="", value="", height=300)

if not story and story_text:
    story = story_text

# ========== Tags Input ==========
st.subheader("🏷️ " + T["add_tags"])
tags_input = st.text_input(T["enter_tags"], value="")
tags = [tag.strip().lower() for tag in tags_input.split(",") if tag.strip()]

# ========== Submit Button ==========
if st.button("📤 " + T['submit']):
    if story.strip():
        save_story(story, tags)

        story_id = str(uuid.uuid4())
        st.session_state.stories.append({"id": story_id, "text": story.strip(), "tags": tags})
        st.session_state.comments[story_id] = []

        st.success("✅ " + T['success'])
    else:
        st.warning("⚠️ " + T['error'])
st.markdown("---")

# ========== Community Stories ==========
st.header("📚 Community Stories")

if not st.session_state.stories:
    st.info(T["no_stories"])
else:
    for story_obj in reversed(st.session_state.stories):
        st.markdown(f"### 🗣️ {story_obj['text']}")
        if story_obj.get("tags"):
            tags_display = " ".join([f"`#{tag}`" for tag in story_obj["tags"]])
            st.markdown(f"**Tags:** {tags_display}")

        # Comment form for each story
        with st.form(key=f"comment_form_{story_obj['id']}"):
            comment_input = st.text_input(
                "💬 " + T["comment_placeholder"],
                key=f"input_{story_obj['id']}"
            )
            post = st.form_submit_button(T["post_comment"])

            if post:
                if comment_input.strip():
                    st.session_state.comments.setdefault(story_obj['id'], []).append(
                        comment_input.strip()
                    )
                    st.success("💬 " + T["comment_posted"])
                else:
                    st.warning("⚠️ " + T["comment_empty"])

        # Display existing comments
        comments = st.session_state.comments.get(story_obj['id'], [])
        if comments:
            st.markdown("**🧵 Comments:**")
            for idx, c in enumerate(comments, 1):
                st.markdown(f"- {c}")

        st.markdown("---")
