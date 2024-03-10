# Import Library
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_resource
def load_data():
    data = pd.read_csv("day.csv")
    return data


data = load_data()


# ==============================
# TITLE DASHBOARD
# ==============================
# Set page title
st.title("Bike Share Dashboard")

# ==============================
# SIDEBAR
# ==============================
st.sidebar.title("Information:")
st.sidebar.markdown("**• Nama: Syafri Winartanto**")
st.sidebar.markdown(
    "**• Email: [syafriwo@gmail.com](syafriwo@gmail.com)**")
st.sidebar.markdown(
    "**• Dicoding: [syafri_winartanto](https://www.dicoding.com/users/syafri_winartanto/)**")
st.sidebar.markdown(
    "**• Github: [Syafriwntrn](https://github.com/Syafriwntrn  )**")


st.sidebar.title("Dataset Bike Share")
# Show the dataset
if st.sidebar.checkbox("Show Dataset"):
    st.subheader("Raw Data")
    st.write(data)

# Display summary statistics
if st.sidebar.checkbox("Show Summary Statistics"):
    st.subheader("Summary Statistics")
    st.write(data.describe())



# ==============================
# VISUALIZATION
# ==============================

# Visualisasi histogram jumlah penyewa sepeda
st.subheader("Histogram Jumlah Penyewa Sepeda (cnt) dalam Day Dataset")
plt.figure(figsize=(10, 6))
sns.histplot(data['cnt'], bins=30, kde=True)
plt.title('Histogram Jumlah Penyewa Sepeda (cnt) dalam Day Dataset')
plt.xlabel('Jumlah Penyewa')
plt.ylabel('Frekuensi')
fig_hist = plt.gcf()  # Menyimpan objek gambar (figure)
st.pyplot(fig_hist)

# Scatter plot jumlah penyewa sepeda vs suhu
st.subheader("Scatter Plot Jumlah Penyewa Sepeda (cnt) vs Suhu (temp) dalam Day Dataset")
plt.figure(figsize=(10, 6))
sns.scatterplot(x='temp', y='cnt', data=data)
plt.title('Scatter Plot Jumlah Penyewa Sepeda (cnt) vs Suhu (temp) dalam Hour Dataset')
plt.xlabel('Suhu (Celsius)')
plt.ylabel('Jumlah Penyewa')
fig_hist = plt.gcf()  
st.pyplot(fig_hist)

# Box plot jumlah penyewa sepeda berdasarkan hari kerja dan hari libur
st.subheader("Perbedaan Pola Penggunaan Sepeda antara Hari Kerja dan Hari Libur dalam Hour Dataset")
plt.figure(figsize=(10, 6))
sns.boxplot(x='workingday', y='cnt', data=data)
plt.title('Perbedaan Pola Penggunaan Sepeda antara Hari Kerja dan Hari Libur dalam Hour Dataset')
plt.xlabel('Hari Kerja (0: Tidak, 1: Ya)')
plt.ylabel('Jumlah Penyewa')
fig_hist = plt.gcf()  
st.pyplot(fig_hist)

# Line plot tren penggunaan sepeda dari tahun ke tahun
st.subheader("Tren Penggunaan Sepeda dari Tahun ke Tahun dalam Day Dataset")
data['dteday'] = pd.to_datetime(data['dteday'])
data['year'] = data['dteday'].dt.year
yearly_cnt = data.groupby('year')['cnt'].sum()
plt.figure(figsize=(10, 6))
yearly_cnt.plot(marker='o')
plt.title('Tren Penggunaan Sepeda dari Tahun ke Tahun dalam Day Dataset')
plt.xlabel('Tahun')
plt.ylabel('Jumlah Penyewa')
plt.xticks(yearly_cnt.index)
plt.grid(True)
fig_hist = plt.gcf()  
st.pyplot(fig_hist)

# Rata-rata jumlah penyewa sepeda berdasarkan kondisi cuaca
st.subheader("Rata-rata Jumlah Penyewa Sepeda Berdasarkan Kondisi Cuaca")
weather_group = data.groupby('weathersit')
average_cnt_by_weather = weather_group['cnt'].mean()
plt.figure(figsize=(10, 6))
plt.bar(average_cnt_by_weather.index, average_cnt_by_weather.values, color='skyblue')
plt.xlabel('Kondisi Cuaca')
plt.ylabel('Rata-rata Jumlah Penyewa Sepeda')
plt.title('Rata-rata Jumlah Penyewa Sepeda Berdasarkan Kondisi Cuaca')
plt.xticks(rotation=45)
fig_hist = plt.gcf()  
st.pyplot(fig_hist)

# Show data source and description
st.sidebar.title("About")
st.sidebar.info("Dashboard ini menampilkan visualisasi untuk sekumpulan data Bike Share. ")
