import streamlit as st
import fun_g4

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Глава 4", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Развернуть боковую панель
)

# Текст по центру страницы
st.header("👩🏻‍💻Листинги главы 4")

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=300)

with cont_1:
    # Раскрывающийся список
    options = st.selectbox("Листинги главы 4",
        ("Листинг 4.1", "Листинг 4.2", "Листинг 4.3", "Листинг 4.4", "Листинг 4.5",
         "Листинг 4.6", "Листинг 4.7", "Листинг 4.8", "Листинг 4.9", "Листинг 4.10",
         "Листинг 4.11", "Листинг 4.12", "Листинг 4.13", "Листинг 4.14", "Листинг 4.15",
         "Листинг 4.16", "Листинг 4.17", "Листинг 4.18", "Листинг 4.19", "Листинг 4.20",
         "Листинг 4.21", "Листинг 4.22", "Листинг 4.23", "Листинг 4.24", "Листинг 4.25",
         "Листинг 4.26", "Листинг 4.27"),
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
    elif options == "Листинг 4.1":
        path = 'pages/glava_4/Listing_4_1.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g4.run_4_1()
    elif options == "Листинг 4.2":
        path = 'pages/glava_4/Listing_4_2.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g4.run_4_2()
    elif options == "Листинг 4.3":
        path = 'pages/glava_4/Listing_4_3.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g4.run_4_3()
    elif options == "Листинг 4.4":
        path = 'pages/glava_4/Listing_4_4.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g4.run_4_4()
    elif options == "Листинг 4.5":
        path = 'pages/glava_4/Listing_4_5.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g4.run_4_5()
    elif options == "Листинг 4.6":
        path = 'pages/glava_4/Listing_4_6.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g4.run_4_6()
    elif options == "Листинг 4.7":
        path = 'pages/glava_4/Listing_4_7.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g4.run_4_7()
    elif options == "Листинг 4.8":
        path = 'pages/glava_4/Listing_4_8.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g4.run_4_8()
    elif options == "Листинг 4.9":
        path = 'pages/glava_4/Listing_4_9.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g4.run_4_9()
    elif options == "Листинг 4.10":
        path = 'pages/glava_4/Listing_4_10.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g4.run_4_10()
    elif options == "Листинг 4.11":
        path = 'pages/glava_4/Listing_4_11.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g4.run_4_11()
    elif options == "Листинг 4.12":
        path = 'pages/glava_4/Listing_4_12.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g4.run_4_12()
    elif options == "Листинг 4.13":
        path = 'pages/glava_4/Listing_4_13.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g4.run_4_13()
    elif options == "Листинг 4.14":
        path = 'pages/glava_4/Listing_4_14.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g4.run_4_14()
    elif options == "Листинг 4.15":
        path = 'pages/glava_4/Listing_4_15.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g4.run_4_15()
    elif options == "Листинг 4.16":
        path = 'pages/glava_4/Listing_4_16.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g4.run_4_16()
    elif options == "Листинг 4.17":
        path = 'pages/glava_4/Listing_4_17.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g4.run_4_17()
    elif options == "Листинг 4.18":
        path = 'pages/glava_4/Listing_4_18.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g4.run_4_18()
    elif options == "Листинг 4.19":
        path = 'pages/glava_4/Listing_4_19.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g4.run_4_19()
    elif options == "Листинг 4.20":
        path = 'pages/glava_4/Listing_4_20.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g4.run_4_20()
    elif options == "Листинг 4.21":
        path = 'pages/glava_4/Listing_4_21.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g4.run_4_21()
    elif options == "Листинг 4.22":
        path = 'pages/glava_4/Listing_4_22.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g4.run_4_22()
    elif options == "Листинг 4.23":
        path = 'pages/glava_4/Listing_4_23.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g4.run_4_23()
    elif options == "Листинг 4.24":
        path = 'pages/glava_4/Listing_4_24.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g4.run_4_24()
    elif options == "Листинг 4.25":
        path = 'pages/glava_4/Listing_4_25.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g4.run_4_25()
    elif options == "Листинг 4.26":
        path = 'pages/glava_4/Listing_4_26.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g4.run_4_26()
    elif options == "Листинг 4.27":
        path = 'pages/glava_4/Listing_4_27.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g4.run_4_27()
