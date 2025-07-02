# Question Answering System using MDeBERTa

This is a robust Question Answering (QA) web application developed using **Hugging Face Transformers** and **Streamlit** as part of the **DevifyX NLP Job Assignment**. It allows users to input a context paragraph and ask natural language questions. The system extracts the most relevant answer span from the context using a powerful transformer model.

---

##  Model Used

* **Model**: `timpal0l/mdeberta-v3-base-squad2`
* **Framework**: Hugging Face Transformers
* **Accuracy**: Very high on SQuAD2.0
* **Justification**: MDeBERTa-v3 is one of the most accurate models for extractive QA and handles unanswerable questions well.

---

##  Features

### Core Features

*  Accepts paragraph (context) and question as input
*  Extracts the most relevant answer from the context
*  Confidence score displayed for the predicted answer
*  Error handling for empty inputs or irrelevant questions
*  Relevance check between question and context (keyword overlap)

### Bonus Features (Implemented)

*  Highlights extracted answer inside the context
*  Score-based answer reliability classification
*  Streamlit web-based UI for interactive use

---

##  How to Run the App Locally

### Step 1: Clone the repository

```bash
git clone https://github.com/your-username/qa-streamlit-app.git
cd qa-streamlit-app
```

### Step 2: Create and activate a virtual environment

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the app

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

---

##  Project Structure

```
qa-streamlit-app/
├── app.py                # Main Streamlit app
├── requirements.txt      # All Python dependencies
└── README.md             # This documentation
```

---

##  Dependencies

```
streamlit
transformers
torch
```

Install with:

```bash
pip install -r requirements.txt
```

---

##  Live Deployment

The app is deployed and accessible online:

🔗 **[Live App](https://question-answering-system-assignment.streamlit.app)**

Anyone can open the link, paste a paragraph, ask a question, and get an answer with confidence insights.

---

##  Assignment Requirements Checklist (DevifyX)

| Requirement                             | Implemented                     |
| --------------------------------------- | ------------------------------- |
| Accepts context and question            | ✅ Yes                           |
| Answer extraction via transformer model | ✅ Yes                           |
| Preprocessing (tokenization, etc.)      | ✅ Done by Hugging Face pipeline |
| Confidence scoring shown                | ✅ Yes                           |
| Handles empty/invalid input             | ✅ Yes                           |
| Documentation provided                  | ✅ This README                   |
| Streamlit UI                            | ✅ Yes                           |
| Bonus: Answer highlighting              | ✅ Yes                           |
| Bonus: Relevance keyword check          | ✅ Yes                           |

---

##  Limitations

* Supports only English (monolingual)
* One question at a time

```
zip qa-streamlit-app.zip app.py requirements.txt README.md
```
