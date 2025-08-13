# # import streamlit as st
# # import pandas as pd
# # import os
# # from datetime import datetime
# # import speech_recognition as sr
# # from pydub import AudioSegment
# # import tempfile

# # # ========== Page Config ==========
# # st.set_page_config(
# #     page_title="Shakti",
# #     page_icon="📖",
# #     layout="centered"
# # )

# # # ========== CSV File Setup ==========
# # CSV_FILE = "anonymous_stories.csv"

# # def save_story(text):
# #     entry = {
# #         "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
# #         "story": text.strip()
# #     }
# #     if os.path.exists(CSV_FILE):
# #         df = pd.read_csv(CSV_FILE)
# #         df = pd.concat([df, pd.DataFrame([entry])], ignore_index=True)
# #     else:
# #         df = pd.DataFrame([entry])
# #     df.to_csv(CSV_FILE, index=False)

# # # ========== Audio Conversion ==========
# # def convert_to_wav(uploaded_file):
# #     audio_format = uploaded_file.type.split("/")[-1]
# #     temp_input = tempfile.NamedTemporaryFile(delete=False, suffix="." + audio_format)
# #     temp_input.write(uploaded_file.read())
# #     temp_input.flush()

# #     audio = AudioSegment.from_file(temp_input.name)
# #     temp_wav = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
# #     audio.export(temp_wav.name, format="wav")
# #     return temp_wav.name

# # # ========== Audio Transcription ==========
# # def transcribe_audio(audio_path):
# #     recognizer = sr.Recognizer()
# #     with sr.AudioFile(audio_path) as source:
# #         audio_data = recognizer.record(source)
# #         return recognizer.recognize_google(audio_data, language="hi-IN")

# # # ========== Language Selection ==========
# # language = st.selectbox("🌐 Choose Language / भाषा चुनें", ["English", "Hindi", "Tamil", "Bengali"])

# # translations = {
# #     "English": {
# #         "title": "Shakti",
# #         "subtitle": "Your story is still alive",
# #         "upload_audio": "Upload your voice (MP3, WAV, M4A)",
# #         "write_story": "Write your story",
# #         "submit": "Submit",
# #         "success": "Your story has been saved. Thank you!",
# #         "error": "Please do not submit an empty story.",
# #         "transcribed": "Transcribed Text (editable):"
# #     },
# #     "Hindi": {
# #         "title": "Shakti",
# #         "subtitle": "हर आवाज़ अब साँस ले रही है",
# #         "upload_audio": "अपनी आवाज़ अपलोड करें (MP3, WAV, M4A)",
# #         "write_story": "अपनी कहानी लिखें",
# #         "submit": "सबमिट करें",
# #         "success": "आपकी कहानी सेव हो गई है। धन्यवाद!",
# #         "error": "कृपया खाली कहानी सबमिट न करें।",
# #         "transcribed": "बदला गया टेक्स्ट (संपादन करें):"
# #     },
# #     "Tamil": {
# #         "title": "என் கதை உயிருடன் உள்ளது",
# #         "subtitle": "உங்கள் கதை இன்னும் உயிருடன் உள்ளது",
# #         "upload_audio": "உங்கள் குரலை பதிவேற்றவும் (MP3, WAV, M4A)",
# #         "write_story": "உங்கள் கதையை எழுதுங்கள்",
# #         "submit": "சமர்ப்பிக்கவும்",
# #         "success": "உங்கள் கதை சேமிக்கப்பட்டது. நன்றி!",
# #         "error": "காலியான கதையை சமர்ப்பிக்க வேண்டாம்.",
# #         "transcribed": "மாற்றிய உரை (திருத்தக்கூடியது):"
# #     },
# #     "Bengali": {
# #         "title": "আমার গল্প এখনও বেঁচে আছে",
# #         "subtitle": "আপনার কণ্ঠ এখনো জীবিত",
# #         "upload_audio": "আপনার কণ্ঠ আপলোড করুন (MP3, WAV, M4A)",
# #         "write_story": "আপনার গল্প লিখুন",
# #         "submit": "জমা দিন",
# #         "success": "আপনার গল্প সংরক্ষিত হয়েছে। ধন্যবাদ!",
# #         "error": "অনুগ্রহ করে খালি গল্প জমা দেবেন না।",
# #         "transcribed": "লিপ্যন্তরিত পাঠ্য (সম্পাদনাযোগ্য):"
# #     }
# # }

# # T = translations[language]

# # # ========== Header ==========
# # st.markdown(f"""
# #     <div style='text-align: center; padding: 10px;'>
# #         <h1 style='color:#4a2c2a;'>📖 {T['title']}</h1>
# #         <h4 style='color:#555;'>{T['subtitle']}</h4>
# #     </div>
# # """, unsafe_allow_html=True)
# # st.markdown("---")

# # # ========== Audio Upload ==========
# # st.subheader("🎙️ " + T['upload_audio'])
# # uploaded_audio = st.file_uploader(label="", type=["mp3", "wav", "m4a", "ogg"])

# # story = ""

# # if uploaded_audio:
# #     st.info("⏳ Transcribing audio...")
# #     try:
# #         wav_path = convert_to_wav(uploaded_audio)
# #         text = transcribe_audio(wav_path)
# #         st.success("✅ Transcription successful!")
# #         story = st.text_area(T["transcribed"], value=text, height=200)
# #     except Exception as e:
# #         st.error(f"⚠️ Error: {e}")
# #         story = ""

# # # ========== Text Area ==========
# # st.subheader("✍️ " + T['write_story'])
# # story_text = st.text_area(label="", value="", height=300)

# # if not story and story_text:
# #     story = story_text

# # # ========== Submit Button ==========
# # if st.button("📤 " + T['submit']):
# #     if story.strip():
# #         save_story(story)
# #         st.success("✅ " + T['success'])
# #     else:
# #         st.warning("⚠️ " + T['error'])

# # st.markdown("---")
# # st.caption("📜 Every word is mine. Every line is my truth. My story is still alive.")


# import streamlit as st
# import pandas as pd
# import os
# from datetime import datetime
# import speech_recognition as sr
# from pydub import AudioSegment
# import tempfile
# import uuid

# if "stories" not in st.session_state:
#     st.session_state.stories = []

# if "comments" not in st.session_state:
#     st.session_state.comments = {}

# # ========== Enhanced Session State ==========
# if "stories" not in st.session_state:
#     st.session_state.stories = []

# if "comments" not in st.session_state:
#     st.session_state.comments = {}

# if "likes" not in st.session_state:
#     st.session_state.likes = {}

# if "user_theme" not in st.session_state:
#     st.session_state.user_theme = "warm"

# if "view_mode" not in st.session_state:
#     st.session_state.view_mode = "all"

# # ========== Enhanced Page Config ==========
# st.set_page_config(
#     page_title="Shakti - Share Your Voice",
#     page_icon="🌸",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # ========== Enhanced CSS Styling ==========
# def load_custom_css():
#     """Load enhanced custom CSS for better UI"""
    
#     # Theme configurations
#     themes = {
#         "warm": {
#             "primary": "#d63384",
#             "secondary": "#f8d7da", 
#             "accent": "#fd7e14",
#             "background": "linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%)",
#             "card_bg": "rgba(255, 255, 255, 0.95)",
#             "text": "#2c3e50"
#         },
#         "cool": {
#             "primary": "#0d6efd",
#             "secondary": "#cff4fc",
#             "accent": "#20c997", 
#             "background": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
#             "card_bg": "rgba(255, 255, 255, 0.95)",
#             "text": "#2c3e50"
#         },
#         "nature": {
#             "primary": "#198754",
#             "secondary": "#d1e7dd",
#             "accent": "#ffc107",
#             "background": "linear-gradient(135deg, #a8edea 0%, #fed6e3 100%)",
#             "card_bg": "rgba(255, 255, 255, 0.95)", 
#             "text": "#2c3e50"
#         }
#     }
    
#     current_theme = themes[st.session_state.user_theme]
    
#     st.markdown(f"""
#     <style>
#     /* Global Styles */
#     .stApp {{
#         background: {current_theme["background"]};
#         color: {current_theme["text"]};
#     }}
    
#     /* Enhanced Header */
#     .main-header {{
#         text-align: center;
#         padding: 2rem 0;
#         background: {current_theme["card_bg"]};
#         border-radius: 20px;
#         margin-bottom: 2rem;
#         box-shadow: 0 8px 32px rgba(0,0,0,0.1);
#         backdrop-filter: blur(10px);
#         border: 1px solid rgba(255,255,255,0.2);
#     }}
    
#     .main-title {{
#         font-size: 3.5rem;
#         font-weight: 700;
#         background: linear-gradient(45deg, {current_theme["primary"]}, {current_theme["accent"]});
#         -webkit-background-clip: text;
#         -webkit-text-fill-color: transparent;
#         margin-bottom: 0.5rem;
#         text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
#     }}
    
#     .main-subtitle {{
#         font-size: 1.3rem;
#         color: {current_theme["text"]};
#         font-weight: 300;
#         opacity: 0.8;
#     }}
    
#     /* Enhanced Cards */
#     .story-card {{
#         background: {current_theme["card_bg"]};
#         padding: 2rem;
#         border-radius: 16px;
#         margin: 1.5rem 0;
#         box-shadow: 0 8px 32px rgba(0,0,0,0.1);
#         backdrop-filter: blur(10px);
#         border: 1px solid rgba(255,255,255,0.2);
#         transition: all 0.3s ease;
#         position: relative;
#         overflow: hidden;
#     }}
    
#     .story-card:hover {{
#         transform: translateY(-5px);
#         box-shadow: 0 16px 48px rgba(0,0,0,0.15);
#     }}
    
#     .story-card::before {{
#         content: '';
#         position: absolute;
#         top: 0;
#         left: 0;
#         right: 0;
#         height: 4px;
#         background: linear-gradient(90deg, {current_theme["primary"]}, {current_theme["accent"]});
#     }}
    
#     /* Enhanced Buttons */
#     .stButton > button {{
#         background: linear-gradient(45deg, {current_theme["primary"]}, {current_theme["accent"]});
#         color: white;
#         border: none;
#         padding: 0.75rem 2rem;
#         border-radius: 50px;
#         font-weight: 600;
#         transition: all 0.3s ease;
#         box-shadow: 0 4px 16px rgba(0,0,0,0.2);
#     }}
    
#     .stButton > button:hover {{
#         transform: translateY(-2px);
#         box-shadow: 0 8px 24px rgba(0,0,0,0.3);
#     }}
    
#     /* Enhanced Form Elements */
#     .stTextArea textarea, .stTextInput input {{
#         border-radius: 12px;
#         border: 2px solid {current_theme["secondary"]};
#         background: rgba(255, 255, 255, 0.9);
#         transition: all 0.3s ease;
#     }}
    
#     .stTextArea textarea:focus, .stTextInput input:focus {{
#         border-color: {current_theme["primary"]};
#         box-shadow: 0 0 0 3px rgba(214, 51, 132, 0.1);
#     }}
    
#     /* Enhanced Sidebar */
#     .sidebar-content {{
#         background: {current_theme["card_bg"]};
#         padding: 1.5rem;
#         border-radius: 16px;
#         margin: 1rem 0;
#         box-shadow: 0 4px 16px rgba(0,0,0,0.1);
#     }}
    
#     /* Tag Styling */
#     .story-tag {{
#         display: inline-block;
#         background: linear-gradient(45deg, {current_theme["primary"]}, {current_theme["accent"]});
#         color: white;
#         padding: 0.3rem 0.8rem;
#         border-radius: 20px;
#         font-size: 0.8rem;
#         font-weight: 500;
#         margin: 0.2rem;
#         box-shadow: 0 2px 8px rgba(0,0,0,0.1);
#     }}
    
#     /* Stats Styling */
#     .stats-container {{
#         display: flex;
#         justify-content: space-around;
#         background: {current_theme["card_bg"]};
#         padding: 1.5rem;
#         border-radius: 16px;
#         margin: 1rem 0;
#         box-shadow: 0 4px 16px rgba(0,0,0,0.1);
#     }}
    
#     .stat-item {{
#         text-align: center;
#     }}
    
#     .stat-number {{
#         font-size: 2rem;
#         font-weight: 700;
#         color: {current_theme["primary"]};
#     }}
    
#     .stat-label {{
#         font-size: 0.9rem;
#         color: {current_theme["text"]};
#         opacity: 0.7;
#     }}
    
#     /* Animation Classes */
#     .fade-in {{
#         animation: fadeIn 0.5s ease-in;
#     }}
    
#     @keyframes fadeIn {{
#         from {{ opacity: 0; transform: translateY(20px); }}
#         to {{ opacity: 1; transform: translateY(0); }}
#     }}
    
#     /* Progress Bar */
#     .upload-progress {{
#         background: {current_theme["secondary"]};
#         border-radius: 10px;
#         overflow: hidden;
#         height: 8px;
#         margin: 1rem 0;
#     }}
    
#     .upload-progress-bar {{
#         background: linear-gradient(90deg, {current_theme["primary"]}, {current_theme["accent"]});
#         height: 100%;
#         transition: width 0.3s ease;
#     }}
    
#     /* Floating Action Styles */
#     .floating-stats {{
#         position: fixed;
#         top: 100px;
#         right: 20px;
#         background: {current_theme["card_bg"]};
#         padding: 1rem;
#         border-radius: 16px;
#         box-shadow: 0 8px 32px rgba(0,0,0,0.1);
#         backdrop-filter: blur(10px);
#         z-index: 1000;
#         border: 1px solid rgba(255,255,255,0.2);
#     }}
    
#     /* Mobile Responsive */
#     @media (max-width: 768px) {{
#         .main-title {{
#             font-size: 2.5rem;
#         }}
        
#         .story-card {{
#             padding: 1.5rem;
#             margin: 1rem 0;
#         }}
        
#         .floating-stats {{
#             position: relative;
#             top: auto;
#             right: auto;
#             margin: 1rem 0;
#         }}
#     }}
#     </style>
#     """, unsafe_allow_html=True)

# # ========== Enhanced CSV File Setup ==========
# CSV_FILE = "anonymous_stories.csv"

# def save_story(text, tags):
#     entry = {
#         "id": str(uuid.uuid4()),
#         "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#         "story": text.strip(),
#         "tags": ",".join(tags)  # Save tags as comma-separated string
#     }
    
#     if os.path.exists(CSV_FILE):
#         df = pd.read_csv(CSV_FILE)
#         df = pd.concat([df, pd.DataFrame([entry])], ignore_index=True)
#     else:
#         df = pd.DataFrame([entry])
#     df.to_csv(CSV_FILE, index=False)
#     return entry["id"]

# def load_stories_from_csv():
#     if os.path.exists(CSV_FILE):
#         df = pd.read_csv(CSV_FILE)
#         # Convert DataFrame rows into list of story dicts with tags as list
#         stories = []
#         for _, row in df.iterrows():
#             tags = []
#             if "tags" in row and pd.notna(row["tags"]):
#                 tags = [tag.strip() for tag in row["tags"].split(",") if tag.strip()]
#             stories.append({
#                 "id": str(uuid.uuid4()),  # unique id for session usage
#                 "text": row["story"],
#                 "tags": tags
#             })
#         return stories
#     return []

# # Load stories from CSV into session state on app start
# if not st.session_state.stories:
#     st.session_state.stories = load_stories_from_csv()

# # ========== Audio Conversion ==========
# def convert_to_wav(uploaded_file):
#     """Enhanced audio conversion with progress indication"""
#     audio_format = uploaded_file.type.split("/")[-1]
#     temp_input = tempfile.NamedTemporaryFile(delete=False, suffix="." + audio_format)
#     temp_input.write(uploaded_file.read())
#     temp_input.flush()

#     audio = AudioSegment.from_file(temp_input.name)
#     temp_wav = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
#     audio.export(temp_wav.name, format="wav")
    
#     # Return both path and duration
#     duration = len(audio) / 1000  # Duration in seconds
#     return temp_wav.name, duration

# def transcribe_audio(audio_path):
#     """Enhanced audio transcription with language detection"""
#     recognizer = sr.Recognizer()
#     with sr.AudioFile(audio_path) as source:
#         audio_data = recognizer.record(source)
#         return recognizer.recognize_google(audio_data, language="hi-IN")

# # ========== Language Selection ==========
# language = st.selectbox("🌐 Choose Language / भाषा चुनें", ["English", "Hindi", "Tamil", "Bengali"])

# translations = {
#     "English": {
#         "title": "Shakti",
#         "subtitle": "Your story is still alive",
#         "upload_audio": "Upload your voice (MP3, WAV, M4A)",
#         "write_story": "Write your story",
#         "submit": "Submit",
#         "success": "Your story has been saved. Thank you!",
#         "error": "Please do not submit an empty story.",
#         "transcribed": "Transcribed Text (editable):",
#         "add_tags": "Add tags (e.g., #domesticviolence, #healingjourney)",
#         "enter_tags": "Enter tags separated by commas:",
#         "comment_placeholder": "Add a comment to this story:",
#         "post_comment": "Post Comment",
#         "comment_empty": "Comment cannot be empty.",
#         "comment_posted": "Comment posted!",
#         "no_stories": "No stories yet. Submit one above to start the conversation."
#     },
#     "Hindi": {
#         "title": "Shakti",
#         "subtitle": "हर आवाज़ अब साँस ले रही है",
#         "upload_audio": "अपनी आवाज़ अपलोड करें (MP3, WAV, M4A)",
#         "write_story": "अपनी कहानी लिखें",
#         "submit": "सबमिट करें",
#         "success": "आपकी कहानी सेव हो गई है। धन्यवाद!",
#         "error": "कृपया खाली कहानी सबमिट न करें।",
#         "transcribed": "बदला गया टेक्स्ट (संपादन करें):",
#         "add_tags": "टैग जोड़ें (जैसे, #domesticviolence, #healingjourney)",
#         "enter_tags": "कॉमा से टैग दर्ज करें:",
#         "comment_placeholder": "इस कहानी पर टिप्पणी जोड़ें:",
#         "post_comment": "टिप्पणी भेजें",
#         "comment_empty": "टिप्पणी खाली नहीं हो सकती।",
#         "comment_posted": "टिप्पणी भेजी गई!",
#         "no_stories": "कोई कहानी नहीं है। ऊपर एक सबमिट करें।"
#     },
#     "Tamil": {
#         "title": "என் கதை உயிருடன் உள்ளது",
#         "subtitle": "உங்கள் கதை இன்னும் உயிருடன் உள்ளது",
#         "upload_audio": "உங்கள் குரலை பதிவேற்றவும் (MP3, WAV, M4A)",
#         "write_story": "உங்கள் கதையை எழுதுங்கள்",
#         "submit": "சமர்ப்பிக்கவும்",
#         "success": "உங்கள் கதை சேமிக்கப்பட்டது. நன்றி!",
#         "error": "காலியான கதையை சமர்ப்பிக்க வேண்டாம்.",
#         "transcribed": "மாற்றிய உரை (திருத்தக்கூடியது):",
#         "add_tags": "டேக்கள் சேர்க்கவும் (எ.கா., #domesticviolence, #healingjourney)",
#         "enter_tags": "டேக்களை கமாஸ் கொண்டு பிரித்து உள்ளிடவும்:",
#         "comment_placeholder": "இந்த கதைக்கு கருத்து சேர்:",
#         "post_comment": "கருத்து பதிவிடு",
#         "comment_empty": "கருத்து காலியானதாக இருக்க முடியாது.",
#         "comment_posted": "கருத்து பதிவிடப்பட்டது!",
#         "no_stories": "கதைகள் இல்லை. மேலே ஒரு கதையை சமர்ப்பிக்கவும்."
#     },
#     "Bengali": {
#         "title": "আমার গল্প এখনও বেঁচে আছে",
#         "subtitle": "আপনার কণ্ঠ এখনো জীবিত",
#         "upload_audio": "আপনার কণ্ঠ আপলোড করুন (MP3, WAV, M4A)",
#         "write_story": "আপনার গল্প লিখুন",
#         "submit": "জমা দিন",
#         "success": "আপনার গল্প সংরক্ষিত হয়েছে। ধন্যবাদ!",
#         "error": "অনুগ্রহ করে খালি গল্প জমা দেবেন না।",
#         "transcribed": "লিপ্যন্তরিত পাঠ্য (সম্পাদনাযোগ্য):",
#         "add_tags": "ট্যাগ যোগ করুন (যেমন, #domesticviolence, #healingjourney)",
#         "enter_tags": "কমা দিয়ে ট্যাগ লিখুন:",
#         "comment_placeholder": "এই গল্পে মন্তব্য যোগ করুন:",
#         "post_comment": "মন্তব্য পোস্ট করুন",
#         "comment_empty": "মন্তব্য খালি হতে পারে না।",
#         "comment_posted": "মন্তব্য পোস্ট হয়েছে!",
#         "no_stories": "কোনো গল্প নেই। উপরে একটি জমা দিন।"
#     }

# # ========== Enhanced Main App ==========
# def main():
#     # Load custom CSS
#     load_custom_css()
    
#     # Sidebar for settings and filters
#     with st.sidebar:
#         st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
        
#         # Language selection
#         language = st.selectbox(
#             "🌐 Language / भाषा / மொழி / ভাষা", 
#             ["English", "Hindi", "Tamil", "Bengali"],
#             help="Choose your preferred language"
#         )
        
#         # Theme selection
#         st.markdown("### 🎨 Theme")
#         theme_option = st.radio(
#             "Choose theme:",
#             ["warm", "cool", "nature"],
#             format_func=lambda x: {"warm": "🌸 Warm", "cool": "🌊 Cool", "nature": "🌿 Nature"}[x],
#             horizontal=True
#         )
        
#         if theme_option != st.session_state.user_theme:
#             st.session_state.user_theme = theme_option
#             st.rerun()
        
#         # View filters
#         st.markdown("### 📊 Filters")
#         view_mode = st.selectbox(
#             "View stories:",
#             ["all", "recent", "popular"],
#             format_func=lambda x: {"all": "All Stories", "recent": "Recent", "popular": "Most Supported"}[x]
#         )
#         st.session_state.view_mode = view_mode
        
#         # Search functionality
#         search_query = st.text_input("🔍 Search stories...", placeholder="Type keywords...")
        
#         st.markdown('</div>', unsafe_allow_html=True)
    
#     # Get translations
#     translations = get_enhanced_translations()
#     T = translations[language]
    
#     # Enhanced Header
#     st.markdown(f"""
#     <div class="main-header fade-in">
#         <h1 class="main-title">🌸 {T['title']}</h1>
#         <p class="main-subtitle">{T['subtitle']}</p>
#         <p style="font-style: italic; opacity: 0.6; margin-top: 0.5rem;">{T['tagline']}</p>
#     </div>
# """, unsafe_allow_html=True)
# st.markdown("---")

# # ========== Audio Upload ==========
# st.subheader("🎙️ " + T['upload_audio'])
# uploaded_audio = st.file_uploader(label="", type=["mp3", "wav", "m4a", "ogg"])

# story = ""

# if uploaded_audio:
#     st.info("⏳ Transcribing audio...")
#     try:
#         wav_path = convert_to_wav(uploaded_audio)
#         text = transcribe_audio(wav_path)
#         st.success("✅ Transcription successful!")
#         story = st.text_area(T["transcribed"], value=text, height=200)
#     except Exception as e:
#         st.error(f"⚠️ Error: {e}")
#         story = ""

# # ========== Text Area ==========
# st.subheader("✍️ " + T['write_story'])
# story_text = st.text_area(label="", value="", height=300)

# if not story and story_text:
#     story = story_text

# # ========== Tags Input ==========
# st.subheader("🏷️ " + T["add_tags"])
# tags_input = st.text_input(T["enter_tags"], value="")
# tags = [tag.strip().lower() for tag in tags_input.split(",") if tag.strip()]

# # ========== Submit Button ==========
# if st.button("📤 " + T['submit']):
#     if story.strip():
#         save_story(story, tags)

#         story_id = str(uuid.uuid4())
#         st.session_state.stories.append({"id": story_id, "text": story.strip(), "tags": tags})
#         st.session_state.comments[story_id] = []

#         st.success("✅ " + T['success'])
#     else:
#         st.warning("⚠️ " + T['error'])
# st.markdown("---")

# # ========== Community Stories ==========
# st.header("📚 Community Stories")

# if not st.session_state.stories:
#     st.info(T["no_stories"])
# else:
#     for story_obj in reversed(st.session_state.stories):
#         st.markdown(f"### 🗣️ {story_obj['text']}")
#         if story_obj.get("tags"):
#             tags_display = " ".join([f"`#{tag}`" for tag in story_obj["tags"]])
#             st.markdown(f"**Tags:** {tags_display}")

#         # Comment form for each story
#         with st.form(key=f"comment_form_{story_obj['id']}"):
#             comment_input = st.text_input(
#                 "💬 " + T["comment_placeholder"],
#                 key=f"input_{story_obj['id']}"
#             )
#             post = st.form_submit_button(T["post_comment"])

#             if post:
#                 if comment_input.strip():
#                     st.session_state.comments.setdefault(story_obj['id'], []).append(
#                         comment_input.strip()
#                     )
#                     st.success("💬 " + T["comment_posted"])
#                 else:
#                     st.warning("⚠️ " + T["comment_empty"])

#         # Display existing comments
#         comments = st.session_state.comments.get(story_obj['id'], [])
#         if comments:
#             st.markdown("**🧵 Comments:**")
#             for idx, c in enumerate(comments, 1):
#                 st.markdown(f"- {c}")

#         st.markdown("---")
import streamlit as st
import pandas as pd
import os
from datetime import datetime
import speech_recognition as sr
from pydub import AudioSegment
import tempfile
import uuid
import time

# ========== Enhanced Session State ==========
if "stories" not in st.session_state:
    st.session_state.stories = []

if "comments" not in st.session_state:
    st.session_state.comments = {}

if "likes" not in st.session_state:
    st.session_state.likes = {}

if "user_theme" not in st.session_state:
    st.session_state.user_theme = "warm"

if "view_mode" not in st.session_state:
    st.session_state.view_mode = "all"

# ========== Enhanced Page Config ==========
st.set_page_config(
    page_title="Shakti - Share Your Voice",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ========== Enhanced CSS Styling ==========
def load_custom_css():
    """Load enhanced custom CSS for better UI"""
    
    # Theme configurations
    themes = {
        "warm": {
            "primary": "#d63384",
            "secondary": "#f8d7da", 
            "accent": "#fd7e14",
            "background": "linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%)",
            "card_bg": "rgba(255, 255, 255, 0.95)",
            "text": "#2c3e50"
        },
        "cool": {
            "primary": "#0d6efd",
            "secondary": "#cff4fc",
            "accent": "#20c997", 
            "background": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
            "card_bg": "rgba(255, 255, 255, 0.95)",
            "text": "#2c3e50"
        },
        "nature": {
            "primary": "#198754",
            "secondary": "#d1e7dd",
            "accent": "#ffc107",
            "background": "linear-gradient(135deg, #a8edea 0%, #fed6e3 100%)",
            "card_bg": "rgba(255, 255, 255, 0.95)", 
            "text": "#2c3e50"
        }
    }
    
    current_theme = themes[st.session_state.user_theme]
    
    st.markdown(f"""
    <style>
    /* Global Styles */
    .stApp {{
        background: {current_theme["background"]};
        color: {current_theme["text"]};
    }}
    
    /* Enhanced Header */
    .main-header {{
        text-align: center;
        padding: 2rem 0;
        background: {current_theme["card_bg"]};
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.2);
    }}
    
    .main-title {{
        font-size: 3.5rem;
        font-weight: 700;
        background: linear-gradient(45deg, {current_theme["primary"]}, {current_theme["accent"]});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }}
    
    .main-subtitle {{
        font-size: 1.3rem;
        color: {current_theme["text"]};
        font-weight: 300;
        opacity: 0.8;
    }}
    
    /* Enhanced Cards */
    .story-card {{
        background: {current_theme["card_bg"]};
        padding: 2rem;
        border-radius: 16px;
        margin: 1.5rem 0;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.2);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }}
    
    .story-card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 16px 48px rgba(0,0,0,0.15);
    }}
    
    .story-card::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, {current_theme["primary"]}, {current_theme["accent"]});
    }}
    
    /* Enhanced Buttons */
    .stButton > button {{
        background: linear-gradient(45deg, {current_theme["primary"]}, {current_theme["accent"]});
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 50px;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 16px rgba(0,0,0,0.2);
    }}
    
    .stButton > button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(0,0,0,0.3);
    }}
    
    /* Enhanced Form Elements */
    .stTextArea textarea, .stTextInput input {{
        border-radius: 12px;
        border: 2px solid {current_theme["secondary"]};
        background: rgba(255, 255, 255, 0.9);
        transition: all 0.3s ease;
    }}
    
    .stTextArea textarea:focus, .stTextInput input:focus {{
        border-color: {current_theme["primary"]};
        box-shadow: 0 0 0 3px rgba(214, 51, 132, 0.1);
    }}
    
    /* Enhanced Sidebar */
    .sidebar-content {{
        background: {current_theme["card_bg"]};
        padding: 1.5rem;
        border-radius: 16px;
        margin: 1rem 0;
        box-shadow: 0 4px 16px rgba(0,0,0,0.1);
    }}
    
    /* Tag Styling */
    .story-tag {{
        display: inline-block;
        background: linear-gradient(45deg, {current_theme["primary"]}, {current_theme["accent"]});
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 500;
        margin: 0.2rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }}
    
    /* Stats Styling */
    .stats-container {{
        display: flex;
        justify-content: space-around;
        background: {current_theme["card_bg"]};
        padding: 1.5rem;
        border-radius: 16px;
        margin: 1rem 0;
        box-shadow: 0 4px 16px rgba(0,0,0,0.1);
    }}
    
    .stat-item {{
        text-align: center;
    }}
    
    .stat-number {{
        font-size: 2rem;
        font-weight: 700;
        color: {current_theme["primary"]};
    }}
    
    .stat-label {{
        font-size: 0.9rem;
        color: {current_theme["text"]};
        opacity: 0.7;
    }}
    
    /* Animation Classes */
    .fade-in {{
        animation: fadeIn 0.5s ease-in;
    }}
    
    @keyframes fadeIn {{
        from {{ opacity: 0; transform: translateY(20px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}
    
    /* Progress Bar */
    .upload-progress {{
        background: {current_theme["secondary"]};
        border-radius: 10px;
        overflow: hidden;
        height: 8px;
        margin: 1rem 0;
    }}
    
    .upload-progress-bar {{
        background: linear-gradient(90deg, {current_theme["primary"]}, {current_theme["accent"]});
        height: 100%;
        transition: width 0.3s ease;
    }}
    
    /* Floating Action Styles */
    .floating-stats {{
        position: fixed;
        top: 100px;
        right: 20px;
        background: {current_theme["card_bg"]};
        padding: 1rem;
        border-radius: 16px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        backdrop-filter: blur(10px);
        z-index: 1000;
        border: 1px solid rgba(255,255,255,0.2);
    }}
    
    /* Mobile Responsive */
    @media (max-width: 768px) {{
        .main-title {{
            font-size: 2.5rem;
        }}
        
        .story-card {{
            padding: 1.5rem;
            margin: 1rem 0;
        }}
        
        .floating-stats {{
            position: relative;
            top: auto;
            right: auto;
            margin: 1rem 0;
        }}
    }}
    </style>
    """, unsafe_allow_html=True)

# ========== Enhanced CSV File Setup ==========
CSV_FILE = "anonymous_stories.csv"

def save_story(text, tags, audio_duration=None):
    """Enhanced story saving with additional metadata"""
    entry = {
        "id": str(uuid.uuid4()),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "story": text.strip(),
        "tags": ",".join(tags),
        "word_count": len(text.split()),
        "audio_duration": audio_duration or 0,
        "likes": 0
    }
    
    if os.path.exists(CSV_FILE):
        df = pd.read_csv(CSV_FILE)
        df = pd.concat([df, pd.DataFrame([entry])], ignore_index=True)
    else:
        df = pd.DataFrame([entry])
    df.to_csv(CSV_FILE, index=False)
    return entry["id"]

def load_stories_from_csv():
    """Enhanced story loading with metadata"""
    if os.path.exists(CSV_FILE):
        df = pd.read_csv(CSV_FILE)
        stories = []
        for _, row in df.iterrows():
            tags = []
            if "tags" in row and pd.notna(row["tags"]):
                tags = [tag.strip() for tag in row["tags"].split(",") if tag.strip()]
            
            story_id = row.get("id", str(uuid.uuid4()))
            stories.append({
                "id": story_id,
                "text": row["story"],
                "tags": tags,
                "timestamp": row.get("timestamp", ""),
                "word_count": row.get("word_count", len(row["story"].split())),
                "audio_duration": row.get("audio_duration", 0),
                "likes": row.get("likes", 0)
            })
        return stories
    return []

# Load stories from CSV into session state on app start
if not st.session_state.stories:
    st.session_state.stories = load_stories_from_csv()

# ========== Enhanced Audio Functions ==========
def convert_to_wav(uploaded_file):
    """Enhanced audio conversion with progress indication"""
    audio_format = uploaded_file.type.split("/")[-1]
    temp_input = tempfile.NamedTemporaryFile(delete=False, suffix="." + audio_format)
    temp_input.write(uploaded_file.read())
    temp_input.flush()

    audio = AudioSegment.from_file(temp_input.name)
    temp_wav = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    audio.export(temp_wav.name, format="wav")
    
    # Return both path and duration
    duration = len(audio) / 1000  # Duration in seconds
    return temp_wav.name, duration

def transcribe_audio(audio_path):
    """Enhanced audio transcription with language detection"""
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)
        return recognizer.recognize_google(audio_data, language="hi-IN")

# ========== Enhanced Language System ==========
def get_enhanced_translations():
    """Enhanced translations with more UI elements"""
    return {
        "English": {
            "title": "Shakti",
            "subtitle": "Every voice deserves to be heard",
            "tagline": "Share your story, inspire others",
            "upload_audio": "🎙️ Share Your Voice",
            "write_story": "✍️ Write Your Story",
            "submit": "Share Story",
            "success": "Your story has been shared successfully!",
            "error": "Please don't submit an empty story.",
            "transcribed": "Voice to Text (you can edit):",
            "add_tags": "Add Tags",
            "enter_tags": "Enter tags separated by commas (e.g., strength, hope, journey)",
            "comment_placeholder": "Add an encouraging comment...",
            "post_comment": "Post Comment",
            "comment_empty": "Please write a comment before posting.",
            "comment_posted": "Thank you for your support!",
            "no_stories": "Be the first to share your story and inspire others.",
            "total_stories": "Stories Shared",
            "total_words": "Words of Strength",
            "community_support": "Community Voices",
            "filter_all": "All Stories",
            "filter_recent": "Recent",
            "filter_popular": "Most Supported",
            "search_placeholder": "Search stories...",
            "reading_time": "min read",
            "like_story": "❤️ Support",
            "liked_story": "💖 Supported"
        },
        "Hindi": {
            "title": "शक्ति",
            "subtitle": "हर आवाज़ सुनी जाने की हकदार है",
            "tagline": "अपनी कहानी साझा करें, दूसरों को प्रेरित करें",
            "upload_audio": "🎙️ अपनी आवाज़ साझा करें",
            "write_story": "✍️ अपनी कहानी लिखें",
            "submit": "कहानी साझा करें",
            "success": "आपकी कहानी सफलतापूर्वक साझा की गई!",
            "error": "कृपया खाली कहानी सबमिट न करें।",
            "transcribed": "आवाज़ से टेक्स्ट (आप संपादित कर सकते हैं):",
            "add_tags": "टैग जोड़ें",
            "enter_tags": "कॉमा से अलग करके टैग दर्ज करें (जैसे, शक्ति, आशा, यात्रा)",
            "comment_placeholder": "एक प्रोत्साहनजनक टिप्पणी जोड़ें...",
            "post_comment": "टिप्पणी भेजें",
            "comment_empty": "कृपया भेजने से पहले टिप्पणी लिखें।",
            "comment_posted": "आपके समर्थन के लिए धन्यवाद!",
            "no_stories": "पहले व्यक्ति बनें जो कहानी साझा करे और दूसरों को प्रेरित करे।",
            "total_stories": "साझा की गई कहानियाँ",
            "total_words": "शक्ति के शब्द",
            "community_support": "समुदायिक आवाज़ें",
            "filter_all": "सभी कहानियाँ",
            "filter_recent": "हाल की",
            "filter_popular": "सबसे समर्थित",
            "search_placeholder": "कहानियाँ खोजें...",
            "reading_time": "मिनट पढ़ना",
            "like_story": "❤️ समर्थन",
            "liked_story": "💖 समर्थित"
        },
        "Tamil": {
            "title": "சக்தி",
            "subtitle": "ஒவ்வொரு குரலும் கேட்கப்பட வேண்டும்",
            "tagline": "உங்கள் கதையைப் பகிருங்கள், மற்றவர்களை ஊக்குவியுங்கள்",
            "upload_audio": "🎙️ உங்கள் குரலைப் பகிருங்கள்",
            "write_story": "✍️ உங்கள் கதையை எழுதுங்கள்",
            "submit": "கதையைப் பகிருங்கள்",
            "success": "உங்கள் கதை வெற்றிகரமாகப் பகிரப்பட்டது!",
            "error": "காலியான கதையை சமர்ப்பிக்க வேண்டாம்.",
            "transcribed": "குரலிலிருந்து உரை (நீங்கள் திருத்தலாம்):",
            "add_tags": "குறிச்சொற்களைச் சேர்க்கவும்",
            "enter_tags": "கமாக்களால் பிரிக்கப்பட்ட குறிச்சொற்களை உள்ளிடவும்",
            "comment_placeholder": "ஊக்கமளிக்கும் கருத்தைச் சேர்க்கவும்...",
            "post_comment": "கருத்தை இடுகையிடவும்",
            "comment_empty": "இடுகையிடும் முன் கருத்து எழுதவும்.",
            "comment_posted": "உங்கள் ஆதரவிற்கு நன்றி!",
            "no_stories": "கதை பகிர்ந்து மற்றவர்களை ஊக்குவிக்கும் முதல் நபராக இருங்கள்.",
            "total_stories": "பகிரப்பட்ட கதைகள்",
            "total_words": "வலிமையின் வார்த்தைகள்",
            "community_support": "சமூகக் குரல்கள்",
            "filter_all": "அனைத்து கதைகள்",
            "filter_recent": "சமீபத்திய",
            "filter_popular": "மிகவும் ஆதரிக்கப்பட்ட",
            "search_placeholder": "கதைகளைத் தேடுங்கள்...",
            "reading_time": "நிமிட வாசிப்பு",
            "like_story": "❤️ ஆதரவு",
            "liked_story": "💖 ஆதரிக்கப்பட்டது"
        },
        "Bengali": {
            "title": "শক্তি",
            "subtitle": "প্রতিটি কণ্ঠস্বর শোনার যোগ্য",
            "tagline": "আপনার গল্প শেয়ার করুন, অন্যদের অনুপ্রাণিত করুন",
            "upload_audio": "🎙️ আপনার কণ্ঠ শেয়ার করুন",
            "write_story": "✍️ আপনার গল্প লিখুন",
            "submit": "গল্প শেয়ার করুন",
            "success": "আপনার গল্প সফলভাবে শেয়ার হয়েছে!",
            "error": "অনুগ্রহ করে খালি গল্প জমা দেবেন না।",
            "transcribed": "কণ্ঠ থেকে লেখা (আপনি সম্পাদনা করতে পারেন):",
            "add_tags": "ট্যাগ যোগ করুন",
            "enter_tags": "কমা দিয়ে পৃথক করে ট্যাগ লিখুন",
            "comment_placeholder": "একটি উৎসাহব্যঞ্জক মন্তব্য যোগ করুন...",
            "post_comment": "মন্তব্য পোস্ট করুন",
            "comment_empty": "পোস্ট করার আগে মন্তব্য লিখুন।",
            "comment_posted": "আপনার সমর্থনের জন্য ধন্যবাদ!",
            "no_stories": "গল্প শেয়ার করে অন্যদের অনুপ্রাণিত করার প্রথম ব্যক্তি হন।",
            "total_stories": "শেয়ার করা গল্পগুলি",
            "total_words": "শক্তির শব্দসমূহ",
            "community_support": "সম্প্রদায়ের কণ্ঠস্বর",
            "filter_all": "সব গল্প",
            "filter_recent": "সাম্প্রতিক",
            "filter_popular": "সবচেয়ে সমর্থিত",
            "search_placeholder": "গল্প খুঁজুন...",
            "reading_time": "মিনিট পড়া",
            "like_story": "❤️ সমর্থন",
            "liked_story": "💖 সমর্থিত"
        }
    }

# ========== Enhanced Main App ==========
def main():
    # Load custom CSS
    load_custom_css()
    
    # Sidebar for settings and filters
    with st.sidebar:
        st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
        
        # Language selection
        language = st.selectbox(
            "🌐 Language / भाषा / மொழி / ভাষা", 
            ["English", "Hindi", "Tamil", "Bengali"],
            help="Choose your preferred language"
        )
        
        # Theme selection
        st.markdown("### 🎨 Theme")
        theme_option = st.radio(
            "Choose theme:",
            ["warm", "cool", "nature"],
            format_func=lambda x: {"warm": "🌸 Warm", "cool": "🌊 Cool", "nature": "🌿 Nature"}[x],
            horizontal=True
        )
        
        if theme_option != st.session_state.user_theme:
            st.session_state.user_theme = theme_option
            st.rerun()
        
        # View filters
        st.markdown("### 📊 Filters")
        view_mode = st.selectbox(
            "View stories:",
            ["all", "recent", "popular"],
            format_func=lambda x: {"all": "All Stories", "recent": "Recent", "popular": "Most Supported"}[x]
        )
        st.session_state.view_mode = view_mode
        
        # Search functionality
        search_query = st.text_input("🔍 Search stories...", placeholder="Type keywords...")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Get translations
    translations = get_enhanced_translations()
    T = translations[language]
    
    # Enhanced Header
    st.markdown(f"""
    <div class="main-header fade-in">
        <h1 class="main-title">🌸 {T['title']}</h1>
        <p class="main-subtitle">{T['subtitle']}</p>
        <p style="font-style: italic; opacity: 0.6; margin-top: 0.5rem;">{T['tagline']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Enhanced Stats Dashboard
    total_stories = len(st.session_state.stories)
    total_words = sum(story.get('word_count', 0) for story in st.session_state.stories)
    total_comments = sum(len(comments) for comments in st.session_state.comments.values())
    
    st.markdown(f"""
    <div class="stats-container fade-in">
        <div class="stat-item">
            <div class="stat-number">{total_stories}</div>
            <div class="stat-label">{T['total_stories']}</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">{total_words:,}</div>
            <div class="stat-label">{T['total_words']}</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">{total_comments}</div>
            <div class="stat-label">{T['community_support']}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Main content in columns
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Enhanced Story Submission
        with st.expander("✨ " + T['upload_audio'], expanded=True):
            uploaded_audio = st.file_uploader(
                "Choose audio file", 
                type=["mp3", "wav", "m4a", "ogg"],
                help="Upload your voice recording in MP3, WAV, M4A, or OGG format"
            )
            
            story = ""
            audio_duration = None
            
            if uploaded_audio:
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                status_text.text("🎵 Processing audio...")
                progress_bar.progress(25)
                
                try:
                    wav_path, audio_duration = convert_to_wav(uploaded_audio)
                    progress_bar.progress(50)
                    
                    status_text.text("🎤 Transcribing speech...")
                    text = transcribe_audio(wav_path)
                    progress_bar.progress(100)
                    
                    status_text.success("✅ Audio processed successfully!")
                    
                    story = st.text_area(
                        T["transcribed"], 
                        value=text, 
                        height=150,
                        help="You can edit the transcribed text before sharing"
                    )
                    
                    # Show audio info
                    if audio_duration:
                        st.info(f"🎵 Audio duration: {audio_duration:.1f} seconds")
                        
                except Exception as e:
                    st.error(f"⚠️ Error processing audio: {str(e)}")
                    story = ""
        
        # Enhanced Text Story Input
        with st.expander("📝 " + T['write_story'], expanded=not story):
            story_text = st.text_area(
                "Share your story", 
                value="", 
                height=200,
                placeholder="Your story matters. Share your experience, strength, and hope...",
                help="Write your story in your own words. Every voice matters."
            )
            
            if not story and story_text:
                story = story_text
        
        # Enhanced Tags Input
        st.markdown(f"### 🏷️ {T['add_tags']}")
        col_tags1, col_tags2 = st.columns([3, 1])
        
        with col_tags1:
            tags_input = st.text_input(
                "Tags", 
                placeholder=T["enter_tags"],
                help="Add relevant tags to help others find your story"
            )
        
        with col_tags2:
            if st.button("💡 Suggest Tags", help="Get tag suggestions"):
                suggested_tags = ["strength", "healing", "hope", "survivor", "journey", "empowerment"]
                st.info("💡 Suggested: " + ", ".join(suggested_tags))
        
        tags = [tag.strip().lower() for tag in tags_input.split(",") if tag.strip()]
        
        # Enhanced Submit Button
        col_submit1, col_submit2, col_submit3 = st.columns([1, 2, 1])
        with col_submit2:
            if st.button(f"🌟 {T['submit']}", use_container_width=True):
                if story.strip():
                    story_id = save_story(story, tags, audio_duration)
                    
                    # Add to session state
                    new_story = {
                        "id": story_id,
                        "text": story.strip(),
                        "tags": tags,
                        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "word_count": len(story.split()),
                        "audio_duration": audio_duration or 0,
                        "likes": 0
                    }
                    st.session_state.stories.append(new_story)
                    st.session_state.comments[story_id] = []
                    st.session_state.likes[story_id] = 0
                    
                    st.success(f"🎉 {T['success']}")
                    st.balloons()
                    time.sleep(2)
                    st.rerun()
                else:
                    st.warning(f"⚠️ {T['error']}")
    
    with col2:
        # Community Insights
        st.markdown("### 📈 Community Insights")
        
        if st.session_state.stories:
            # Most used tags
            all_tags = []
            for story in st.session_state.stories:
                all_tags.extend(story.get('tags', []))
            
            if all_tags:
                from collections import Counter
                tag_counts = Counter(all_tags)
                st.markdown("**🏷️ Popular Tags:**")
                for tag, count in tag_counts.most_common(5):
                    st.markdown(f"`#{tag}` ({count})")
            
            # Recent activity
            st.markdown("**⏰ Recent Activity:**")
            recent_stories = sorted(st.session_state.stories, 
                                  key=lambda x: x.get('timestamp', ''), 
                                  reverse=True)[:3]
            
            for story in recent_stories:
                preview = story['text'][:50] + "..." if len(story['text']) > 50 else story['text']
                st.markdown(f"• {preview}")
    
    st.markdown("---")
    
    # Enhanced Community Stories Section
    st.markdown("## 📚 Community Stories")
    
    # Filter and search stories
    filtered_stories = st.session_state.stories.copy()
    
    # Apply search filter
    if search_query:
        filtered_stories = [
            story for story in filtered_stories 
            if search_query.lower() in story['text'].lower() 
            or any(search_query.lower() in tag for tag in story.get('tags', []))
        ]
    
    # Apply view mode filter
    if st.session_state.view_mode == "recent":
        filtered_stories = sorted(filtered_stories, 
                                key=lambda x: x.get('timestamp', ''), 
                                reverse=True)
    elif st.session_state.view_mode == "popular":
        filtered_stories = sorted(filtered_stories, 
                                key=lambda x: st.session_state.likes.get(x['id'], 0), 
                                reverse=True)
    
    if not filtered_stories:
        st.info(f"🌟 {T['no_stories']}")
    else:
        # Display stories with enhanced UI
        for idx, story_obj in enumerate(filtered_stories):
            with st.container():
                st.markdown(f"""
                <div class="story-card fade-in">
                """, unsafe_allow_html=True)
                
                # Story header with metadata
                col_story1, col_story2, col_story3 = st.columns([3, 1, 1])
                
                with col_story1:
                    # Reading time calculation
                    words = len(story_obj['text'].split())
                    reading_time = max(1, words // 200)  # Assume 200 words per minute
                    
                    st.markdown(f"**📖 Story #{len(filtered_stories) - idx}**")
                    st.caption(f"⏱️ {reading_time} {T['reading_time']} • 📝 {words} words")
                
                with col_story2:
                    # Like button
                    story_id = story_obj['id']
                    current_likes = st.session_state.likes.get(story_id, 0)
                    
                    if st.button(f"❤️ {current_likes}", key=f"like_{story_id}"):
                        st.session_state.likes[story_id] = current_likes + 1
                        st.rerun()
                
                with col_story3:
                    # Share button (placeholder)
                    if st.button("🔗 Share", key=f"share_{story_id}"):
                        st.info("Link copied to clipboard! (Feature coming soon)")
                
                # Story content
                st.markdown(f"""
                <div style="
                    background: rgba(255,255,255,0.7);
                    padding: 1.5rem;
                    border-radius: 12px;
                    margin: 1rem 0;
                    border-left: 4px solid #d63384;
                    font-size: 1.1rem;
                    line-height: 1.6;
                ">
                    {story_obj['text']}
                </div>
                """, unsafe_allow_html=True)
                
                # Tags display
                if story_obj.get("tags"):
                    st.markdown("**Tags:** " + " ".join([f'<span class="story-tag">#{tag}</span>' 
                                                       for tag in story_obj["tags"]]), 
                              unsafe_allow_html=True)
                
                # Audio info if available
                if story_obj.get('audio_duration', 0) > 0:
                    st.caption(f"🎵 Original audio: {story_obj['audio_duration']:.1f} seconds")
                
                # Enhanced comment section
                st.markdown("---")
                
                # Comment form
                with st.form(key=f"comment_form_{story_obj['id']}"):
                    comment_input = st.text_area(
                        f"💬 {T['comment_placeholder']}",
                        key=f"input_{story_obj['id']}",
                        height=80,
                        placeholder="Your words of support and encouragement..."
                    )
                    
                    col_comment1, col_comment2 = st.columns([3, 1])
                    with col_comment2:
                        post = st.form_submit_button(
                            f"💌 {T['post_comment']}", 
                            use_container_width=True
                        )
                    
                    if post:
                        if comment_input.strip():
                            st.session_state.comments.setdefault(story_obj['id'], []).append({
                                'text': comment_input.strip(),
                                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            })
                            st.success(f"💖 {T['comment_posted']}")
                            st.rerun()
                        else:
                            st.warning(f"⚠️ {T['comment_empty']}")
                
                # Display existing comments with enhanced styling
                comments = st.session_state.comments.get(story_obj['id'], [])
                if comments:
                    st.markdown("**🧵 Community Support:**")
                    for idx, comment in enumerate(comments[-5:]):  # Show last 5 comments
                        comment_text = comment if isinstance(comment, str) else comment.get('text', comment)
                        comment_time = comment.get('timestamp', '') if isinstance(comment, dict) else ''
                        
                        st.markdown(f"""
                        <div style="
                            background: rgba(32, 201, 151, 0.1);
                            padding: 0.8rem;
                            border-radius: 8px;
                            margin: 0.5rem 0;
                            border-left: 3px solid #20c997;
                        ">
                            💬 {comment_text}
                            {f'<br><small style="opacity: 0.6;">🕒 {comment_time}</small>' if comment_time else ''}
                        </div>
                        """, unsafe_allow_html=True)
                    
                    if len(comments) > 5:
                        st.caption(f"... and {len(comments) - 5} more comments")
                
                st.markdown("</div>", unsafe_allow_html=True)
                st.markdown("<br>", unsafe_allow_html=True)
    
    # Enhanced Footer
    st.markdown("---")
    st.markdown(f"""
    <div style="text-align: center; padding: 2rem; opacity: 0.7;">
        <p>🌸 <strong>Shakti</strong> - Empowering voices, building community</p>
        <p>Every story shared makes our community stronger 💪</p>
        <p>Made with ❤️ for survivors and supporters</p>
    </div>
    """, unsafe_allow_html=True)

# Run the enhanced app
if __name__ == "__main__":
    main()