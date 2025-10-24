import streamlit as st
import statistics

page_bg = """
    <style>
    .stApp {
    background-color: #333333;
    font-family: "Countimport streamlit as st
import statisticsier New", monospace;
    }
    h1{
    color: #ff2800;
    text-decoration: underline;
    font-family : "Courier New" , monospace;
    font-style: bold;
    }
    span, label {
    color: white,
    font-family: "Countier New", monospace;
    }
    blockquote, p.quote {
    font-family: "Countier New", monospace;
    font-style: italic;
    color: #fcc00;
    }
    div.stButton > button {
    backgroud-color:#333333;
    colour: white;
    border-radius: 10px;
    border: 1px solid #ff2800;
    }
    div[data-baseweb="slider"] > div > div {
    background: #ff2800 !important;
    }
    div[data-baseweb="slider"] > div > div > div {
    background: #ff2800 !important;
    }
    div[data-testid="stProgressBar"] > div > div {
    background-color: #ff2800 !important;
    }
    </style>
    """

st.markdown(page_bg, unsafe_allow_html=True)


st.title("Meinungsquiz zum Existenzialismus")
st.write("Jetzt kurz nach den Ferien kannst du hier wieder anfangen zu philosophieren.")

quotes = [
    {"t": "Der Mensch ist vollkommen frei.", "p": "Sartre"},
    {"t": "Wir sind unsere Entscheidungen.", "p": "Sartre"},
    {"t": "Die Freiheit besteht in erster Linie nicht aus Privilegien, sondern aus Pflichten.", "p": "Camus"},
    {"t": "Die Entdeckung, dass wir nichts zu verlieren haben, gibt uns unsere Freiheit.", "p": "Camus"},
    {"t": "Jeder gibt sich den Sinn des Lebens selber.", "p": "Sartre"},
    {"t": "Menschen tendieren dazu ihre Freiheit zum Teil zu leugnen um sich der damit folgenden Verantwortung für ihr Handeln zu entziehen.", "p": "Sartre"},
    {"t": "Wenn wir nicht mehr darauf vertrauen, dass alles sicher wird, eröffnet das neue Möglichkeiten, sich anzupassen und spontan zu handeln.", "p": "Camus"},
    {"t": "Der Mensch ist das einzige Lebewesen, dass sich weigert, das zu sein, was es ist.", "p": "Camus"},
    
]
if "stage" not in st.session_state:
    st.session_state.stage = 0
if "answers" not in st.session_state:
    st.session_state.answers = []


if st.session_state.stage < len(quotes):
    current = quotes[st.session_state.stage]
    st.write(f"**Frage {st.session_state.stage + 1} von {len(quotes)}**")
    st.write(f"„{current['t']}“")

    move = st.slider("Wie sehr stimmst du zu?", 0, 10, key=f"slider_{st.session_state.stage}")

    if st.button("Weiter"):
        st.session_state.answers.append({
            "p": current["p"],
            "score": move
        })
        st.session_state.stage += 1
        st.rerun()

elif st.session_state.stage < len(quotes):
    current = quotes[st.session_state.stage]
    st.write(f"**Frage {st.session_state.stage + 1} von {len(quotes)}**")
    st.write(f"{current['t']}")

    move = st.slider("Wie sehr stimmst du zu?", 0, 10, key=f"slider_{st.session_state.stage}")

    if st.button("Weiter"):
        st.session_state.answer.append({
            "p": current["p"],
            "score": move
        })
        st.session_state.stage += 1
        st.rerun()

elif st.session_state.stage < len(quotes):
    current = quotes[st.session_state.stage]
    st.write(f"**Frage {st.session_state.stage + 1} von {len(quotes)}")
    st.write(f"{current['t']}")

    move = st.slider("Wie sehr stimmst du zu?", 0, 10, key=f"slider_{st.session_state.stage}")

    if st.button("Weiter"):
        st.session_state.answer.append({
            "p": current["p"],
            "score": move
        })
        st.session_state.stage += 1
        st.rerun()

elif st.session_state.stage < len(quotes):
    current = quotes[st.session_state.stage]
    st.write(f"**Frage {st.session_state.stage + 1} von {len(quotes)}")
    st.write(f"{current['t']}")

    move = st.slider("Wie sehr stimmst du zu?", 0, 10, key=f"slider_{st.session_state.stage}")

    if st.button("Weiter"):
        st.session_state.answer.append({
            "p": current["p"],
            "score": move
        }) 
        st.session_state.stage += 1
        st.rerun()

elif st.session_state.stage < len(quotes):
    current = quotes[st.session_state.stage]
    st.write(f"**Frage {st.session_state.stage + 1} von {len(quotes)}")
    st.write(f"{current['t']}")

    move = st.slider("Wie sehr stimmst du zu?", 0, 10, key=f"slider_{st.session_state.stage}")

    if st.button("Weiter"):
        st.session_state.answer.append({
            "p": current["p"],
            "score": move
        })
        st.session_state.stage += 1
        st.rerun()

elif st.session_state.stage < len(quotes):
    current = quotes[st.session_state.stage]
    st.write(f"**Frage {st.session_state.stage + 1} von {len(quotes)}")
    st.write(f"{current['t']}")

    move = st.slider("Wie sehr stimmst du zu?", 0, 10, key=f"slider_{st.session_state.stage}")

    if st.button("Weiter"):
        st.session_state.answer.append({
            "p": current["p"],
            "score": move
        })
        st.session_state.stage += 1
        st.rerun()

elif st.session_state.stage < len(quotes):
    current = quotes[st.session_state.stage]
    st.write(f"**Frage {st.session_state.stage + 1} von {len(quotes)}")
    st.write(f"{current['t']}")

    move = st.slider("Wie sehr stimmst du zu?", 0, 10, key=f"slider_{st.session_state.stage}")

    if st.button("Weiter"):
        st.session_state.answer.append({
            "p": current["p"],
            "score": move
        })
        st.session_state.stage += 1
        st.rerun()

elif st.session_state.stage < len(quotes):
    current = quotes[st.session_state.stage]
    st.write(f"**Frage {st.session_state.stage + 1} von {len(quotes)}")
    st.write(f"{current['t']}")

    move = st.slider("Wie sehr stimmst du zu?", 0, 10, key=f"slider_{st.session_state.stage}")

    if st.button("Weiter"):
        st.session_state.answer.append({
            "p": current["p"],
            "score": move
        })
        st.session_state.stages
        st.rerun()

else:
    st.write("###🧭 Auswerung")

    sartre_scores = [a["score"] for a in st.session_state.answers if a["p"] == "Sartre"]
    camus_scores = [a["score"] for a  in st.session_state.answers if a["p"] == "Camus"]

    sartre_avg = statistics.mean(sartre_scores)
    camus_avg = statistics.mean(camus_scores)

    st.bar_chart({"Sartre": sartre_avg, "Camus": camus_avg})

    if sartre_avg > camus_avg:
        st.success("Nach deinen Antworten in diesen Quiz tendierst du eher zu Sartres Thesen und Ansichten.")
    elif camus_avg > sartre_avg:
        st.success("Nach deinen Antworten in diesem Quiz tendierst du eher zu den Thesen und Ansichten von Camus.")
    else:
        st.success("Du liegst nach deinen Antworten in diesem Quiz genau zwischen den Thesen von Sartre und Camus.")
