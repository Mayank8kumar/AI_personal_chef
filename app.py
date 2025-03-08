from flask import Flask, render_template, request, session, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from config import Config

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')

#### WTForms form 
class RecipeForm(FlaskForm):
    recipe_message = StringField('Ask your recipe', validators=[DataRequired()])
    submit = SubmitField('Ask')

### LangChain Function 
def Chef(recipe_message):
    openai_api_key = os.getenv('OPENAI_API_KEY')
    chat = ChatOpenAI(openai_api_key=openai_api_key)

    systemMessagePrompt = SystemMessagePromptTemplate.from_template(
        "You are Ramu Kaka. You are a master chef. First, introduce yourself as Ramu Kaka the chef. You can write any type of food recipe that can be cooked easily in 15-20 minutes. You are allowed to answer only food-related queries. If you don't know the answer, respond with 'Maafi Sahab mujhe nhi pta'."
    )

    humanMessagePrompt = HumanMessagePromptTemplate.from_template('{asked_recipe}')
    chatPrompt = ChatPromptTemplate.from_messages([systemMessagePrompt, humanMessagePrompt])

    formattedchatprompt = chatPrompt.format_messages(asked_recipe=recipe_message)
    response = chat.invoke(formattedchatprompt)
    
    return response.content

# Define Routes
@app.route("/", methods=["GET", "POST"])
def home():
    form = RecipeForm()
    response_ai_recipe = session.get('response_ai_recipe', '')

    if request.method == "POST" and form.validate_on_submit():
        recipe_message = form.recipe_message.data
        response_recipe = Chef(recipe_message)
        session['response_ai_recipe'] = response_recipe
        return redirect("/")

    return render_template("home.html", form=form, response_ai_recipe=response_ai_recipe)


############ Run Flask App ############
if __name__ == '__main__':
    app.run(debug=True)
