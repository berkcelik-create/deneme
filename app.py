import streamlit as st
import json

# Veriyi yükle
def load_data():
    with open('settings.json', 'r', encoding='utf-8') as f:
        return json.load(f)

data = load_data()

st.set_page_config(page_title="Gaming Optimizer", page_icon="🎮")
st.title("🎮 Gaming Performance Optimizer")

# Seçim kutuları
cpu_list = list(data.keys())
selected_cpu = st.selectbox("İşlemcinizi seçin:", cpu_list)

gpu_list = list(data[selected_cpu].keys())
selected_gpu = st.selectbox("Ekran kartınızı seçin:", gpu_list)

# Sonuçları göster
if st.button("Optimize Et"):
    settings = data[selected_cpu][selected_gpu]
    
    st.success("Optimum ayarlar bulundu!")
    
    # Görselleştirme için sütunlar
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Texture", settings["texture"])
        st.metric("Shadows", settings["shadows"])
    with col2:
        st.metric("Reflex", settings["reflex"])
        st.metric("Vibrance", settings["digital_vibrance"])
    
    st.info("Bu ayarlar rekabetçi oyunlarda FPS kararlılığını artırmak için test edilmiştir.")
