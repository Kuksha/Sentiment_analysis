import pandas as pd
import numpy as np
import streamlit as st
import pickle
import emoji
import random


@st.cache
def get_model():
    clf = pickle.load(open("model.pkl", "rb"))
    return clf


model = get_model()

text = st.text_area('Введите отзыв на телефон')
corpus = [text]

start_button = st.button("Показать результат")

bad_emoji = [':pensive:',  ':anguished:', ':hushed:']
good_emoji = [':grinning:', ':satisfied:', ':smile:']


if start_button:

    if corpus == '':
        st.write("Пожалуста, напишите свой отзыв")

    try: 

        res = model.predict(corpus)
        res = res[0]                                    # Распакуем класс отзыва
        num  = random.randint(0, 2)

        if res:
            st.write(emoji.emojize("Отзыв отрицательный {}:thumbsdown:".format(bad_emoji[num]), use_aliases = True))
        else:
            st.write(emoji.emojize("Отзыв положительный {}:thumbsup:".format(good_emoji[num]), use_aliases = True))


    except:
        st.write("Введён некорректный текст")



