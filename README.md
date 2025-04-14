# 🤖 Chatbot

An interactive chatbot application built using **Python** and **PyTorch**, featuring natural language understanding, machine learning, and a sleek **Tkinter** GUI.

---

## 🚀 Project Overview

This project showcases a basic yet powerful chatbot that learns from predefined intents and responds intelligently to user input.

### 🛠️ Core Components

| File | Purpose |
|:---|:---|
| **`intents.json`** | Stores user intents, patterns (sample user messages), and corresponding responses. Easily customizable! |
| **`nltk_util.py`** | Provides text preprocessing utilities: `tokenize`, `stem`, and `bag_of_words`. |
| **`train.py`** | Trains the model based on `intents.json`, and saves the trained model data. |
| **`model.py`** | Defines a simple neural network architecture for intent classification. |
| **`chat.py`** | Handles user input, predicts the intent, and selects an appropriate response. |
| **`app.py`** | Provides a graphical user interface (GUI) using `tkinter` for real-time chatbot interaction. |

---

## 📦 Installation Guide

Get your chatbot running locally with these simple steps:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/nasim-raj-laskar/Chat-Bot.git
   cd Chat-Bot
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv env
   ```

3. **Activate the Virtual Environment**

   • On **Windows**:
   ```bash
   .\env\Scripts\activate
   ```

   • On **macOS/Linux**:
   ```bash
   source env/bin/activate
   ```

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   If `requirements.txt` is missing:
   ```bash
   pip install nltk torch tkinter
   ```

5. **Download NLTK Data**
   ```python
   import nltk
   nltk.download('punkt')
   ```

6. **Train the Model**
   ```bash
   python train.py
   ```

7. **Launch the Chatbot GUI**
   ```bash
   python app.py
   ```

---

## 🛠️ Customizing Your Chatbot

Want your bot to talk about new topics? Just edit the `intents.json` file!

### ➕ Add New Intents
```json
{
  "tag": "new_feature",
  "patterns": [
    "How do I use this feature?",
    "Tell me more about the new feature"
  ],
  "responses": [
    "Here's how you can use this feature...",
    "The new feature works by..."
  ]
}
```

### ✏️ Modify Existing Intents
- Add, remove, or update `patterns` and `responses` under any intent.
- **Note:** Keep the `tag` consistent.

### ➖ Remove Intents
- Simply delete the corresponding intent object from the list.

👉 **Don't forget to retrain the model** after making changes:
```bash
python train.py
```

---

## 💬 Usage

- **Chat**: Type your message in the input box and press **Send** or **Enter**.
- **Retrain**: Modify `intents.json` and re-run `train.py` anytime you need new behaviors.

---

## 🤝 Contributing

We welcome contributions!  
Fork the repository, make your improvements, and submit a **pull request**.

---

## 📄 License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for more information.

---

## 🙌 Acknowledgements

- [**PyTorch**](https://pytorch.org/) — Deep learning framework
- [**NLTK**](https://www.nltk.org/) — Natural Language Toolkit for text preprocessing

---
