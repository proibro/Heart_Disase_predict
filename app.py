import streamlit as st
import pickle
import numpy as np

# Загружаем модель
with open('heart_disease_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("💓 Прогноз сердечных заболеваний")

# Ввод данных пользователем
age = st.number_input("Возраст", 1, 120, 30)
sex = st.selectbox("Пол", ("Мужской", "Женский"))
cp = st.selectbox("Тип боли в груди (0-3)", [0, 1, 2, 3])
trestbps = st.number_input("Давление в покое", 80, 200, 120)
chol = st.number_input("Холестерин", 100, 600, 200)
fbs = st.selectbox("Сахар > 120 мг/дл", [0, 1])
restecg = st.selectbox("Результат ЭКГ (0-2)", [0, 1, 2])
thalach = st.number_input("Макс. частота сердечных сокращений", 60, 250, 150)
exang = st.selectbox("Ишемия при нагрузке", [0, 1])
oldpeak = st.number_input("Снижение ST", 0.0, 6.0, 1.0)
slope = st.selectbox("Наклон ST (0-2)", [0, 1, 2])
ca = st.selectbox("Количество сосудов (0-3)", [0, 1, 2, 3])
thal = st.selectbox("Thal (1-3)", [1, 2, 3])

# Формируем входные данные
sex = 1 if sex == "Мужской" else 0
features = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                      thalach, exang, oldpeak, slope, ca, thal]])

# Предсказание
if st.button("Предсказать"):
    pred = model.predict(features)[0]
    if pred == 1:
        st.error("⚠️ Вероятность болезни сердца! : больше 50%")
    else:
        st.success("✅ Всё хорошо, низкий риск! : меньше 50%")
