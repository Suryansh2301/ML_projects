import streamlit as st
import pickle
import string
import nltk

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Download nltk resources
nltk.download('punkt')
nltk.download('stopwords')

ps = PorterStemmer()

# -------------------------------
# Text Preprocessing Function
# -------------------------------
def transform_text(text):
    text = text.lower()

    tokens = nltk.word_tokenize(text)

    y = []
    for i in tokens:
        if i.isalnum():
            y.append(i)

    tokens = y[:]
    y.clear()

    for i in tokens:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    tokens = y[:]
    y.clear()

    for i in tokens:
        y.append(ps.stem(i))

    return " ".join(y)

# -------------------------------
# Load Vectorizer and Model
# -------------------------------
tfidf = pickle.load(open('Vectorizer.pkl', 'rb'))
model = pickle.load(open('ExtraTreesClassifier.pkl', 'rb'))

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="Spam SMS Detector",
    page_icon="📩",
    layout="centered"
)

# -------------------------------
# Custom CSS
# -------------------------------
st.markdown("""
<style>
.main {
    padding-top: 1rem;
}
.title {
    text-align:center;
    color:#1E88E5;
}
.result-spam{
    padding:15px;
    border-radius:10px;
    background-color:#ffebee;
    color:#d32f2f;
    font-size:22px;
    text-align:center;
}
.result-ham{
    padding:15px;
    border-radius:10px;
    background-color:#e8f5e9;
    color:#2e7d32;
    font-size:22px;
    text-align:center;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# UI
# -------------------------------
st.markdown("<h1 class='title'>📩 Spam SMS Detection App</h1>", unsafe_allow_html=True)

st.write("Enter any SMS or Message below to check whether it is Spam or Not Spam.")

input_sms = st.text_area(
    "Enter Message",
    height=150,
    placeholder="Type your SMS here..."
)

if st.button("Detect Spam"):

    if input_sms.strip() == "":
        st.warning("Please enter a message.")
    else:

        # preprocessing
        transformed_sms = transform_text(input_sms)

        # vectorize
        vector_input = tfidf.transform([transformed_sms])

        # prediction
        result = model.predict(vector_input)[0]

        # probability
        try:
            probability = model.predict_proba(vector_input)
            confidence = max(probability[0]) * 100
        except:
            confidence = None

        if result == 1:
            st.markdown(
                "<div class='result-spam'>🚨 SPAM MESSAGE</div>",
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                "<div class='result-ham'>✅ NOT SPAM</div>",
                unsafe_allow_html=True
            )

        if confidence:
            st.write(f"**Confidence:** {confidence:.2f}%")

        st.write("### Processed Text")
        st.code(transformed_sms)

import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
# from streamlit import header

ps = PorterStemmer()
def transform_text(text):
    text = text.lower()
    text = word_tokenize(text)
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words("english") and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))
    return " ".join(y)

tfidf= pickle.load(open("Vectorizer.pkl", "rb"))
model = pickle.load(open("ExtraTreesClassifier.pkl", "rb"))
model_1 = pickle.load(open("MultinomialNB.pkl", "rb"))

st.title("Email/SMS Spam Classifier")

input_sms = st.text_area("Enter the messages")



if st.button("predict"):

    # 1. preprocess
    transform_sms =transform_text(input_sms)
    #2. vectorize
    vector_input  = tfidf.transform([transform_sms])
    #3. predict
    result = model.predict(vector_input)[0]
    # result_1 = model.predict(vector_input)[0]
    #4. Display
    if result == 1:
      st.header("Spam")
    else:
        st.header("Not Spam")

    # if result_1 == 1:
    #   st.header("Spam")
    # else:
    #     st.header("Not Spam")
