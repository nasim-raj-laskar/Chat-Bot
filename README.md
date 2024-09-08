# Chatbot 

## Project Description

This project is a chatbot application built using Python and PyTorch. The chatbot uses machine learning to understand and respond to user inputs based on predefined intents. Here's an overview of its components and functionality:

### Components

1. **`intents.json`**:
   - **Purpose**: Stores the different types of user interactions or "intents" that the chatbot can recognize and respond to.
   - **Structure**: This JSON file contains various intents, each with a unique `tag`, a list of `patterns` (phrases or questions a user might ask), and corresponding `responses` (how the chatbot should reply).
   - **Usage**: Modify this file to customize the chatbot's behavior by adding new intents, updating existing ones, or removing those that are no longer needed.

2. **`nltk_util.py`**:
   - **Purpose**: Provides utility functions for preprocessing text data.
   - **Functions**:
     - `tokenize(sentence)`: Splits a sentence into individual words or tokens.
     - `stem(word)`: Reduces words to their root form to handle variations in word usage.
     - `bag_of_words(tokenized_sentence, all_words)`: Converts a sentence into a numerical format suitable for training the neural network, using the presence or absence of known words.

3. **`train.py`**:
   - **Purpose**: Contains the script to train the neural network model based on the intents and patterns defined in `intents.json`.
   - **Functionality**: 
     - Loads and preprocesses the data from `intents.json`.
     - Defines a custom dataset class (`ChatDataset`) for training.
     - Initializes and trains the neural network model (`NeuralNet` defined in `model.py`).
     - Saves the trained model and associated data for later use.

4. **`model.py`**:
   - **Purpose**: Defines the architecture of the neural network used by the chatbot.
   - **Architecture**: 
     - Includes two hidden layers with ReLU activation functions.
     - Outputs logits for each possible intent without a final activation function (since the loss function will handle the final classification).

5. **`chat.py`**:
   - **Purpose**: Handles user input and generates responses based on the trained model.
   - **Functionality**:
     - Takes user input, preprocesses it, and converts it into a format suitable for the model.
     - Passes the input through the model to get the predicted intent.
     - Selects and returns a response based on the predicted intent.

6. **`app.py`**:
   - **Purpose**: Provides a graphical user interface (GUI) for interacting with the chatbot.
   - **Functionality**:
     - Displays a chat window where users can type their messages and see responses from the chatbot.
     - Includes features such as a typing indicator to simulate real-time interaction.
     - Uses `tkinter` for the GUI and customizes the appearance of the chat window and message bubbles.

### Summary

This chatbot project combines natural language processing with a user-friendly interface to create an interactive application. It demonstrates how to use machine learning for text classification and how to integrate a trained model into a desktop application. Whether you're looking to understand chatbot development, natural language processing, or machine learning in practice, this project offers a comprehensive example.


## Installation

To set up the chatbot project on your local machine, follow these steps:

1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

2. **Create a Virtual Environment**
```bash
python -m venv env
```

3. **Activate the Virtual Environment**
• On Windows:
```bash
.\env\Scripts\activate
```

• On macOS/Linux:
```bash
source env/bin/activate
```

4. **Install Required Packages**
```bash
pip install -r requirements.txt
```

If `requirements.txt` is not included, you can manually install the required packages:
```bash
pip install nltk torch tkinter
```

5. **Download NLTK Data**
Run the following script to download necessary NLTK data:
```python
import nltk
nltk.download('punkt')
```

6. **Train the Model**
Run the `train.py` script to train the model:
```bash
python train.py
```

7. **Run the Chatbot GUI**
Start the chatbot GUI with:
```bash
python app.py
```

## Customizing Intents

The `intents.json` file defines the various user intents and responses used by the chatbot. You can modify this file to better suit your needs by following these guidelines:

• Adding New Intents: To add a new `intent`, create a new object in the intents list with a unique `tag`, a list of `patterns`, and corresponding `responses`. For example:

```json
{
  "tag": "new_intent",
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
• Modifying Existing Intents: Update the patterns or responses for existing intents as needed. Ensure that the `tag` remains consistent with your code.

• Removing Intents: If you want to remove an `intent`, delete the corresponding object from the intents list.

Remember to retrain the model (`train.py`) after making changes to the `intents.json` file to incorporate the updates into the chatbot's behavior.

## Usage
• Chat with the Bot: Type your message in the input field and press "Send" or hit Enter to interact with the chatbot.
• Train the Model: To retrain the model, modify the training data or parameters in `train.py` and re-run the script.

## Contributing
If you want to contribute to this project, please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

## Acknowledgements

• PyTorch: For the deep learning framework.

• NLTK: For natural language processing utilities.
   
