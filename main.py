import streamlit as st
import base64
from gtts import gTTS

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

add_bg_from_local('ccc.jpg')

st.title('Страны мира')

option = st.selectbox("О какой стране ты хочешь узнать?",
                 ("Россия", "США", "Япония", "Китай"))

if option == "Россия":
    st.header('Россия')
    Russia ="""
    Россия – самая большая страна мира, расположена в Северном полушарии,
    занимает большую часть Евразии.
    С запада на восток Россия протянулась
    на 10 тысяч километров,с севера на юг – около 4 тысяч.
    В стране 11 часовых поясов.
    Площадь — около 17 млн. км2.
    Столица — город Москва.
    Россия – одна из самых многонациональных стран мира — около 160 национальностей.
    Религия:  православие, ислам, буддизм, иудаизм и некоторые другие религии.
    Государственный язык: русский.
    Денежная единица — рубль."""

    st.text(Russia)

    if Russia:
        tts = gTTS(text=Russia, lang='ru')
        tts.save("good.mp3")

        audio_file = open('good.mp3', 'rb')
        audio_bytes = audio_file.read()

        st.audio(audio_bytes, format='audio/mp3')

if option == "США":
    st.header('США')
    USA = '''
    Одно из крупнейших и влиятельнейших государств современного мира.
    Оно находится в Северной Америке и является четвертым по территории
    после России, Канады и Китая.
    Площадь - 9,5 млн км²
    Столица - город Вашингтон
    Численность населения - 301 693 000 человек
    Государственный язык - английский
    Денежная единица - доллар'''

    st.text(USA)
    if USA:
        tts = gTTS(text=USA, lang='ru')
        tts.save("good.mp3")

        audio_file = open('good.mp3', 'rb')
        audio_bytes = audio_file.read()

        st.audio(audio_bytes, format='audio/mp3')

if option == "Япония":
    st.header('Япония')
    Japan = '''
    Япония – страна особенного очарования в Восточной Азии.
    Расположено в северо – восточной части Тихого океана.
    Япония островное государство, состоит примерно из 6800 островов,
    главные и самые большие из них – Хоккайдо, Хонсю, Сикоку и Кюсю.
    Столица - город Токио
    Численность населения - 125 440 000
    Государственный язык - японский
    Денежная едиица - иена'''
    st.text(Japan)

    if Japan:
        tts = gTTS(text=Japan, lang='ru')
        tts.save("good.mp3")

        audio_file = open('good.mp3', 'rb')
        audio_bytes = audio_file.read()

        st.audio(audio_bytes, format='audio/mp3')

if option == "Китай":
    st.header('Китай')
    China = '''
    Китай — государство, которое находится в Восточной Азии.
    Эта страна является соседом России и занимает по площади третье место в мире.
    Её площадь 9 миллионов квадратных километров.
    Китай — самая густонаселённая страна в мире.
    Здесь проживает более 1.4 миллиарда человек.
    Столица - Пекин
    Государственный язык - китайский
    Денежная единица - юань'''
    st.text(China)
    if China:
        tts = gTTS(text=China, lang='ru')
        tts.save("good.mp3")

        audio_file = open('good.mp3', 'rb')
        audio_bytes = audio_file.read()

        st.audio(audio_bytes, format='audio/mp3')

# hello