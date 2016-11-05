# Sistem Informasi Geografis - Pertemuan 4
RESUME PEMBUATAN METHOD DAN CLASS RETRIEVE DATA GEOSPASIAL
<p align="center">
  <img src="../../img/3.jpg">
</p>

## Latar Belakang Masalah :
Retrieve Data Geospasial ialah Meretrieve Data Vektor.

Data shapefile.shp

operasi Retrieve data menggunakan library python yang bernama py.shp

Shapefile : ialah standart file

Vektor Geospasial dikeluarkan oleh ESI

jadi Shapefile dibagi menjadi 2 yaitu 

<p align="center">
  <img src="../../img/1-1.jpg">
</p>

Geometri
Data koordinat yang membentuk bangun datar/ruang diantaranya:

1. Point/titik [1]

2. Line/garis [3] Shape,type

3. Polygon [5]

Operasi Pengambilan Data

Library pyshp class shapefile

1. Buka/baca

2.
<p align="center">
  <img src="../../img/1-2.jpg">
</p>

Method dari DBF

fields

record(n)

Record (n) baris ke (n) records

Method dari SHP

shapes() - Menampilkan semua

shape(n) - Menampilkan dengan parameter

1. bbox

2. parts

3. point s 

4. shape type


bbox

boading box, merupakan batas view peta.

contohnya :

<p align="center">
  <img src="../../img/1-3.jpg">
</p>

Koordinat a,b,c,d itu di sebut bbox

parts

part ialah apakah record ini bagian dari record lain/ precahan relasi

points

koordinat pembentukan peta

shapetype

jenis geometri dari points

## Praktek : 

Menampilkan jumlah record melalui terminal

<p align="center">
  <img src="../../img/Screenshot from 2016-11-05 23-51-22.png.jpg">
</p>

Menampilkan jumlah record dengan py shp

<p align="center">
  <img src="../../img/Screenshot from 2016-11-05 23-52-29.png">
</p>

main.py

<p align="center">
  <img src="../../img/Screenshot from 2016-11-05 23-52-29.png">
</p>

1. Buatlah class geospasial editor,

<p align="center">
  <img src="../../img/Screenshot from 2016-11-06 01-40-33.png">
</p>

Masukan Kode didalam tugas.py

<p align="center">
  <img src="../../img/Screenshot from 2016-11-06 01-36-05.png">
</p>

2. Buat Method Select, Where Negara (Indonesia)?
Output Data Record Negara Indonesia

Lakukan pengujian

<p align="center">
  <img src="../../img/Screenshot from 2016-11-06 01-41-10.png">
</p>

## Penutup
**Kesimpulan**
jadi pada pertemuan 4 ini , kita dapat mengetahui bagaimana membuat class dan penggunaan method method yang terdapat pada retrieve datasulitnya memahami penggunaan method, kurang nya latihan praktek di kelas, diperbanyak praktek di dalam kelas nya

**Saran**
sulitnya memahami penggunaan method, kurang nya latihan praktek di kelas, diperbanyak praktek di dalam kelas nya