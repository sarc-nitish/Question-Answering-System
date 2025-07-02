# Question Answering System using MDeBERTa

This is a robust Question Answering (QA) web application developed using **Hugging Face Transformers** and **Streamlit** as part of the DevifyX NLP Job Assignment. It allows users to input a context paragraph and ask natural language questions. The system extracts the most relevant answer span from the context using a powerful transformer model.

---

## 🔬 Model Used

* **Model**: `timpal0l/mdeberta-v3-base-squad2`
* **Framework**: Hugging Face Transformers
* **Reason**: MDeBERTa-v3 is known for its high accuracy on QA tasks, especially on the SQuAD2.0 dataset.

---

## ⚖️ Features

### Core Features

* ✏️ Accepts paragraph (context) and question as input
* ✉️ Extracts the most relevant answer from the context
* 🔢 Confidence score displayed for the predicted answer
* ⚠️ Error handling for empty inputs or invalid questions
* 🔮 Relevance check between question and context (keyword overlap)

### Bonus Features

* 🔍 Highlights extracted answer inside the context
* 📊 Score-based warnings (e.g., low confidence)
* 🌐 Streamlit web interface

---

## 🚀 How to Run the App

### Step 1: Clone the repository (or download ZIP)

```bash
$ git clone https://github.com/your-repo/qa-streamlit-app.git
$ cd qa-streamlit-app
```

### Step 2: Create and activate a virtual environment (recommended)

```bash
# For Windows
$ python -m venv venv
$ venv\Scripts\activate

# For Linux/macOS
$ python3 -m venv venv
$ source venv/bin/activate
```

### Step 3: Install dependencies

```bash
$ pip install -r requirements.txt
```

### Step 4: Run the Streamlit app

```bash
$ streamlit run app.py
```

The app will open in your browser (usually at [http://localhost:8501](http://localhost:8501)).

---

## 📄 Project Structure

```
qa-streamlit-app/
├── app.py                # Main Streamlit app
├── requirements.txt      # All Python dependencies
└── README.md             # This documentation
```

---

## 🔧 Dependencies

Listed in `requirements.txt`:

```txt
streamlit
transformers
torch
```

To install:

```bash
pip install -r requirements.txt
```

---

## ✅ Evaluation Checklist (Assignment Criteria)

| Criteria                          | Status               |
| --------------------------------- | -------------------- |
| Context + Question Input          | ✅ Yes                |
| Answer Extraction via Transformer | ✅ Yes                |
| Preprocessing                     | ✅ Via pipeline       |
| Confidence Score Display          | ✅ Yes                |
| Error Handling                    | ✅ Yes                |
| Highlighting + Relevance Check    | ✅ Bonus Done         |
| Streamlit Web Interface           | ✅ Yes                |
| Documentation (README)            | ✅ You're reading it! |

---

## 🚫 Limitations

* Not multilingual (currently uses English-only model)
* Only one question at a time
* Not containerized (Docker not included)

---

## 🙏 Credits

* Developed by: \[Your Name]
* Using Hugging Face Transformers & Streamlit
* Assignment by: DevifyX NLP Job Assignment Team

---

## ✉ Submission Reminder

Zip this folder and submit via:
**[https://forms.gle/A2MBA9FTJsJerh1s5](https://forms.gle/A2MBA9FTJsJerh1s5)**

Good luck ✨ and thank you for reviewing this project!
