
## 🛡️ AI-Powered Insurance Policy Chatbot

This project is an AI-powered **Insurance Policy Assistant** chatbot built using **Streamlit** for the frontend and integrated with **Gemini** AI for conversational capabilities. The bot can provide answers to user queries regarding insurance plans, coverage, premiums, and claims, utilizing a knowledge base extracted from a PDF document.

## 📌 Problem Statement
Insurance companies provide various policies such as health, life, auto, and home insurance. Customers often have questions about these policies, including coverage, premiums, and claims. Providing timely, accurate information is crucial. This project aims to build an AI-powered chatbot to assist customers with such queries using natural language understanding and a document-based knowledge base.
## ⚙️ Features

- **Interactive Chatbot**: Engage with a chatbot powered by Gemini AI to answer queries about insurance policies.
- **LLM Integration**: gemini-1.5-flash is used for generating natural language responses.
- **Knowledge Base Integration**: The chatbot is integrated with a knowledge base extracted from a PDF document, ensuring it has the latest insurance-related data.
- **Modern Dark Theme**: The UI features a dark theme to provide a modern, user-friendly interface.
- **Human Agent Assistance**: If needed, users can request to be connected to a human agent for more detailed assistance.
- **Submit Button**: A sleek submit button to trigger the chatbot's response.

## ✅ Requirements

To run this project, make sure you have the following dependencies installed:

- Python 3.7+
- Streamlit
- Fitz (PyMuPDF)
- Gemini API client (for conversational AI)



## 📁 Files

- `app.py`: Main file to run the chatbot interface using Streamlit.
- `utils.py`: Contains helper functions like `ask_gemini` (to query Gemini AI) and `load_knowledge_base` (to load data from a PDF).
- `data.pdf`: PDF containing insurance policy details (place your own PDF here).

## 💡 Customization

- **Change Knowledge Base**: To change the insurance policies or data used by the chatbot, replace the `data.pdf` file with your own PDF containing the relevant information.
- **UI Customization**: You can tweak the UI by modifying the CSS in the `app.py` file, adjusting colors, fonts, and layout.

## 🚀 How to Run the Project
- Add insurance PDFs to the data/ folder.
- Launch the chatbot
   ```bash
   streamlit run app.py
   ```

## 📌 Conclusion
The chatbot efficiently handles insurance-related queries using LLM and a PDF-based knowledge base. It improves user experience by delivering clear, reliable information and routing complex queries to human agents when needed.

