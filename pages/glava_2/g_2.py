# https://python-code-online.pages.dev/ru/
import streamlit as st
import fun_g2

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Глава 2", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="auto",  # Развернуть боковую панель
)

# Текст по центру страницы
st.header("👩🏻‍💻Листинги главы 2")

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=300)

# Контейнер
with cont_1:
    # Раскрывающийся список
    options = st.selectbox("Листинги главы 2",
        ("Листинг 2.1", "Листинг 2.2", "Листинг 2.3", "Листинг 2.4",
         "Листинг 2.5", "Листинг 2.6", "Листинг 2.7", "Листинг 2.8",
         "Листинг 2.9", "Листинг 2.10", "Листинг 2.11", "Листинг 2.12",
         "Листинг 2.13", "Листинг 2.14", "Листинг 2.15", "Листинг 2.16",
         "Листинг 2.17", "Листинг 2.18", "Листинг 2.19", "Листинг 2.20",
         "Листинг 2.21", "Листинг 2.22", "Листинг 2.23", "Листинг 2.24",
         "Листинг 2.25", "Листинг 2.26", "Листинг 2.27", "Листинг 2.28",
         "Листинг 2.29", "Листинг 2.30", "Листинг 2.31", "Листинг 2.32",
         "Листинг 2.33", "Листинг 2.34", "Листинг 2.35", "Листинг 2.36",
         "Листинг 2.37", "Листинг 2.38", "Листинг 2.39", "Листинг 2.40",
         "Листинг 2.41", "Листинг 2.42", "Листинг 2.43", "Листинг 2.44",
         "Листинг 2.45", "Листинг 2.46", "Листинг 2.47", "Листинг 2.48",
         "Листинг 2.49", "Листинг 2.50", "Листинг 2.51", "Листинг 2.52",
         "Листинг 2.53", "Листинг 2.54", "Листинг 2.55", "Листинг 2.56",
         "Листинг 2.57", "Листинг 2.58", "Листинг 2.59", "Листинг 2.60",
         "Листинг 2.61", "Листинг 2.62", "Листинг 2.63", "Листинг 2.64", "Листинг 2.65",
         "Листинг 2.66", "Листинг 2.67", "Листинг 2.68", "Листинг 2.69", "Листинг 2.70",
         "Листинг 2.71", "Листинг 2.72", "Листинг 2.73", "Листинг 2.74", "Листинг 2.75",
         "Листинг 2.76", "Листинг 2.77", "Листинг 2.78", "Листинг 2.79", "Листинг 2.80",
         "Листинг 2.81", "Листинг 2.82", "Листинг 2.83", "Листинг 2.84", "Листинг 2.85",
         "Листинг 2.86", "Листинг 2.87", "Листинг 2.88", "Листинг 2.89", "Листинг 2.90",
         "Листинг 2.91", "Листинг 2.92", "Листинг 2.93", "Листинг 2.94", "Листинг 2.95",
         "Листинг 2.96", "Листинг 2.97", "Листинг 2.98", "Листинг 2.99", "Листинг 2.100",
         "Листинг 2.101", "Листинг 2.102", "Листинг 2.103", "Листинг 2.104", "Листинг 2.105",
         "Листинг 2.106", "Листинг 2.107", "Листинг 2.108", "Листинг 2.109", "Листинг 2.110",
         "Листинг 2.111", "Листинг 2.112", "Листинг 2.113", "Листинг 2.114", "Листинг 2.115",
         "Листинг 2.116", "Листинг 2.117", "Листинг 2.118", "Листинг 2.119", "Листинг 2.120",
         "Листинг 2.121", "Листинг 2.122", "Листинг 2.123", "Листинг 2.124"
         ),
        index=None,
        placeholder="Выберите листинг..."
    )

# Контейнер
cont_2 = st.container(width=800)
with cont_2:
    if options == "Листинг 2.33":
        st.page_link('https://nextleap.app/online-compiler/python-programming', label='🛠️ Редактор код ✍🏻')
        # st.page_link('https://www.online-ide.com/online_python_editor', label='🛠️ Редактор код ✍🏻')
    else:
        st.page_link('https://pythonlib.ru/sandbox', label='🛠️ Редактор код ✍🏻')

    if options is None:
        st.write('Листинг не выбран')
        st.image("Python_Book.jpg", width=350)
    elif options == "Листинг 2.1":
        path = 'pages/glava_2/Listing_2_1.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g2.run_2_1()
    elif options == "Листинг 2.2":
        path = 'pages/glava_2/Listing_2_2.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        st.divider()  # Разделитель
        with st.expander("🔍 Показать результат"):
            fun_g2.run_2_2()
    elif options == "Листинг 2.3":
        st.write('Код листинга 2.3')
        path = 'pages/glava_2/Listing_2_3.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g2.run_2_3()
    elif options == "Листинг 2.4":
        path = 'pages/glava_2/Listing_2_4.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g2.run_2_4()
    elif options == "Листинг 2.5":
        path = 'pages/glava_2/Listing_2_5.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g2.run_2_5()
    elif options == "Листинг 2.6":
        path = 'pages/glava_2/Listing_2_6.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g2.run_2_6()
    elif options == "Листинг 2.7":
        path = 'pages/glava_2/Listing_2_7.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g2.run_2_7()
    elif options == "Листинг 2.8":
        path = 'pages/glava_2/Listing_2_8.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g2.run_2_8()
    elif options == "Листинг 2.9":
        path = 'pages/glava_2/Listing_2_9.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g2.run_2_9()
    elif options == "Листинг 2.10":
        path = 'pages/glava_2/Listing_2_10.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g2.run_2_10()
    elif options == "Листинг 2.11":
        path = 'pages/glava_2/Listing_2_11.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g2.run_2_11()
    elif options == "Листинг 2.12":
        path = 'pages/glava_2/Listing_2_12.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g2.run_2_12()
    elif options == "Листинг 2.13":
        path = 'pages/glava_2/Listing_2_13.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g2.run_2_13()
    elif options == "Листинг 2.14":
        path = 'pages/glava_2/Listing_2_14.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("Показать результат"):
            fun_g2.run_2_14()
    elif options == "Листинг 2.15":
        path = 'pages/glava_2/Listing_2_15.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g2.run_2_15()
    elif options == "Листинг 2.16":
        path = 'pages/glava_2/Listing_2_16.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g2.run_2_16()
    elif options == "Листинг 2.17":
        path = 'pages/glava_2/Listing_2_17.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g2.run_2_17()
    elif options == "Листинг 2.18":
        path = 'pages/glava_2/Listing_2_18.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g2.run_2_18()
    elif options == "Листинг 2.19":
        path = 'pages/glava_2/Listing_2_19.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g2.run_2_19()
    elif options == "Листинг 2.20":
        path = 'pages/glava_2/Listing_2_20.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g2.run_2_20()
    elif options == "Листинг 2.21":
        path = 'pages/glava_2/Listing_2_21.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g2.run_2_21()
    elif options == "Листинг 2.22":
        path = 'pages/glava_2/Listing_2_22.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g2.run_2_22()
    elif options == "Листинг 2.23":
        path = 'pages/glava_2/Listing_2_23.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g2.run_2_23()
    elif options == "Листинг 2.24":
        path = 'pages/glava_2/Listing_2_24.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g2.run_2_24()
    elif options == "Листинг 2.25":
        path = 'pages/glava_2/Listing_2_25.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g2.run_2_25()
    elif options == "Листинг 2.26":
        path = 'pages/glava_2/Listing_2_26.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g2.run_2_26()
    elif options == "Листинг 2.27":
        path = 'pages/glava_2/Listing_2_27.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g2.run_2_27()
    elif options == "Листинг 2.28":
        path = 'pages/glava_2/Listing_2_28.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g2.run_2_28()
    elif options == "Листинг 2.29":
        path = 'pages/glava_2/Listing_2_29.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g2.run_2_29()
    elif options == "Листинг 2.30":
        path = 'pages/glava_2/Listing_2_30.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g2.run_2_30()
    elif options == "Листинг 2.31":
        path = 'pages/glava_2/Listing_2_31.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g2.run_2_31()
    elif options == "Листинг 2.32":
        path = 'pages/glava_2/Listing_2_32.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g2.run_2_32()
    elif options == "Листинг 2.33":
        path = 'pages/glava_2/Listing_2_33.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g2.run_2_33()
    elif options == "Листинг 2.34":
        path = 'pages/glava_2/Listing_2_34.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g2.run_2_34()
    elif options == "Листинг 2.35":
        path = 'pages/glava_2/Listing_2_35.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g2.run_2_35()
    elif options == "Листинг 2.36":
        path = 'pages/glava_2/Listing_2_36.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g2.run_2_36()
    elif options == "Листинг 2.37":
        path = 'pages/glava_2/Listing_2_37.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍 Показать результат"):
            fun_g2.run_2_37()
    elif options == "Листинг 2.38":
        path = 'pages/glava_2/Listing_2_38.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_38()
    elif options == "Листинг 2.39":
        path = 'pages/glava_2/Listing_2_39.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_39()
    elif options == "Листинг 2.40":
        path = 'pages/glava_2/Listing_2_40.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_40()
    elif options == "Листинг 2.41":
        path = 'pages/glava_2/Listing_2_41.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_41()
    elif options == "Листинг 2.42":
        path = 'pages/glava_2/Listing_2_42.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_42()
    elif options == "Листинг 2.43":
        path = 'pages/glava_2/Listing_2_43.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_43()
    elif options == "Листинг 2.44":
        path = 'pages/glava_2/Listing_2_44.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_44()
    elif options == "Листинг 2.45":
        path = 'pages/glava_2/Listing_2_45.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_45()
    elif options == "Листинг 2.46":
        path = 'pages/glava_2/Listing_2_46.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_46()
    elif options == "Листинг 2.47":
        path = 'pages/glava_2/Listing_2_47.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_47()
    elif options == "Листинг 2.48":
        path = 'pages/glava_2/Listing_2_48.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_48()
    elif options == "Листинг 2.49":
        path = 'pages/glava_2/Listing_2_49.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_49()
    elif options == "Листинг 2.50":
        path = 'pages/glava_2/Listing_2_50.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_50()
    elif options == "Листинг 2.51":
        path = 'pages/glava_2/Listing_2_51.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_51()
    elif options == "Листинг 2.52":
        path = 'pages/glava_2/Listing_2_52.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_52()
    elif options == "Листинг 2.53":
        path = 'pages/glava_2/Listing_2_53.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_53()
    elif options == "Листинг 2.54":
        path = 'pages/glava_2/Listing_2_54.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_54()
    elif options == "Листинг 2.55":
        path = 'pages/glava_2/Listing_2_55.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_55()
    elif options == "Листинг 2.56":
        path = 'pages/glava_2/Listing_2_56.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_56()
    elif options == "Листинг 2.57":
        path = 'pages/glava_2/Listing_2_57.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_57()
    elif options == "Листинг 2.58":
        path = 'pages/glava_2/Listing_2_58.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_58()
    elif options == "Листинг 2.59":
        path = 'pages/glava_2/Listing_2_59.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_59()
    elif options == "Листинг 2.60":
        path = 'pages/glava_2/Listing_2_60.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_60()
    elif options == "Листинг 2.61":
        path = 'pages/glava_2/Listing_2_61.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_61()
    elif options == "Листинг 2.62":
        path = 'pages/glava_2/Listing_2_62.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_62()
    elif options == "Листинг 2.63":
        path = 'pages/glava_2/Listing_2_63.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_63()
    elif options == "Листинг 2.64":
        path = 'pages/glava_2/Listing_2_64.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_64()
    elif options == "Листинг 2.65":
        path = 'pages/glava_2/Listing_2_65.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_65()
    elif options == "Листинг 2.66":
        path = 'pages/glava_2/Listing_2_66.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_66()
    elif options == "Листинг 2.67":
        path = 'pages/glava_2/Listing_2_67.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_67()
    elif options == "Листинг 2.68":
        path = 'pages/glava_2/Listing_2_68.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_68()
    elif options == "Листинг 2.69":
        path = 'pages/glava_2/Listing_2_69.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_69()
    elif options == "Листинг 2.70":
        path = 'pages/glava_2/Listing_2_70.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_70()
    elif options == "Листинг 2.71":
        path = 'pages/glava_2/Listing_2_71.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_71()
    elif options == "Листинг 2.72":
        path = 'pages/glava_2/Listing_2_72.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_72()
    elif options == "Листинг 2.73":
        path = 'pages/glava_2/Listing_2_73.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_73()
    elif options == "Листинг 2.74":
        path = 'pages/glava_2/Listing_2_74.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_74()
    elif options == "Листинг 2.75":
        path = 'pages/glava_2/Listing_2_75.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_75()
    elif options == "Листинг 2.76":
        path = 'pages/glava_2/Listing_2_76.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_76()
    elif options == "Листинг 2.77":
        path = 'pages/glava_2/Listing_2_77.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_77()
    elif options == "Листинг 2.78":
        path = 'pages/glava_2/Listing_2_78.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_78()
    elif options == "Листинг 2.79":
        path = 'pages/glava_2/Listing_2_79.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_79()
    elif options == "Листинг 2.80":
        path = 'pages/glava_2/Listing_2_80.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_80()
    elif options == "Листинг 2.81":
        path = 'pages/glava_2/Listing_2_81.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_81()
    elif options == "Листинг 2.82":
        path = 'pages/glava_2/Listing_2_82.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_82()
    elif options == "Листинг 2.83":
        path = 'pages/glava_2/Listing_2_83.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_83()
    elif options == "Листинг 2.84":
        path = 'pages/glava_2/Listing_2_84.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_84()
    elif options == "Листинг 2.85":
        path = 'pages/glava_2/Listing_2_85.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_85()
    elif options == "Листинг 2.86":
        path = 'pages/glava_2/Listing_2_86.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_86()
    elif options == "Листинг 2.87":
        path = 'pages/glava_2/Listing_2_87.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_87()
    elif options == "Листинг 2.88":
        path = 'pages/glava_2/Listing_2_88.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_88()
    elif options == "Листинг 2.89":
        path = 'pages/glava_2/Listing_2_89.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_89()
    elif options == "Листинг 2.90":
        path = 'pages/glava_2/Listing_2_90.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_90()
    elif options == "Листинг 2.91":
        path = 'pages/glava_2/Listing_2_91.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_91()
    elif options == "Листинг 2.92":
        path = 'pages/glava_2/Listing_2_92.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_92()
    elif options == "Листинг 2.93":
        path = 'pages/glava_2/Listing_2_93.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_93()
    elif options == "Листинг 2.94":
        path = 'pages/glava_2/Listing_2_94.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_94()
    elif options == "Листинг 2.95":
        path = 'pages/glava_2/Listing_2_95.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_95()
    elif options == "Листинг 2.96":
        path = 'pages/glava_2/Listing_2_96.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_96()
    elif options == "Листинг 2.97":
        path = 'pages/glava_2/Listing_2_97.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_97()
    elif options == "Листинг 2.98":
        path = 'pages/glava_2/Listing_2_98.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_98()
    elif options == "Листинг 2.99":
        path = 'pages/glava_2/Listing_2_99.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_99()
    elif options == "Листинг 2.100":
        path = 'pages/glava_2/Listing_2_100.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_100()
    elif options == "Листинг 2.101":
        path = 'pages/glava_2/Listing_2_101.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_101()
    elif options == "Листинг 2.102":
        path = 'pages/glava_2/Listing_2_102.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_102()
    elif options == "Листинг 2.103":
        path = 'pages/glava_2/Listing_2_103.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_103()
    elif options == "Листинг 2.104":
        path = 'pages/glava_2/Listing_2_104.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_104()
    elif options == "Листинг 2.105":
        path = 'pages/glava_2/Listing_2_105.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_105()
    elif options == "Листинг 2.106":
        path = 'pages/glava_2/Listing_2_106.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_106()
    elif options == "Листинг 2.107":
        path = 'pages/glava_2/Listing_2_107.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_107()
    elif options == "Листинг 2.108":
        path = 'pages/glava_2/Listing_2_108.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_108()
    elif options == "Листинг 2.109":
        path = 'pages/glava_2/Listing_2_109.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_109()
    elif options == "Листинг 2.110":
        path = 'pages/glava_2/Listing_2_110.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_110()
    elif options == "Листинг 2.111":
        path = 'pages/glava_2/Listing_2_111.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_111()
    elif options == "Листинг 2.112":
        path = 'pages/glava_2/Listing_2_112.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_112()
    elif options == "Листинг 2.113":
        path = 'pages/glava_2/Listing_2_113.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_113()
    elif options == "Листинг 2.114":
        path = 'pages/glava_2/Listing_2_114.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_114()
    elif options == "Листинг 2.115":
        path = 'pages/glava_2/Listing_2_115.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_115()
    elif options == "Листинг 2.116":
        path = 'pages/glava_2/Listing_2_116.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_116()
    elif options == "Листинг 2.117":
        path = 'pages/glava_2/Listing_2_117.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_117()
    elif options == "Листинг 2.118":
        path = 'pages/glava_2/Listing_2_118.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_118()
    elif options == "Листинг 2.119":
        path = 'pages/glava_2/Listing_2_119.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_119()
    elif options == "Листинг 2.120":
        path = 'pages/glava_2/Listing_2_120.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_120()
    elif options == "Листинг 2.121":
        path = 'pages/glava_2/Listing_2_121.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_121()
    elif options == "Листинг 2.122":
        path = 'pages/glava_2/Listing_2_122.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_122()
    elif options == "Листинг 2.123":
        path = 'pages/glava_2/Listing_2_123.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_123()
    elif options == "Листинг 2.124":
        path = 'pages/glava_2/Listing_2_124.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        with st.expander("🔍Показать результат"):
            fun_g2.run_2_124()
