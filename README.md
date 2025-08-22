# 🧊 AI Icebreakers

AI Icebreakers is a lightweight Streamlit app that generates short, fun, and creative icebreaker questions using Google’s Gemini API.
Originally designed for conferences, the app can be used in any setting where you want to spark conversation.

---

## 🚀 Features

* Generates a random, under-20-word icebreaker in seconds
* Context-aware prompts based on optional URL parameters:

  * `event`
  * `event_subject`
  * `audience`
  * `additional_notes`
* Simple web interface with one-click regeneration
* Customisable style via `style.css`

---

## ⚡ Quickstart

### 1. Get a Gemini API Key

* Sign up for [Google AI Studio](https://aistudio.google.com/)
* Create an API key and copy it somewhere safe

### 2. Clone this Repository

On macOS/Linux:

```bash
git clone https://github.com/yourusername/ai-icebreakers.git
cd ai-icebreakers
```

On Windows (PowerShell):

```powershell
git clone https://github.com/yourusername/ai-icebreakers.git
cd ai-icebreakers
```

### 3. Set up Environment Variable

On macOS/Linux:

```bash
export GEMINI_API_KEY="your_api_key_here"
```

On Windows (PowerShell):

```powershell
$env:GEMINI_API_KEY="your_api_key_here"
```

### 4. Install Requirements

```bash
pip install -r requirements.txt
```

### 5. Run the App

```bash
streamlit run app.py
```

Now open [http://localhost:8501](http://localhost:8501) in your browser to start generating icebreakers!

---

## 📂 Project Structure

```
.
├── app.py           # Main Streamlit app
├── style.css        # Custom styling
├── Logo2.png        # Example logo
└── requirements.txt # Python dependencies
```

---

## 🙏 Acknowledgements

A big thank you to:

* [Google DeepMind / Gemini](https://deepmind.google/) for providing the language models
* The open-source [Streamlit](https://streamlit.io/) community for making interactive apps simple
* Contributors and testers who helped refine this project

---

## 📜 Licence

This project is open-source and available under the [MIT Licence](LICENSE).
Feel free to fork, adapt, and share!
