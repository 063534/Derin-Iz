import streamlit as st
import pandas as pd
import time
import whois
import plotly.express as px
import requests
import hashlib
import random
import string

st.set_page_config(page_title="Derin-İz Ultra", layout="wide", page_icon="🛡️")

st.title("🛡️ Derin-İz: Ultra Siber İstihbarat Platformu")
st.write("---")

# --- Yan Menü (Sidebar) ---
st.sidebar.success("Sistem: Ultra Mod Aktif ✅")

# 1. OSINT Bölümü
st.sidebar.header("🔍 OSINT & IP Takip")
ip_or_domain = st.sidebar.text_input("IP veya Domain girin:", "")
if st.sidebar.button("İzini Sür"):
    if ip_or_domain:
        # IP Geolocation Simülasyonu (Basit Harita İçin)
        st.sidebar.info(f"📍 {ip_or_domain} konumu hesaplanıyor...")
        # Harita verisi (Örnek koordinatlar: Ankara)
        map_data = pd.DataFrame({'lat': [39.93], 'lon': [32.85]})
        st.sidebar.map(map_data)
    else:
        st.sidebar.warning("Veri girilmedi.")

# --- Ana Sekmeler ---
tab1, tab2, tab3, tab4 = st.tabs(["📡 Tehdit Akışı", "📉 Analitik", "📂 Dosya Analizi", "🔐 Crypto Araçları"])

with tab1:
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("Canlı İstihbarat Operasyonu")
        if st.button("Taramayı Başlat"):
            with st.status("Sistemler Sorgulanıyor...", expanded=True) as s:
                st.write("🕵️ Veri sızıntıları taranıyor...")
                time.sleep(1)
                s.update(label="Tarama Tamamlandı!", state="complete")
            st.warning("⚠️ Kritik Sızıntı: CEREBRO kaynak kodları paylaşıldı!")

with tab2:
    st.subheader("Siber Tehdit Grafiği")
    chart_data = pd.DataFrame({"Gün": ["Pzt", "Sal", "Çar", "Per", "Cum"], "Sızıntı": [10, 25, 15, 45, 30]})
    fig = px.line(chart_data, x="Gün", y="Sızıntı", template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.subheader("📂 Statik Dosya Analizörü")
    uploaded_file = st.file_uploader("Analiz için bir dosya yükleyin (.py, .txt)", type=['py', 'txt'])
    if uploaded_file is not None:
        content = uploaded_file.read().decode("utf-8")
        danger_words = ["password", "eval", "exec", "admin", "secret", "token"]
        found = [word for word in danger_words if word in content.lower()]
        
        st.write("### Analiz Sonucu")
        score = 100 - (len(found) * 15)
        st.progress(max(score, 0))
        st.write(f"🛡️ Güvenlik Skoru: %{max(score, 0)}")
        if found:
            st.error(f"⚠️ Riskli kelimeler bulundu: {', '.join(found)}")
        else:
            st.success("✅ Dosya temiz görünüyor.")

with tab4:
    st.subheader("🔐 Crypto Tool & Şifre Oluşturucu")
    pass_len = st.slider("Şifre Uzunluğu", 8, 32, 16)
    if st.button("Güçlü Şifre Üret"):
        chars = string.ascii_letters + string.digits + string.punctuation
        new_pass = ''.join(random.choice(chars) for i in range(pass_len))
        st.code(new_pass, language="text")
        # SHA-256 Maskeleme
        hashed = hashlib.sha256(new_pass.encode()).hexdigest()
        st.write(f"**SHA-256 Hash:** `{hashed}`")
        # Mevcut tab tanımlamasına "📊 Genel Durum" ekle:
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Genel Durum", "📡 Tehdit Akışı", "📉 Analitik", "📂 Dosya Analizi", "🔐 Crypto Araçları"
])

with tab1:
    st.subheader("🌐 Siber Harekat Merkezi - Tek Bakışta Tüm Sistem")
    
    # Üst Panel: Metrikler
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("OSINT Durumu", "Aktif", "Güvenli")
    m2.metric("Sızıntı Trendi", "%42", "+5.2")
    m3.metric("Dosya Skoru", "%85", "-2")
    m4.metric("Aktif Oturum", "Tor_Node_Ankara", "Gizli")

    # Orta Panel: Harita ve Grafik Yan Yana
    c1, c2 = st.columns(2)
    with c1:
        st.write("📍 **Son Tehdit Konumu**")
        # Ankara koordinatlarını odak noktası yapalım
        map_data = pd.DataFrame({'lat': [39.93], 'lon': [32.85]})
        st.map(map_data, zoom=5)
    
    with c2:
        st.write("📈 **Siber Hareketlilik (Canlı)**")
        chart_data = pd.DataFrame({"Saat": ["09:00", "10:00", "11:00", "12:00"], "Saldırı": [5, 12, 28, 15]})
        fig = px.area(chart_data, x="Saat", y="Saldırı", template="plotly_dark")
        fig.update_traces(line_color='#00ff00') # Siber yeşil
        st.plotly_chart(fig, use_container_width=True)

    # Alt Panel: Son İşlemler Özeti
    st.write("---")
    st.write("📝 **Sistem Günlüğü (Log)**")
    log_data = {
        "İşlem": ["WHOIS Sorgusu", "SHA-256 Üretimi", "Dosya Taraması", "IP Takibi"],
        "Durum": ["Tamamlandı", "Başarılı", "Risk Bulundu", "Aktif"],
        "Zaman": ["11:02", "11:04", "11:05", "11:06"]
    }
    st.table(pd.DataFrame(log_data))