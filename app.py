# 2023/04/04 VS Codeで書いたやつ

import streamlit as st
import openai

# Streamlit Cludの「Secrets」からOpenAI API keyを取得
openai.api_key = st.secrets.OpenAIAPI.openai_api_key

# st.session_stateを使いメッセージのやり取りを保存
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role":"system","content":"あなたは優秀なアシスタントAIです。"}
    ]

# チャットボットとやり取りする関数
def communicate():
    messages = st.session_state["messages"]

    user_message = {"role":"user","content":st.session_state["user_input"]}
    messages.append(user_message)

    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )

    bot_message = response["choices"][0]["message"]
    messages.append(bot_message)

    st.session_state["user_input"] = "" #入力欄を消去


# UIの構築
st.title("My AI Assitantだよ")
st.write("ChatGPT APIを使ったチャットボットでーす")

user_input = st.text_input("メッセージ入れて", key = "user_input", on_change = communicate)

if st.session_state["messages"]:
    messages = st.session_state["messages"]

    for message in reversed(messages[1:]):
        speaker = "☺️"
        if message["role"] == "assistant":
            speaker = "🤖"

        st.write(speaker + ":" + message["content"])

