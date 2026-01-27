# Laporan Praktikum Kriptografi
Minggu ke-: X  
Topik: [judul praktikum]  
Nama: [Nama Mahasiswa]  
NIM: [NIM Mahasiswa]  
Kelas: [Kelas]  

Perancangan Sistem E-Voting Berbasis Blockchain untuk Mendukung Pemilihan Presiden Mahasiswa oleh KPUM














Kelompok 5 : 
 
1.	Nafis Ramadhan K.J  	(230202769)
2.	Faiz Al Mubarok  	(230202748)
3.	Julian Aji Pratama   	(230202760)
4.	Fauzan Hidayat  	 (230202807)
5.	Iman Sunan Maknun	(230202758)


Dosen Pengampu :
Helmi Bahar Alim, S.Kom., M.Kom



PRODI ILMU KOMPUTER
FAKULTAS SAINS DAN TEKNOLOGI
UNIVERSITAS PUTRA BANGSA
2026
BAB I PENDAHULUAN

1.1	Latar Belakang
Pemilihan Presiden Mahasiswa merupakan salah satu proses demokrasi penting di lingkungan perguruan tinggi yang diselenggarakan oleh Komisi Pemilihan Umum Mahasiswa (KPUM). Proses ini bertujuan untuk memilih pemimpin mahasiswa yang akan mewakili aspirasi seluruh mahasiswa serta menjalankan roda organisasi kemahasiswaan. Namun, pada praktiknya, proses pemilihan Presiden Mahasiswa di banyak perguruan tinggi masih menggunakan metode tradisional, yaitu pemungutan suara berbasis kertas (paper-based voting). Metode pemilihan tradisional tersebut memiliki berbagai keterbatasan dan permasalahan. Di antaranya adalah tingginya biaya operasional untuk pencetakan surat suara, distribusi logistik, serta kebutuhan sumber daya manusia yang besar untuk proses penghitungan suara. Selain itu, proses penghitungan suara secara manual juga rentan terhadap kesalahan manusia (human error), membutuhkan waktu yang lama, dan berpotensi menimbulkan sengketa akibat kurangnya transparansi. Di sisi lain, metode pemungutan suara konvensional juga memiliki kelemahan dari aspek keamanan dan kepercayaan. Potensi terjadinya kecurangan, seperti pemungutan suara ganda, manipulasi hasil suara, maupun kehilangan surat suara, masih menjadi kekhawatiran dalam setiap pelaksanaan pemilihan. Hal ini dapat menurunkan tingkat kepercayaan mahasiswa terhadap hasil pemilihan yang diselenggarakan oleh KPUM.
Perkembangan teknologi informasi, khususnya teknologi blockchain, membuka peluang untuk mengatasi berbagai permasalahan tersebut. Blockchain merupakan teknologi buku besar terdistribusi (distributed ledger) yang bersifat transparan, tidak dapat diubah (immutable), dan aman secara kriptografis. Setiap transaksi yang tercatat di dalam blockchain akan tersimpan secara permanen dan dapat diverifikasi oleh semua pihak, sehingga sangat sesuai untuk diterapkan pada sistem pemungutan suara elektronik (e-voting). Dengan memanfaatkan teknologi blockchain dan kriptografi, sistem e-voting dapat memberikan jaminan keamanan, transparansi, dan integritas data suara. Setiap pemilih hanya dapat memberikan satu suara, dan hasil pemungutan suara tidak dapat dimanipulasi setelah tercatat di blockchain. Selain itu, proses penghitungan suara dapat dilakukan secara otomatis dan real-time, sehingga mempercepat proses rekapitulasi hasil pemilihan. Berdasarkan permasalahan dan peluang tersebut, proyek ini dikembangkan untuk membangun sistem e-voting berbasis blockchain yang bertujuan untuk memudahkan KPUM dalam menyelenggarakan pemilihan Presiden Mahasiswa secara lebih efisien, transparan, dan aman. Sistem ini diharapkan dapat menjadi solusi alternatif terhadap metode pemilihan konvensional serta meningkatkan kepercayaan mahasiswa terhadap proses dan hasil pemilihan.
1.2	Tujuan Projek
Proyek ini bertujuan untuk merancang dan mengimplementasikan sistem e-voting berbasis blockchain menggunakan kriptografi untuk meminimalkan kesalahan, menghindari kecurangan, dan memastikan hasil pemilihan yang transparan dan aman. Tujuan utamanya adalah:
1)	Membangun sistem e-voting yang efisien dan mudah digunakan untuk pemilihan Presiden Mahasiswa.
2)	Memastikan keamanan dan transparansi dalam setiap langkah pemilihan dengan menggunakan blockchain dan algoritma kriptografi.
3)	Mengurangi biaya dan waktu yang dibutuhkan dalam proses pemungutan suara dan penghitungan suara.


 
BAB II DESKRIPSI SISTEM

2.1 Gambaran Umum Sistem
Sistem E-Voting ini merupakan aplikasi berbasis web yang terintegrasi dengan teknologi blockchain Ethereum. Sistem memungkinkan mahasiswa untuk melakukan pemungutan suara secara digital menggunakan dompet kripto (MetaMask) sebagai identitas pemilih. Seluruh proses pemilihan, mulai dari pencatatan suara hingga perhitungan hasil, dilakukan secara on-chain melalui smart contract.
Sistem terdiri dari dua peran utama, yaitu:
•	Pemilih (Mahasiswa): memberikan suara menggunakan wallet Ethereum.
•	Admin (KPUM): memantau hasil pemilihan dan mengatur status pemilihan (dibuka atau ditutup).

2.2	Komponen Sistem

1.	Smart Contract Ethereum
•	Ditulis menggunakan bahasa Solidity.
•	Mengatur proses voting, pencatatan suara, dan validasi pemilih.

2.	Web Application
•	Dibangun menggunakan HTML, CSS, dan JavaScript.
•	Menggunakan library Ethers.js untuk komunikasi dengan blockchain.

3.	MetaMask
•	Digunakan sebagai wallet pengguna dan alat penandatanganan transaksi.

4.	Ethereum Testnet (Sepolia)
•	Digunakan sebagai jaringan blockchain untuk pengujian sistem tanpa biaya nyata.

2.3	Alur Kerja Sistem




 



















1.	Mulai
Proses dimulai ketika pengguna membuka sistem e-voting.
2.	Buka Aplikasi E-Voting
Pengguna mengakses aplikasi e-voting berbasis web yang sudah terhubung dengan blockchain.
3.	Cek Status Login (Sudah Login?) Jika belum login, pengguna diarahkan ke Halaman Login untuk melakukan autentikasi (misalnya menggunakan NIM).Jika sudah login, sistem melanjutkan ke proses berikutnya.
4.	Cek Ketersediaan MetaMask
Sistem memeriksa apakah browser pengguna sudah terpasang ekstensi MetaMask. Jika tidak tersedia, sistem menampilkan pesan error karena transaksi blockchain tidak bisa dilakukan. Jika tersedia, sistem melanjutkan ke proses koneksi wallet.
5.	Hubungkan Wallet (MetaMask)
Pengguna diminta menghubungkan wallet Ethereum melalui MetaMask sebagai identitas blockchain pemilih.
6.	Cek Status Voting (Sudah Pernah Vote?)
Sistem memeriksa status pemilih di smart contract: Jika sudah pernah vote, pengguna langsung diarahkan ke Halaman Terima Kasih. Jika belum pernah vote, pengguna dapat melanjutkan proses pemilihan.
7.	Tampilkan Daftar Paslon
Sistem menampilkan daftar pasangan calon (paslon) yang dapat dipilih oleh pemilih.
8.	Pilih Paslon
Pengguna memilih salah satu paslon sesuai dengan pilihannya.
9.	Konfirmasi Transaksi MetaMask
Setelah memilih paslon, MetaMask akan menampilkan pop-up konfirmasi transaksi blockchain yang harus disetujui oleh pengguna.
10.	Validasi Smart Contract
Smart contract melakukan validasi: Apakah voting masih dibuka Apakah pemilih belum pernah memilih Apakah ID paslon valid Jika validasi gagal, transaksi dibatalkan (Transaksi Gagal). Jika validasi berhasil, suara dicatat ke blockchain.
11.	Catat Suara ke Blockchain
Pilihan pemilih disimpan secara permanen di blockchain melalui smart contract.
12.	Konfirmasi Berhasil
Sistem menampilkan notifikasi bahwa voting berhasil dilakukan.
13.	Admin Monitoring Hasil
Admin (KPUM) dapat memantau hasil perolehan suara secara real-time melalui halaman admin yang membaca data langsung dari blockchain.
14.	Selesai
Proses voting selesai.

 
BAB III
ALGORITMA DAN PROTOKOL KRIPTOGRAFI
3.1	Kriptografi Kunci Publik
Sistem e-voting memanfaatkan kriptografi kunci publik (public key cryptography) melalui wallet Ethereum. Setiap pemilih memiliki:
•	Private Key: digunakan untuk menandatangani transaksi voting.
•	Public Key & Address: berfungsi sebagai identitas pemilih di blockchain.

3.2	Fungsi Hash
Fungsi hash digunakan untuk:
1)	Membentuk alamat wallet Ethereum.
2)	Menghasilkan transaction hash sebagai identitas unik transaksi voting.
3)	Menjaga integritas data pada blockchain.
Ethereum menggunakan algoritma Keccak-256, yang merupakan varian dari SHA-3.

3.3	Digital Signature
Setiap suara yang diberikan harus ditandatangani secara digital menggunakan algoritma ECDSA (Elliptic Curve Digital Signature Algorithm). Digital signature memastikan:
•	Autentikasi pemilih
•	Integritas data transaksi
•	Non-repudiation (pemilih tidak dapat menyangkal suara yang diberikan)
 
BAB IV
IMPLEMENTASI DAN PENGUJIAN SISTEM
4.1	Implementasi Sistem
•  Smart contract dikembangkan dan dideploy menggunakan Remix IDE.
•  Web aplikasi terhubung ke blockchain menggunakan Ethers.js.
•  MetaMask digunakan untuk konfirmasi dan penandatanganan transaksi voting.

4.2	Hasil Pengujian
Tampilan Login






Gambar 1. Login
Halaman login merupakan tahap awal akses ke sistem e-Voting yang berfungsi untuk memastikan bahwa hanya pemilih yang sah yang dapat mengikuti proses pemilihan. Pada tahap ini, pengguna diminta memasukkan Nomor Induk Mahasiswa (NIM) dan tanggal lahir sebagai data autentikasi. NIM digunakan sebagai identitas unik pemilih, sedangkan tanggal lahir berperan sebagai verifikasi tambahan. Setelah data dimasukkan dan dinyatakan valid, pengguna akan diarahkan ke halaman pemilihan. Apabila data tidak sesuai, sistem akan menolak akses. Dengan adanya halaman login, sistem e-Voting dapat membatasi akses hanya kepada pemilih yang berhak sebelum proses voting dicatat secara permanen pada blockchain, sehingga keamanan dan keabsahan pemilihan dapat terjaga.

 
	Tampilan Pemilihan








Gambar 2. Pemilihan
Gambar pertama menunjukkan halaman utama aplikasi KPUM E-Vote yang diakses oleh pemilih setelah berhasil login. Pada halaman ini, pengguna ditampilkan tiga kandidat pasangan calon (Paslon 01, Paslon 02, dan Paslon 03) lengkap dengan nama dan visi singkat masing-masing kandidat. Setiap kandidat memiliki tombol “Vote” yang dapat ditekan oleh pemilih. Sistem memastikan bahwa pemilih hanya dapat melakukan pemungutan suara satu kali dengan memanfaatkan validasi on-chain melalui smart contract blockchain. Tujuan halaman ini adalah memberikan antarmuka yang sederhana, intuitif, dan mudah dipahami oleh pemilih agar proses pemungutan suara dapat dilakukan dengan cepat dan minim kesalahan.

Tampilan Konfirmasi








Gambar 3. Konfirmasi

Gambar ini memperlihatkan pop-up MetaMask yang muncul ketika pemilih menekan tombol Vote. MetaMask berfungsi sebagai wallet kripto sekaligus jembatan antara aplikasi web dengan blockchain Ethereum (Sepolia Test Network) 

Tampilan Berhasil Memilih









Gambar 4. Berhasil
Gambar ini menunjukkan halaman konfirmasi sukses setelah transaksi voting berhasil dikonfirmasi di blockchain. Sistem menampilkan pesan:
•	“Terima kasih”
•	Informasi bahwa suara telah berhasil dicatat di blockchain
•	Pilihan paslon yang dipilih oleh pemilih
Selain itu, terdapat notifikasi dari MetaMask yang menandakan bahwa transaksi telah berhasil dan sudah mendapatkan konfirmasi di jaringan Sepolia, yang dapat dilihat lebih lanjut melalui Etherscan.
Halaman ini berfungsi sebagai bukti visual bagi pemilih bahwa suara mereka telah sah tercatat dan tidak perlu melakukan voting ulang.






Tampilan Admin







Gambar 5. Admin

Gambar terakhir memperlihatkan dashboard admin/panitia KPUM yang digunakan untuk memantau hasil pemilihan secara real-time.
Pada halaman ini ditampilkan:
•	Status pemilihan (OPEN)
•	Daftar pasangan calon beserta jumlah suara masing-masing
•	Peringkat kandidat berdasarkan perolehan suara
•	Waktu terakhir data diperbarui
•	Tombol Buka/Tutup Voting untuk mengatur status pemilihan
•	Tombol Reset Voting untuk keperluan pengujian sistem
Seluruh data suara yang ditampilkan diambil langsung dari blockchain menggunakan fungsi getVotes() pada smart contract, sehingga hasil yang ditampilkan bersifat transparan, real-time, dan tidak dapat dimanipulasi oleh pihak manapun.
 
BAB V ANALISIS KEAMANAN
5.1 Analisis Ancaman Keamanan
Sistem e-Voting berbasis blockchain yang dikembangkan memiliki beberapa mekanisme keamanan untuk menjamin keabsahan proses pemilihan serta keutuhan data suara. Analisis keamanan dilakukan terhadap aspek autentikasi, integritas data, pencegahan kecurangan, dan transparansi sistem.
1.	Autentikasi dan Identitas Pemilih
Autentikasi pemilih dilakukan melalui input Nomor Induk Mahasiswa (NIM) dan tanggal lahir pada aplikasi web. Selanjutnya, identitas pemilih diperkuat menggunakan alamat wallet blockchain (MetaMask) yang bersifat unik. Setiap alamat wallet merepresentasikan satu pemilih sehingga identitas tidak dapat dipalsukan secara mudah.

2.	Pencegahan Pemungutan Suara Ganda
Smart contract menerapkan mekanisme pencegahan voting ganda menggunakan struktur mapping(address => bool). Jika suatu alamat wallet telah tercatat melakukan voting, maka transaksi berikutnya dari alamat yang sama akan ditolak secara otomatis oleh smart contract. Mekanisme ini menjamin prinsip one person, one vote.

3.	Integritas dan Kemanan Data Suara
Setiap suara yang diberikan dicatat sebagai transaksi blockchain dan disimpan secara permanen. Data yang telah tercatat tidak dapat diubah atau dihapus karena sifat immutability pada blockchain. Hal ini memastikan bahwa hasil pemilihan tetap utuh dan tidak dapat dimanipulasi.

4.	Transparansi Sistem
Hasil pemilihan dapat diakses dan diverifikasi melalui fungsi pembacaan data pada smart contract serta melalui blockchain explorer. Transparansi ini memungkinkan proses audit hasil pemilihan secara terbuka tanpa mengungkap identitas pribadi pemilih.

5.	Kontrol Akses Admin
Fungsi administratif seperti membuka dan menutup voting dibatasi menggunakan mekanisme kontrol akses (onlyAdmin). Dengan demikian, hanya admin yang berwenang yang dapat mengubah status pemilihan

6.	Keterbatasan Keamanan
Keamanan sistem masih bergantung pada keamanan wallet pengguna. Apabila private key wallet bocor, maka terdapat potensi penyalahgunaan hak suara. Selain itu, autentikasi NIM dilakukan di sisi aplikasi sehingga masih memerlukan pengamanan tambahan pada level aplikasi.


 
BAB VI KESIMPULAN
6.1	Kesimpulan
Berdasarkan hasil perancangan, implementasi, dan pengujian yang telah dilakukan, dapat disimpulkan bahwa sistem e-Voting berbasis blockchain berhasil dibangun dan dijalankan sesuai dengan tujuan yang diharapkan. Sistem ini mampu menggantikan metode pemilihan konvensional dengan mekanisme digital yang lebih efisien, transparan, dan aman. Pemanfaatan teknologi blockchain dan smart contract memungkinkan pencatatan suara dilakukan secara permanen dan tidak dapat diubah, sehingga integritas hasil pemilihan dapat terjaga. Selain itu, mekanisme pencegahan voting ganda yang diterapkan pada smart contract memastikan bahwa setiap pemilih hanya dapat memberikan satu suara. Dengan adanya dashboard admin yang terhubung langsung ke blockchain, panitia KPUM dapat memantau hasil pemilihan secara real-time. Secara keseluruhan, sistem ini menunjukkan bahwa integrasi kriptografi dan blockchain dapat diterapkan secara efektif dalam sistem pemilihan presiden mahasiswa.

6.2	Saran
Untuk pengembangan selanjutnya, sistem e-Voting ini masih dapat ditingkatkan dari berbagai aspek. Autentikasi pemilih dapat diperkuat dengan mekanisme kriptografi tambahan, seperti tanda tangan digital atau verifikasi berbasis multi-faktor, agar keamanan identitas pemilih semakin terjamin. Selain itu, sistem dapat dikembangkan dengan fitur enkripsi data identitas pemilih serta integrasi database terpusat yang lebih aman untuk pengelolaan data akademik. Penggunaan jaringan blockchain yang lebih stabil atau penerapan solusi layer-2 juga dapat dipertimbangkan untuk meningkatkan efisiensi dan mengurangi biaya transaksi. Dengan pengembangan lebih lanjut, sistem e-Voting berbasis blockchain ini diharapkan dapat digunakan dalam skala yang lebih besar dan menjadi alternatif yang andal dalam penyelenggaraan pemilihan di lingkungan kampus.
 
LAMPIRAN
1.	File Slide Presentasi
https://www.canva.com/design/DAG_geiGqME/XKsquCnnZ4amunMJEiuJHg/edit?utm_content=DAG_geiGqME&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
2.	Link Presentasi
https://youtu.be/vLDyL8qyr9c?si=uFotw_PRIFG15oE3
3.	Manual Book
1)	Kebutuhan Sistem
•	Browser (Chrome / Edge)
•	Ekstensi MetaMask
•	Akun wallet Ethereum (jaringan Sepolia)
•	Koneksi internet
2)	Panduan Memilih
a)	Buka halaman login.
b)	Masukkan NIM dan tanggal lahir.
c)	Login ke sistem.
d)	Hubungkan wallet MetaMask.
e)	Pilih pasangan calon dan klik Vote.
f)	Konfirmasi transaksi di MetaMask.
g)	Sistem menampilkan notifikasi bahwa suara berhasil dicatat.
Setiap wallet hanya dapat melakukan voting satu kali.
3)  Panduan Penggunaan Admin

a)	Buka halaman admin.
b)	Hubungkan wallet admin.
c)	Lihat hasil voting yang diambil langsung dari blockchain.
d)	Admin dapat membuka atau menutup periode voting.

4)	Penanganan Masalah
•	MetaMask tidak terdeteksi: pastikan ekstensi aktif.
•	Transaksi gagal: periksa saldo ETH dan jaringan.
•	Voting ulang ditolak: wallet sudah tercatat melakukan voting.

4.	Link Repositori Github
https://github.com/narawho/kpumvote-blockchain.git

5.	Sumbangsih dan Pembagian Peran Anggota Tim
Nama	Jobdesk
Nafis Ramadhan Khoeru Jati	Membuat Program Sistem
Membuat Laporan
Membuat PPT
Faiz Al Mubarok	Membantu Manual Book
Julian Aji Pratama	Membantu Buat PPT
Fauzan Hidayat	Membantu Buat PPT
Iman Sunan Maknun	Membantu Buat PPT
