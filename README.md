# 🍽️ AI Personal Chef  
**An AI-powered recipe recommendation web application using OpenAI's LLM & Flask**  

AI Personal Chef is a smart web-based application that utilizes **OpenAI's Large Language Model (LLM)** to suggest personalized recipes based on user-inputted ingredients. The goal is to make cooking more efficient and enjoyable by providing AI-generated recipe ideas tailored to available ingredients.  

---

## 🚀 Features  

👉 **AI-Powered Recipe Suggestions** - Uses OpenAI's API to generate personalized recipe ideas.  
👉 **Ingredient-Based Filtering** - Users can input available ingredients to receive relevant recipes.  
👉 **User-Friendly Web Interface** - Built with **HTML5, CSS3, and Bootstrap** for a responsive and modern UI.  
👉 **Flask-Based Backend** - Lightweight and efficient Python backend for handling user requests.  
👉 **Dynamic & Interactive UI** - Enhances user experience with a smooth and intuitive design.  

---

## 🏗️ Tech Stack  

| Component       | Technology Used          |
|----------------|-------------------------|
| **Backend**    | Python 3.9+ with Flask  |
| **Frontend**   | HTML5, CSS3, Bootstrap  |
| **AI Model**   | OpenAI API (LLM-based)  |
| **Version Control** | Git & GitHub |
| **Environment Management** | Virtualenv for isolated dependencies |

---

## 🔧 Installation & Setup  

Follow these steps to set up the AI Personal Chef application on your local machine:  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/Mayank8kumar/AI_personal_chef.git
cd AI_personal_chef
```

### **2️⃣ Set Up the Virtual Environment**  

#### **For Windows**  
```bash
python -m venv venv
venv\Scripts\activate
```

#### **For Mac/Linux**  
```bash
python3 -m venv venv
source venv/bin/activate
```

### **3️⃣ Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **4️⃣ Set Up Environment Variables**  
Rename `.env.example` to `.env`  
Add your OpenAI API Key in the `.env` file:  
```ini
OPENAI_API_KEY=your_api_key_here
```

### **5️⃣ Run the Application**  
```bash
python app.py
```
Your application will be accessible at **http://127.0.0.1:5000/**  

---

## 📂 Project Structure  
```bash
AI_personal_chef/
│── static/               # CSS, images, and static assets  
│   └── css/styles.css    # Stylesheet  
│  
│── templates/            # HTML templates  
│   └── home.html         # Homepage  
│  
│── app.py                # Main Flask application  
│── config.py             # Configuration settings  
│── requirements.txt      # Python dependencies  
│── .gitignore            # Git ignore rules  
│── .env.example          # Environment variable template  
│── README.md             # Documentation (You are here)  
```

---

## 📌 Usage  

1️⃣ **Enter ingredients** you have in your kitchen.  
2️⃣ Click the **"Generate Recipe"** button.  
3️⃣ The AI will suggest a recipe using the OpenAI API.  
4️⃣ **Enjoy cooking** with AI-powered recommendations!  

---

## 🤝 Contributing  

Contributions are welcome! To contribute:  

1. **Fork the repository**  
2. **Create a new branch** (`feature-branch`)  
3. **Commit your changes** (`git commit -m "Added a new feature"`)  
4. **Push the changes** (`git push origin feature-branch`)  
5. **Open a Pull Request**  

---

## 📝 License  

This project is licensed under the **MIT License**. You are free to modify, distribute, and use it as per the license terms.  

---

## 🌟 Future Enhancements  

👉 Deploy the app on **Render / Vercel / Heroku**  
👉 Add **user authentication** for personalized recipe history  
👉 Implement **meal planning & dietary preference filters**  
👉 Improve UI with **TailwindCSS or React.js**  

---

## 👤 Author  

Developed by **Mayank Kumar**  
[GitHub Profile](https://github.com/Mayank8kumar)  


