import streamlit as st
import fun_g3

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Глава 3", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Развернуть боковую панель
)

# Текст по центру страницы
st.header("👩🏻‍💻Листинги главы 3")

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=300)

with cont_1:
    # Раскрывающийся список
    options = st.selectbox("Листинги главы 3",
        ("Листинг 3.1", "Листинг 3.2", "Листинг 3.3", "Листинг 3.4", "Листинг 3.5",
         "Листинг 3.6", "Листинг 3.7", "Листинг 3.8", "Листинг 3.9", "Листинг 3.10",
         "Листинг 3.11", "Листинг 3.12", "Листинг 3.13", "Листинг 3.14", "Листинг 3.15",
         "Листинг 3.16", "Листинг 3.17", "Листинг 3.18", "Листинг 3.19", "Листинг 3.20",
         "Листинг 3.21", "Листинг 3.22", "Листинг 3.23", "Листинг 3.24", "Листинг 3.25",
         "Листинг 3.26", "Листинг 3.27", "Листинг 3.28", "Листинг 3.29", "Листинг 3.30",
         "Листинг 3.31", "Листинг 3.32", "Листинг 3.33", "Листинг 3.34", "Листинг 3.35",
         "Листинг 3.36", "Листинг 3.37", "Листинг 3.38", "Листинг 3.39", "Листинг 3.40",
         "Листинг 3.41", "Листинг 3.42", "Листинг 3.43", "Листинг 3.44", "Листинг 3.45",
         "Листинг 3.46", "Листинг 3.47", "Листинг 3.48",
         ),
        index=None,
        placeholder="Выберите листинг..."
    )

# Контейнер
cont_2 = st.container(width=800)
with cont_2:
    st.page_link('https://pythonlib.ru/sandbox', label='🛠️ Редактор код ✍🏻')
    if options is None:
        st.write('Листинг не выбран')
        st.image("Python_Book.jpg", width=350)
    elif options == "Листинг 3.1":
        path = 'pages/glava_3/Listing_3_1.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_1()
    elif options == "Листинг 3.2":
        path = 'pages/glava_3/Listing_3_2.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_2()
    elif options == "Листинг 3.3":
        path = 'pages/glava_3/Listing_3_3.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_3()
    elif options == "Листинг 3.4":
        path = 'pages/glava_3/Listing_3_4.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_4()
    elif options == "Листинг 3.5":
        path = 'pages/glava_3/Listing_3_5.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_5()
    elif options == "Листинг 3.6":
        path = 'pages/glava_3/Listing_3_6.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_6()
    elif options == "Листинг 3.7":
        path = 'pages/glava_3/Listing_3_7.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_7()
    elif options == "Листинг 3.8":
        path = 'pages/glava_3/Listing_3_8.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_8()
    elif options == "Листинг 3.9":
        path = 'pages/glava_3/Listing_3_9.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_9()
    elif options == "Листинг 3.10":
        path = 'pages/glava_3/Listing_3_10.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_10()
    elif options == "Листинг 3.11":
        path = 'pages/glava_3/Listing_3_11.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_11()
    elif options == "Листинг 3.12":
        path = 'pages/glava_3/Listing_3_12.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_12()
    elif options == "Листинг 3.13":
        path = 'pages/glava_3/Listing_3_13.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_13()
    elif options == "Листинг 3.14":
        path = 'pages/glava_3/Listing_3_14.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_14()
    elif options == "Листинг 3.15":
        path = 'pages/glava_3/Listing_3_15.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_15()
    elif options == "Листинг 3.16":
        path = 'pages/glava_3/Listing_3_16.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_16()
    elif options == "Листинг 3.17":
        path = 'pages/glava_3/Listing_3_17.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_17()
    elif options == "Листинг 3.18":
        path = 'pages/glava_3/Listing_3_18.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_18()
    elif options == "Листинг 3.19":
        path = 'pages/glava_3/Listing_3_19.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_19()
    elif options == "Листинг 3.20":
        path = 'pages/glava_3/Listing_3_20.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_20()
    elif options == "Листинг 3.21":
        path = 'pages/glava_3/Listing_3_21.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_21()
    elif options == "Листинг 3.22":
        path = 'pages/glava_3/Listing_3_22.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_22()
    elif options == "Листинг 3.23":
        path = 'pages/glava_3/Listing_3_23.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_23()
    elif options == "Листинг 3.24":
        path = 'pages/glava_3/Listing_3_24.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_24()
    elif options == "Листинг 3.25":
        path = 'pages/glava_3/Listing_3_25.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_25()
    elif options == "Листинг 3.26":
        path = 'pages/glava_3/Listing_3_26.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_26()
    elif options == "Листинг 3.27":
        path = 'pages/glava_3/Listing_3_27.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_27()
    elif options == "Листинг 3.28":
        path = 'pages/glava_3/Listing_3_28.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_28()
    elif options == "Листинг 3.29":
        path = 'pages/glava_3/Listing_3_29.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_29()
    elif options == "Листинг 3.30":
        path = 'pages/glava_3/Listing_3_30.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_30()
    elif options == "Листинг 3.31":
        path = 'pages/glava_3/Listing_3_31.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_31()
    elif options == "Листинг 3.32":
        path = 'pages/glava_3/Listing_3_32.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_32()
    elif options == "Листинг 3.33":
        path = 'pages/glava_3/Listing_3_33.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_33()
    elif options == "Листинг 3.34":
        path = 'pages/glava_3/Listing_3_34.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_34()
    elif options == "Листинг 3.35":
        path = 'pages/glava_3/Listing_3_35.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_35()
    elif options == "Листинг 3.36":
        path = 'pages/glava_3/Listing_3_36.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_36()
    elif options == "Листинг 3.37":
        path = 'pages/glava_3/Listing_3_37.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_37()
    elif options == "Листинг 3.38":
        path = 'pages/glava_3/Listing_3_38.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_38()
    elif options == "Листинг 3.39":
        path = 'pages/glava_3/Listing_3_39.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_39()
    elif options == "Листинг 3.40":
        path = 'pages/glava_3/Listing_3_40.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_40()
    elif options == "Листинг 3.41":
        path = 'pages/glava_3/Listing_3_41.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_41()
    elif options == "Листинг 3.42":
        path = 'pages/glava_3/Listing_3_42.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_42()
    elif options == "Листинг 3.43":
        path = 'pages/glava_3/Listing_3_43.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_43()
    elif options == "Листинг 3.44":
        path = 'pages/glava_3/Listing_3_44.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_44()
    elif options == "Листинг 3.45":
        path = 'pages/glava_3/Listing_3_45.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_45()
    elif options == "Листинг 3.46":
        path = 'pages/glava_3/Listing_3_46.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_46()
    elif options == "Листинг 3.47":
        path = 'pages/glava_3/Listing_3_47.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_47()
    elif options == "Листинг 3.48":
        path = 'pages/glava_3/Listing_3_48.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g3.run_3_48()