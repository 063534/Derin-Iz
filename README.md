# 🕵️‍♂️ Derin-İz Ultra: Cyber Intelligence & OSINT Platform

**Derin-İz Ultra**, modern bir siber istihbarat ve tehdit analiz platformudur. Bu proje, siber güvenlik dünyasındaki dijital ayak izlerini takip etmek, veri sızıntılarını analiz etmek ve açık kaynak istihbaratı (OSINT) toplamak amacıyla geliştirilmiştir.

## 🚀 Özellikler / Features

* **🔍 OSINT & Whois Query**: Alan adlarının kayıt bilgilerini ve kuruluş detaylarını anlık olarak sorgular.
* **📍 IP Geolocation**: IP adreslerinin coğrafi konumlarını harita üzerinde görselleştirir.
* **📂 Static File Analyzer**: Yüklenen `.py` veya `.txt` dosyalarını tarayarak içindeki riskli kelimeleri (password, eval, secret vb.) tespit eder ve bir **Güvenlik Skoru** atar.
* **📈 Threat Analytics**: Siber sızıntı trendlerini interaktif grafiklerle sunar.
* **🔐 Crypto Tools**: Güçlü şifreler üretir ve bunları **SHA-256** algoritması ile maskeler.
* **📡 Live Monitoring**: Tor ağı simülasyonu ile siber forumlardaki sızıntıları (CEREBRO, GuardLog vb.) takip eder.

## 🛠️ Kullanılan Teknolojiler / Tech Stack

* **Language**: Python 3.13
* **Framework**: Streamlit (UI)
* **Visuals**: Plotly (Interactive Charts)
* **Libraries**: python-whois, requests, hashlib
* **Environment**: Developed on macOS (Apple Silicon M2)

## 🔧 Kurulum / Installation

Projeyi yerel makinenizde çalıştırmak için / To run the project locally:

1.  Repoyu klonlayın / Clone the repo:
    ```bash
    git clone https://github.com/063534/Derin-Iz.git
    ```
2.  Gerekli kütüphaneleri yükleyin / Install requirements:
    ```bash
    pip install -r requirements.txt
    ```
3.  Uygulamayı başlatın / Start the app:
    ```bash
    streamlit run istihbarat.py
    ```

---

