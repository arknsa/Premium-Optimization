# Premium Optimization

Membuka Potensi Keadilan dan Profitabilitas dalam Penetapan Premi Asuransi Berbasis Data

## Gambaran Umum
Premium Optimization adalah proyek berbasis data yang dirancang untuk merevolusi cara perusahaan asuransi menentukan premi optimal bagi setiap pelanggan. Dengan memanfaatkan analitik lanjutan dan machine learning, proyek ini bertujuan menyeimbangkan risiko, kepuasan pelanggan, dan profitabilitas perusahaan—sehingga setiap premi menjadi adil sekaligus kompetitif.

## Motivasi Bisnis
Dalam industri asuransi, penetapan premi yang tepat adalah seni sekaligus sains. Premi terlalu rendah berisiko merugikan perusahaan, sementara premi terlalu tinggi membuat pelanggan beralih ke kompetitor. Proyek ini membantu perusahaan untuk:
- Memersonalisasi premi berdasarkan profil pelanggan yang komprehensif
- Meminimalkan risiko adverse selection dan churn
- Memaksimalkan retensi dan profitabilitas

## Sorotan Dataset
- **Baris:** 150.000
- **Kolom:** 30
- **Sumber:** Data sintetis yang merepresentasikan perjalanan pelanggan asuransi di dunia nyata
- **Fitur Utama:**
  - Demografi: Usia, Jenis Kelamin, Pekerjaan, Tingkat Pendapatan, Tingkat Pendidikan
  - Detail Polis: Tanggal Mulai/Perpanjangan Polis, Nilai Pertanggungan, Deductible, Tipe Polis
  - Risiko & Klaim: Riwayat Klaim, Profil Risiko, Skor Kredit, Catatan Mengemudi
  - Perilaku: Riwayat Pembelian, Preferensi Pelanggan, Interaksi dengan Customer Service
  - Fitur Turunan: Customer Tenure (durasi menjadi nasabah)

## Tujuan Proyek
- **Memprediksi jumlah premi optimal** untuk setiap pelanggan menggunakan data historis dan perilaku
- **Mengidentifikasi faktor utama** yang memengaruhi penetapan premi
- **Memberikan insight bisnis** yang actionable bagi pengambil keputusan

## Struktur Folder
```
├── Insurance Data.xlsx        # Dataset utama
├── tes.ipynb                 # Notebook analisis & pemodelan utama
├── requirements.txt          # Dependensi proyek
├── About Dataset.docx        # Dokumentasi dataset
```

## Cara Memulai
1. Clone repository ini
2. Install dependensi:
   ```bash
   pip install -r requirements.txt
   ```
3. Buka `tes.ipynb` dan ikuti pipeline analisis

## Insight Utama
- **Customer tenure dan riwayat klaim** adalah prediktor kuat risiko dan kecocokan premi
- **Segmentasi perilaku dan demografi** memungkinkan penetapan harga yang lebih akurat dan personal
- **Optimasi premi berbasis data** dapat meningkatkan retensi pelanggan dan margin perusahaan secara signifikan

## Dependensi
- polars
- pandas
- matplotlib
- seaborn
- openpyxl
- fastexcel

## Catatan
- Seluruh data telah dianonimkan dan bersifat sintetis untuk keperluan akademik
- Untuk eksplorasi lebih lanjut atau implementasi bisnis, pertimbangkan integrasi dengan data real-time dan pengecekan kepatuhan regulasi
