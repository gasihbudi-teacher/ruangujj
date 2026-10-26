#!/usr/bin/env python3
"""Reviewed editorial layer over extracted primary-source questions."""
import json
from pathlib import Path
root=Path(__file__).resolve().parent.parent
source=json.loads((root/'data/source_extracted.json').read_text(encoding='utf8'))
passage_id={
'passage-1': '''Dahulu kala, di sebuah hutan luas dekat sungai, hiduplah seekor gajah yang sangat besar dan kuat. Setiap pagi, gajah itu berjalan mengelilingi hutan untuk mencari dedaunan segar dan rumput sebagai makanan. Walaupun tubuhnya sangat besar, ia biasanya tenang dan ramah.

Suatu hari, ketika gajah berjalan di dekat pohon tinggi, ia mendengar seekor burung kecil bernyanyi nyaring. Burung itu bertengger di sebuah dahan sambil menikmati hangatnya sinar matahari.

Gajah mendongak dan berkata, “Mengapa kamu bernyanyi begitu keras? Suaramu sangat kecil.”

Burung kecil itu menjawab, “Aku mungkin kecil, tetapi aku suka bernyanyi. Nyanyianku membuatku bahagia.”

Gajah tertawa. “Kamu terlalu kecil untuk melakukan sesuatu yang penting,” katanya. Burung itu merasa sedih, tetapi ia tidak membantahnya.

Beberapa hari kemudian, badai dahsyat melanda hutan. Hujan deras turun dan angin bertiup menerpa pepohonan. Gajah sedang berjalan di dekat sungai ketika tiba-tiba ia terjebak dalam lumpur yang kental. Ia mencoba menarik kakinya keluar, tetapi lumpurnya terlalu dalam.

Gajah berjuang cukup lama. Ia berteriak meminta bantuan, tetapi tidak ada hewan lain yang datang. Ia kelelahan dan khawatir karena permukaan air sungai terus naik.

Burung kecil mendengar teriakan keras gajah. Ia segera terbang mengelilingi hutan dan memanggil hewan-hewan lain. “Gajah terjebak di dekat sungai! Kita harus menolongnya!”

Hewan-hewan itu berkumpul. Sebagian mendorong gajah dari belakang, sementara yang lain menarik dahan-dahan dari lumpur. Burung kecil terbang di atas mereka dan menunjukkan kepada semua hewan cara yang paling aman untuk membantu.

Setelah beberapa waktu, akhirnya gajah berhasil keluar dari lumpur. Ia menatap burung kecil dengan heran dan berkata, “Terima kasih. Aku salah menilaimu. Walaupun kamu kecil, kamu telah menolongku saat aku membutuhkannya.”

Burung kecil tersenyum dan berkata, “Setiap orang punya sesuatu yang bermanfaat untuk diberikan, tidak peduli seberapa besar atau kecil dirinya.” Sejak hari itu, gajah tidak pernah lagi menertawakan hewan-hewan kecil. Ia belajar bahwa ukuran tubuh seseorang tidak menentukan seberapa berharga bantuannya.''',
'passage-2': '''Belajar secara efektif bukan hanya soal menghabiskan berjam-jam bersama buku. Kamu juga perlu mempersiapkan sesi belajar dengan saksama agar dapat memahami dan mengingat materi dengan lebih baik.

1. Pilih tempat yang sesuai
Carilah tempat belajar yang tenang, bersih, dan nyaman. Pastikan tempat itu cukup terang dan bebas dari gangguan seperti televisi atau notifikasi yang tidak perlu.

2. Siapkan perlengkapanmu
Kumpulkan semua buku, catatan, alat tulis, dan bahan lain yang kamu perlukan sebelum mulai belajar. Ini akan menghemat waktu dan mencegah sesi belajarmu terputus.

3. Tetapkan tujuan yang jelas
Tentukan hal yang ingin kamu capai selama sesi belajar. Misalnya, kamu ingin memahami satu bab, menghafal kosakata baru, atau menyelesaikan beberapa soal latihan.

4. Belajar dalam sesi singkat
Belajarlah sekitar 25–30 menit, lalu beristirahat sebentar. Istirahat singkat dapat membantu pikiranmu tetap segar dan meningkatkan konsentrasi.

5. Buat catatan yang bermanfaat
Tuliskan gagasan penting, rumus, atau kata kunci. Kamu bisa menggunakan peta pikiran, tabel, atau rangkuman singkat agar informasi lebih mudah diingat.

6. Praktikkan apa yang kamu pelajari

7. Ulangi materi secara teratur
Tinjau kembali materi setelah beberapa hari, alih-alih mempelajari semuanya sekaligus. Pengulangan teratur membantu memperkuat ingatan dan mencegah kamu melupakan informasi penting.

8. Beristirahatlah dengan cukup
Setelah selesai belajar, sediakan waktu yang cukup untuk bersantai dan tidur. Tidur yang baik membantu otak memproses dan mengingat informasi yang sudah dipelajari.

Dengan mengikuti langkah-langkah ini, kamu dapat membuat waktu belajarmu lebih teratur, terfokus, dan efektif.''',
'passage-3': '''Labuan Bajo adalah kota kecil di Kabupaten Manggarai Barat, Nusa Tenggara Timur, Indonesia. Terletak di ujung barat Pulau Flores, kota ini dikelilingi perbukitan indah, perairan biru, dan banyak pulau kecil. Labuan Bajo dikenal luas sebagai salah satu gerbang utama menuju Taman Nasional Komodo, situs Warisan Dunia UNESCO. Pemandangan alamnya yang menakjubkan membuat kota ini semakin populer di kalangan wisatawan domestik maupun internasional.

Salah satu objek wisata paling luar biasa di dekat Labuan Bajo adalah Taman Nasional Komodo, habitat komodo yang terkenal. Taman ini juga menawarkan berbagai bentang alam, termasuk sabana, hutan tropis, pantai, dan terumbu karang. Pengunjung dapat menjelajahi pulau-pulau dengan perahu, melakukan snorkeling atau menyelam, serta menikmati pemandangan luas dari sejumlah bukit. Pulau Padar, misalnya, terkenal dengan bukit-bukit khasnya dan pantai indah dengan warna pasir yang berbeda-beda.

Labuan Bajo juga memiliki warisan budaya yang kaya. Masyarakat setempat terutama berasal dari suku Manggarai, yang tradisinya terlihat dalam upacara, tarian, musik, dan rumah adat mereka. Kuliner setempat juga merupakan bagian penting dari budaya daerah ini. Pengunjung dapat mencicipi beragam hidangan laut serta makanan tradisional dari bahan-bahan lokal. Perpaduan tradisi setempat dan pariwisata menciptakan pengalaman budaya yang unik bagi pengunjung.

Pariwisata berperan penting dalam perkembangan ekonomi Labuan Bajo. Hotel, restoran, layanan transportasi, operator wisata, dan usaha setempat menyediakan kesempatan kerja bagi warga. Pemerintah juga telah meningkatkan infrastruktur, termasuk jalan, fasilitas umum, dan layanan transportasi, untuk mendukung bertambahnya jumlah pengunjung. Namun, pengembangan pariwisata harus dikelola dengan hati-hati agar lingkungan alam dan warisan budaya daerah tetap terlindungi.

Labuan Bajo memiliki iklim tropis dengan suhu hangat sepanjang tahun. Keindahan alam, satwa liar yang unik, tradisi budaya, dan industri pariwisata yang berkembang menjadikannya destinasi penting di Indonesia bagian timur. Melalui pariwisata yang bertanggung jawab dan pelestarian lingkungan, Labuan Bajo dapat terus berkembang sambil menjaga sumber daya alam dan budayanya yang berharga.''',
'passage-4': '''November lalu, aku mendapat kesempatan menyaksikan Coldplay tampil langsung di Jakarta, sebuah pengalaman yang tetap menjadi salah satu momen paling berkesan dalam hidupku. Karena telah mengikuti musik band tersebut selama bertahun-tahun, aku selalu membayangkan bagaimana rasanya menyaksikan mereka tampil secara langsung. Jadi, ketika mengetahui Coldplay akhirnya akan mengadakan konser di Indonesia, aku langsung memutuskan untuk datang. Kakak perempuanku, yang juga menyukai musik mereka, setuju menemaniku.

Mendapatkan tiket ternyata sama sekali tidak mudah. Kami membelinya tiga bulan sebelum konser, tetapi ribuan penggemar mencoba mengakses situs penjualan tiket pada waktu yang sama. Setelah menunggu di antrean daring lebih dari satu jam, kami lega karena berhasil mendapatkan dua tiket untuk area duduk. Walaupun tempat duduk kami tidak sedekat yang diharapkan dengan panggung, kami bersyukur telah memperoleh tiket.

Pada hari konser, kami tiba di lokasi beberapa jam sebelum pertunjukan dimulai. Area tersebut sudah ramai oleh para penggemar antusias yang mengenakan kaus Coldplay dan membawa tongkat lampu warna-warni. Sambil menunggu gerbang dibuka, kami berfoto dan mengobrol dengan penggemar lain. Meski menunggu lama, semangat kerumunan membuat waktu terasa berlalu cepat.

Ketika memasuki stadion, kami menerima gelang khusus yang akan menyala selama pertunjukan. Tepat pukul delapan malam, lampu padam dan penonton bersorak saat band muncul di panggung. Ketika Coldplay membuka konser dengan lagu “Higher Power”, ribuan gelang menyala serentak, menciptakan pemandangan yang luar biasa. Saat itu aku menyadari bahwa konser ini lebih dari sekadar mendengarkan lagu-lagu favoritku.

Sepanjang pertunjukan, Coldplay membawakan beberapa lagu populer, termasuk “Yellow”, “Fix You”, dan “Viva La Vida”. Chris Martin juga berinteraksi dengan hangat bersama penonton dan bahkan mengucapkan beberapa kata dalam bahasa Indonesia. Upayanya menjalin hubungan dengan penonton setempat membuat pertunjukan terasa lebih personal.''',
'passage-5': '''Liburan lalu, teman-teman sekelasku dan aku pergi berwisata selama tiga hari ke Yogyakarta. Ini merupakan perjalanan sekolah pertama kami setelah sekian lama sebagian besar belajar di rumah, sehingga semua orang sangat bersemangat. Kami mengunjungi beberapa tempat bersejarah, mencoba makanan tradisional, dan mempelajari banyak hal menarik tentang budaya Jawa.

Pada hari pertama, kami mengunjungi Candi Borobudur pagi-pagi sekali. Cuacanya sejuk dan langit cerah saat kami tiba. Guru meminta kami berjalan mengelilingi candi dan mengamati pahatan batu di dindingnya. Seorang pemandu lokal menjelaskan bahwa candi tersebut dibangun berabad-abad lalu dan memuat banyak kisah tentang ajaran Buddha. Setelah menjelajahi candi, kami berfoto bersama sebelum berangkat ke hotel.

Keesokan paginya, kami pergi ke Pantai Parangtritis. Awalnya cuaca cerah, sehingga sebagian siswa bermain voli sementara yang lain berjalan menyusuri pantai. Namun, tiba-tiba awan gelap muncul dan angin kencang mulai bertiup. Guru kami segera meminta semua orang menjauh dari pantai dan menunggu di tempat yang lebih aman. Beberapa menit kemudian hujan deras turun. Walaupun tidak bisa menikmati pantai sesuai rencana, kami tertawa bersama sambil menunggu hujan reda.

Pada hari terakhir, kami mengunjungi pasar tradisional dekat Malioboro. Pasar itu ramai oleh penduduk setempat dan wisatawan. Kami membeli pakaian batik, suvenir kecil, dan jajanan tradisional untuk dibawa pulang. Aku sangat tertarik pada proses pembuatan batik karena salah seorang penjual menunjukkan bagaimana pola sederhana digambar pada kain menggunakan malam atau lilin panas. Sebelum pulang, kami makan siang di sebuah restoran kecil dan berbincang tentang pengalaman favorit kami selama perjalanan.

Perjalanan itu melelahkan, tetapi menjadi salah satu pengalaman paling berkesan selama aku bersekolah. Aku belajar bahwa bepergian bukan hanya tentang mengunjungi tempat-tempat indah. Bepergian juga berarti memahami sejarah, mengalami tradisi setempat, dan menciptakan kenangan tak terlupakan bersama teman-teman.'''
}
# Original questions are kept solely in source_extracted.json and unchanged by this layer.
question_translation={
1:'Pilihan manakah yang paling tepat merangkum cerita?',
2:'Ketika membaca bagian saat gajah mengatakan bahwa burung kecil terlalu kecil untuk melakukan sesuatu yang penting, akhir cerita manakah yang kamu perkirakan akan terjadi?',
3:'Pernyataan manakah yang paling tepat menyampaikan pesan cerita?',
4:'Mengapa gajah memutuskan membiarkan burung kecil pergi dan tidak mengusirnya?',
5:'Manakah di antara kalimat-kalimat berikut dari cerita yang membantumu memahami sifat gajah?',
6:'Berdasarkan informasi yang diberikan, kita dapat meningkatkan konsentrasi saat belajar dengan cara …',
7:'Dari pilihan yang tersedia, pilihlah urutan yang paling sesuai dengan informasi dalam teks “Cara Mempersiapkan Sesi Belajar yang Efektif”.',
8:'Apa tujuan utama teks tersebut?',
9:'Seorang siswa biasanya belajar lama tanpa istirahat dan sering lupa apa yang telah dipelajarinya. Strategi manakah dari teks yang paling sesuai untuk mengatasi masalah siswa tersebut?',
10:'Rani telah menyiapkan buku-bukunya dan memilih tempat belajar yang tenang. Namun, setelah mempelajari satu bab, ia masih kesulitan mengetahui bagian mana yang sudah benar-benar dipahaminya. Berdasarkan teks, apa yang sebaiknya Rani lakukan selanjutnya?',
11:'Fitur alam atau objek wisata apa saja yang disebutkan sebagai bagian dari Labuan Bajo dan sekitarnya? Centang semua jawaban benar berdasarkan teks. (Ada lebih dari satu jawaban benar.)',
12:'Aspek budaya Labuan Bajo apa saja yang disebutkan dalam teks? Centang semua jawaban benar. (Ada lebih dari satu jawaban benar.)',
13:'Aspek pariwisata dan perkembangan ekonomi Labuan Bajo mana saja yang disebutkan dalam teks? Centang semua jawaban benar. (Ada lebih dari satu jawaban benar.)',
14:'Kesimpulan apa saja yang dapat ditarik dari pengalaman penulis mendapatkan tiket dan menunggu konser? Centang semua jawaban benar. (Ada lebih dari satu jawaban benar.)',
15:'Mengapa penulis menyebut penggunaan bahasa Indonesia oleh Chris Martin selama konser? Centang semua jawaban benar. (Ada lebih dari satu jawaban benar.)',
16:'Pernyataan mana saja tentang penonton yang didukung oleh teks? Centang semua jawaban benar. (Ada lebih dari satu jawaban benar.)',
17:'Pernyataan mana saja yang paling tepat menjelaskan mengapa konser itu menjadi pengalaman berkesan bagi penulis? Centang semua jawaban benar. (Ada lebih dari satu jawaban benar.)',
18:'Bagian teks mana yang mendukung gagasan bahwa siswa belajar tentang sejarah dan tradisi setempat selama perjalanan? Pilih Ya atau Tidak untuk setiap kalimat.',
19:'Bagian teks mana yang mendukung gagasan bahwa siswa harus mengubah aktivitas karena cuaca selama perjalanan? Pilih Ya atau Tidak untuk setiap kalimat.',
20:'Apa yang dapat disimpulkan dari refleksi penulis tentang perjalanan itu? Pilih Ya atau Tidak untuk setiap kalimat.'
}
option_translations={
1:[
'Awal: Seekor burung kecil bernyanyi di pohon tinggi. Masalah: Gajah marah karena burung terlalu berisik. Penyelesaian: Burung berhenti bernyanyi dan terbang meninggalkan hutan. Pelajaran: Kita harus selalu menghindari mengganggu orang lain.',
'Awal: Gajah menertawakan burung kecil karena tubuhnya kecil. Masalah: Gajah terjebak dalam lumpur tebal di dekat sungai. Penyelesaian: Burung kecil memanggil hewan lain untuk membantu menyelamatkan gajah. Pelajaran: Semua orang dapat memberikan bantuan berharga, tanpa memandang ukuran tubuh.',
'Awal: Gajah dan burung kecil menjadi teman dekat. Masalah: Burung terjebak badai di dekat sungai. Penyelesaian: Gajah membawa burung ke tempat aman. Pelajaran: Teman baik selalu saling melindungi.',
'Awal: Gajah berjalan di hutan mencari makanan. Masalah: Badai dahsyat menghancurkan rumahnya. Penyelesaian: Burung kecil membangunkan rumah baru untuk gajah. Pelajaran: Kerja keras dapat menyelesaikan semua masalah.',
'Awal: Burung kecil ingin menjadi sebesar gajah. Masalah: Ia tidak bahagia karena lebih kecil daripada hewan lain. Penyelesaian: Gajah mengajarinya menjadi lebih kuat. Pelajaran: Kita sebaiknya mengubah diri agar diterima orang lain.'
],
2:['Burung kecil takut kepada gajah dan meninggalkan hutan.','Burung kecil berhenti bernyanyi karena ingin menjadi sebesar gajah.','Gajah marah dan mengusir semua hewan kecil.','Burung kecil meminta gajah mengajarinya menjadi lebih kuat.','Gajah mengalami kesulitan dan burung kecil membantunya bersama hewan-hewan lain.'],
3:['Makhluk kecil pun dapat membawa perubahan besar.','Kita tidak boleh menilai orang lain berdasarkan kepribadiannya.','Meminta bantuan orang lain dapat menyelesaikan masalah sulit.','Hewan besar selalu lebih kuat dan lebih penting daripada hewan kecil.','Kita tidak boleh menertawakan seseorang yang tampak lemah.'],
4:['Gajah terlalu lelah untuk berdebat dengan burung.','Burung kecil mengatakan kepada gajah bahwa suatu hari ia mungkin akan membantunya.','Gajah senang karena nyanyian burung membuatnya tenang.','Gajah mendengar hewan lain datang dan menjadi takut.','Burung kecil berjanji akan membawakan makanan untuk gajah.'],
5:['“Setiap pagi, gajah berjalan mengelilingi hutan untuk mencari dedaunan segar dan rumput sebagai makanan.”','“Gajah mendongak dan berkata, ‘Mengapa kamu bernyanyi begitu keras?’”','“Burung kecil terbang di atas mereka dan menunjukkan kepada semua hewan cara yang paling aman untuk membantu.”','“Gajah tertawa. ‘Kamu terlalu kecil untuk melakukan sesuatu yang penting,’ katanya.”','“Ia menatap burung kecil dengan heran dan berkata, ‘Terima kasih. Aku salah menilaimu.’”'],
6:['menyiapkan semua perlengkapan belajar','menetapkan tujuan belajar yang jelas','belajar dalam sesi singkat','mengulang materi secara teratur','membuat catatan yang bermanfaat'],
7:['Pilih tempat yang sesuai – Siapkan perlengkapan – Tetapkan tujuan yang jelas – Belajar dalam sesi singkat – Ulangi materi secara teratur','Siapkan perlengkapan – Beristirahat lama – Tetapkan tujuan yang jelas – Tonton video pelajaran – Beristirahat dengan cukup','Tetapkan tujuan yang jelas – Pilih tempat yang sesuai – Putar musik – Buat catatan bermanfaat – Belajar sepanjang malam','Belajar dalam sesi singkat – Lewati soal latihan – Ulangi materi secara teratur – Beristirahat lama – Tidur cukup','Pilih tempat yang sesuai – Gunakan kuis daring – Bergabunglah dengan kelompok belajar – Belajar sepanjang malam – Buat catatan bermanfaat'],
8:['Menjelaskan beberapa kegiatan yang dapat dilakukan siswa sebelum memulai pelajaran.','Memperkenalkan berbagai kebiasaan belajar yang dapat dipilih siswa sesuai preferensi mereka.','Menyajikan berbagai lingkungan belajar yang mungkin mendukung siswa selama ujian.','Menjelaskan beberapa cara siswa dapat mengatur waktu belajar dan meningkatkan hasil pembelajaran.','Menyajikan berbagai lingkungan belajar yang mungkin mendukung siswa selama ujian.'],
9:['Menyiapkan semua perlengkapan yang diperlukan sebelum memulai setiap sesi belajar.','Menulis informasi penting dalam bentuk rangkuman atau peta pikiran.','Membagi waktu belajar menjadi beberapa periode singkat yang diikuti istirahat sebentar dan pengulangan teratur.','Memilih tempat belajar yang nyaman dengan cahaya cukup dan sedikit gangguan.','Menjawab soal latihan setelah menyelesaikan setiap topik dengan berkali-kali memeriksa catatan.'],
10:['Menjawab beberapa soal tentang bab tersebut tanpa melihat catatannya.','Menulis ulang seluruh bab dengan kata-katanya sendiri sebelum melanjutkan.','Beristirahat lebih lama sebelum memulai sesi belajar berikutnya.','Mengumpulkan buku dan bahan tambahan terkait bab tersebut.','Membaca ulang bab tersebut beberapa kali sampai ia mengingat semuanya.'],
11:['Hutan tropis','Terumbu karang','Pegunungan yang tertutup salju','Danau beku','Pulau Padar'],
12:['Tradisi Manggarai','Tarian dan musik tradisional','Rumah adat','Festival budaya Eropa','Upacara tradisional Jepang'],
13:['Pariwisata telah sepenuhnya menggantikan usaha setempat.','Kota tersebut terutama bergantung pada ekspor hasil pertanian.','Pariwisata berkontribusi terhadap perkembangan ekonomi.','Pemerintah telah memperbaiki infrastruktur.','Pariwisata telah mengurangi kesempatan kerja.'],
14:['Datang lebih awal ke lokasi membuat penulis terhindar dari keramaian di sekitar stadion.','Kesulitan memperoleh tiket meningkatkan rasa syukur penulis karena dapat menghadiri konser.','Penulis menganggap lokasi tempat duduk tidak penting karena duduk dekat panggung bukan bagian dari rencana awal.','Semangat penulis tetap terjaga meskipun menghadapi ketidaknyamanan saat menghadiri konser.','Interaksi dengan penggemar lain membantu menjadikan masa menunggu sebagai bagian dari pengalaman konser.'],
15:['Menunjukkan bahwa Chris Martin berusaha menjalin hubungan dengan penonton Indonesia.','Menjelaskan mengapa konser terasa lebih personal bagi penulis dan Chris Martin.','Membuktikan bahwa Chris Martin fasih berbahasa Indonesia.','Menekankan interaksi hangat antara penampil dan penonton.','Menunjukkan bahwa konser terutama diselenggarakan untuk penggemar yang berbahasa Indonesia.'],
16:['Banyak penonton menunjukkan antusiasme sebelum memasuki lokasi konser.','Sebagian penggemar mengenakan pakaian yang berkaitan dengan Coldplay dan membawa tongkat lampu.','Penonton kebanyakan tetap diam sambil menunggu konser dimulai.','Ribuan penonton ikut bernyanyi selama pertunjukan.','Sebagian besar penonton adalah orang-orang yang sudah saling mengenal.'],
17:['Penulis tidak pernah mengikuti musik Coldplay selama bertahun-tahun, lalu akhirnya menyaksikan mereka tampil langsung.','Efek visual ribuan gelang yang menyala menciptakan momen berkesan.','Interaksi antara band dan penonton memberi dimensi personal pada konser.','Penulis dapat duduk sangat dekat dengan panggung sepanjang pertunjukan.','Penulis memperoleh kesadaran bermakna tentang kekuatan musik untuk menyatukan orang-orang.'],
18:['Seorang pemandu lokal menjelaskan bahwa candi dibangun berabad-abad lalu dan memuat banyak kisah tentang ajaran Buddha. (Ya / Tidak)','Salah seorang penjual menunjukkan bagaimana pola sederhana digambar pada kain menggunakan malam atau lilin panas. (Ya / Tidak)','Sebagian siswa bermain voli sedangkan yang lain berjalan di tepi pantai. (Ya / Tidak)'],
19:['Para siswa berfoto bersama setelah menjelajahi Candi Borobudur. (Ya / Tidak)','Awan gelap tiba-tiba muncul dan angin kencang mulai bertiup di Pantai Parangtritis. (Ya / Tidak)','Pemandu wisata meminta semua orang menjauh dari pantai dan menunggu di tempat yang lebih aman. (Ya / Tidak)'],
20:['Penulis mempelajari hal-hal baru dan menciptakan kenangan indah selama perjalanan. (Ya / Tidak)','Penulis menganggap mengunjungi tempat-tempat indah sebagai satu-satunya tujuan penting bepergian. (Ya / Tidak)','Penulis menganggap perjalanan itu berharga meskipun melelahkan. (Ya / Tidak)']
}
# Each excerpt is verified as a literal substring of the extracted English passage.
keys={1:['B'],2:['E'],3:['A'],4:None,5:None,6:['C'],7:['A'],8:['D'],9:['C'],10:['A'],11:['A','B','E'],12:['A','B','C'],13:['C','D'],14:['B','D','E'],15:['A','D'],16:['A','B'],17:['B','C'],18:{'A':'Yes','B':'Yes','C':'No'},19:None,20:{'A':'Yes','B':'No','C':'Yes'}}
evidence={
1:['The elephant laughed. "You are too small to do anything important," he said.','She quickly flew around the forest and called the other animals.','Everyone has something useful to give, no matter how big or small they are.'],
2:['The elephant laughed. "You are too small to do anything important," he said.','The little bird heard the elephant\'s loud cries.'],
3:['Everyone has something useful to give, no matter how big or small they are.'],
4:['The bird felt sad, but she did not argue with him.'],
5:['The elephant laughed. "You are too small to do anything important," he said.','Thank you. I was wrong about you.'],
6:['Study for about 25–30 minutes, then take a short break.','A brief rest can help your mind stay fresh and improve your concentration.'],
7:['1. Choose a suitable place','2. Prepare Your Materials','3. Set a Clear Goal','4. Study in Short Sessions','7. Review Regularly'],
8:['By following these steps, you can make your study time more organized, focused, and effective.'],
9:['Study for about 25–30 minutes, then take a short break.','Review the material after a few days instead of studying everything at once.'],
10:['6. Practice What You Learn'],
11:['including savannas, tropical forests, beaches, and coral reefs.','Padar Island, for example, is well known'],
12:['whose traditions can be seen in their ceremonies, dances, music, and traditional houses.'],
13:['Tourism plays an important role in the economic development of Labuan Bajo.','The government has also improved infrastructure'],
14:['we were grateful to have tickets.','Despite the long wait, the excitement among the crowd made the time pass quickly.','we took photographs and talked with other fans.'],
15:['Chris Martin also interacted warmly with the audience and even spoke some Bahasa Indonesia.','His effort to connect with the local audience made the performance feel more personal.'],
16:['The area was already crowded with enthusiastic fans wearing Coldplay shirts and carrying colorful light sticks.','the crowd erupted in cheers as the band appeared on stage.'],
17:['thousands of wristbands illuminated at the same time, creating a breathtaking display.','His effort to connect with the local audience made the performance feel more personal.'],
18:['A local guide explained that the temple was built many centuries ago and contains many stories about Buddhist teachings.','one of the sellers showed us how simple patterns were drawn on the fabric using hot wax.'],
19:['Our teacher quickly asked everyone to move away from the beach and wait in a safer place.','However, dark clouds suddenly appeared, and strong wind began to blow.'],
20:['I learned that traveling was not only about visiting beautiful places.','The trip was tiring, but it became one of the most memorable experiences of my school life.']
}
explanations={
1:'Soal meminta rangkuman yang memuat awal, konflik, penyelesaian, dan pesan cerita secara utuh. Gajah meremehkan burung; ia lalu terjebak lumpur; burung mengorganisasi penyelamatan; akhirnya gajah belajar bahwa ukuran tubuh bukan ukuran nilai pertolongan. Hanya B cocok di setiap tahap.',
2:'Kata “anticipate” meminta kita memperkirakan arah perkembangan cerita berdasarkan konflik awal. Ucapan meremehkan burung menyiapkan pembalikan keadaan: justru si burung kelak akan berguna ketika gajah kesulitan. Ini juga benar-benar terjadi dalam kelanjutan cerita.',
3:'Pertanyaan menanyakan amanat utama, bukan sekadar peristiwa. Burung kecil bisa mengerahkan bantuan bagi gajah besar sehingga ukuran fisik tidak menentukan manfaat seseorang. Opsi A menangkap inti tersebut.',
4:'Tidak ada bagian cerita yang mengatakan gajah “memutuskan membiarkan burung pergi” atau “tidak mengusirnya”. Setelah mengejek, cerita hanya menyebut burung merasa sedih dan tidak membantah. Kelima pilihan alasan menambah informasi yang tidak diberikan. Karena itu soal ini tidak layak diberi nilai pasti.',
5:'Kata “character” mengacu pada sifat/kepribadian tokoh, tetapi beberapa kutipan memang menggambarkannya. D menunjukkan sikap merendahkan pada awal cerita; E menunjukkan penyesalan dan perubahan sikap pada akhir cerita; B juga bisa mencerminkan sikapnya saat mempertanyakan nyanyian burung. Tanpa kriteria lain, tidak ada satu opsi unik yang dapat dipastikan.',
6:'Teks menghubungkan secara langsung belajar 25–30 menit lalu istirahat dengan peningkatan konsentrasi. Pilihan lain merupakan strategi belajar yang sah, tetapi hanya C disebut secara eksplisit sebagai cara meningkatkan “concentration”.',
7:'Cari urutan judul langkah bernomor dalam bacaan. Teks menyebut memilih tempat → menyiapkan bahan → menetapkan tujuan → belajar singkat → mengulang secara teratur (langkah 1, 2, 3, 4, dan 7). A mempertahankan urutan dan tidak menambahkan langkah yang dilarang atau tidak disebut.',
8:'“Main purpose” menanyakan tujuan keseluruhan teks prosedural. Artikel memberi berbagai tindakan untuk menata sesi belajar agar lebih fokus dan efektif. D mencakup persiapan, strategi saat belajar, pengulangan, dan istirahat. Pilihan C dan E bahkan tercetak identik di PDF, tetapi keduanya bukan tujuan utama.',
9:'Dua masalah harus ditangani sekaligus: terlalu lama tanpa jeda dan sering lupa. Langkah 4 menganjurkan sesi singkat dengan istirahat; langkah 7 menyarankan pengulangan berkala. Opsi C menggabungkan keduanya.',
10:'Rani ingin mengetahui bagian yang sudah dan belum dipahami. Menguji diri dengan soal tanpa membuka catatan adalah cara masuk akal untuk menilai pemahaman, sejalan dengan judul langkah 6, “Practice What You Learn”. Perlu dicatat: PDF tidak menyertakan penjelasan untuk langkah 6; rincian “tanpa catatan” adalah inferensi, bukan kutipan dari paragraf yang hilang.',
11:'Ini soal pilih semua jawaban benar, bukan satu saja. Pada paragraf kedua, taman nasional memiliki “tropical forests” dan “coral reefs”; Pulau Padar juga disebut. Tidak ada pegunungan bersalju maupun danau beku.',
12:'Paragraf ketiga menjelaskan masyarakat Manggarai, tradisi, tarian, musik, dan rumah adat. Ketiga pilihan A, B, dan C tepat. Tidak ada penyebutan festival Eropa atau upacara Jepang.',
13:'Paragraf keempat menyatakan pariwisata penting bagi perkembangan ekonomi dan pemerintah meningkatkan infrastruktur. Teks justru menyatakan usaha setempat memberi lapangan kerja, bukan digantikan atau mengurangi pekerjaan.',
14:'Meskipun penulis menunggu antrean tiket lama dan tidak mendapatkan kursi sedekat harapan, ia bersyukur tetap mendapat tiket (B). Semangat bertahan meski menunggu (D), sedangkan berfoto dan bercakap dengan sesama penggemar membantu membuat masa tunggu menjadi bagian pengalaman positif (E).',
15:'Kalimat penutup menerangkan bahwa penggunaan bahasa Indonesia adalah usaha Chris Martin mendekati penonton setempat dan membuat pertunjukan terasa personal. Jadi A dan D. B menambahkan bahwa Chris Martin sendiri merasakan konser itu lebih personal—perasaan tersebut tidak dinyatakan; C dan E juga tidak ditunjukkan.',
16:'Kerumunan sudah antusias sebelum pertunjukan, mengenakan kaus band dan membawa tongkat lampu. Itu mendukung A dan B. Teks menyebut sorakan dan gelang menyala, tetapi tidak pernah mengatakan ribuan orang bernyanyi; jangan mengganti “cheers” dengan “singing”.',
17:'Penulis sangat terkesan oleh gelang yang menyala serentak (B) dan kehangatan interaksi band dengan penonton (C). Opsi E mungkin terasa selaras secara tematik, tetapi teks hanya menyatakan konser lebih daripada mendengarkan lagu, tidak secara khusus menyimpulkan bahwa musik menyatukan orang. Karena itu E tidak dihitung sebagai bukti yang cukup untuk klaim spesifik tersebut.',
18:'Perhatikan apakah setiap kalimat membuktikan pembelajaran sejarah atau tradisi. Keterangan pemandu tentang Borobudur merupakan informasi sejarah (A: Ya); demonstrasi pembuatan batik menunjukkan tradisi (B: Ya); kegiatan bermain voli di pantai tidak menunjukkan keduanya (C: Tidak).',
19:'Ini adalah masalah sumber yang tidak bisa digradasi dengan yakin. B jelas terkait perubahan cuaca; A tidak. C menggambarkan tindakan evakuasi yang memang terjadi, tetapi subjeknya keliru: soal menyebut “tour guide”, sedangkan cerita mengatakan “our teacher”. Penilaian Ya/Tidak untuk C akan bergantung pada apakah kesalahan identitas diabaikan, sehingga seluruh soal ditandai belum terselesaikan.',
20:'Penulis menyebut mempelajari sejarah dan tradisi serta membentuk kenangan, jadi A = Ya. Ia justru menolak bahwa bepergian hanya berarti melihat tempat indah, jadi B = Tidak. Ia menyebut perjalanan melelahkan tetapi berkesan, jadi C = Ya.'
}
reasons={
1:{'A':'Tidak ada adegan burung berhenti bernyanyi atau meninggalkan hutan.','B':'Sesuai dengan seluruh alur: ejekan, lumpur, penyelamatan, dan pesan tentang manfaat setiap makhluk.','C':'Peran penyelamat dibalik; burung tidak diselamatkan gajah.','D':'Badai tidak dikatakan merusak rumah gajah; burung tidak membangunkan rumah.','E':'Burung tidak ingin menjadi besar; pesan cerita bukan mengubah diri untuk diterima.'},
2:{'A':'Burung tetap berada di hutan dan menolong gajah.','B':'Tidak ada keinginan burung untuk menjadi sebesar gajah.','C':'Gajah tidak mengusir hewan-hewan kecil.','D':'Burung tidak meminta pelatihan kekuatan.','E':'Tepat: konflik awal dibalik saat burung mengumpulkan hewan untuk menolong gajah.'},
3:{'A':'Paling luas menangkap pesan moral tentang kontribusi makhluk kecil.','B':'Fokusnya bukan kepribadian, melainkan prasangka berdasarkan ukuran tubuh.','C':'Ada unsur kerja sama, tetapi ini bukan pesan sentral mengenai nilai makhluk kecil.','D':'Bertentangan dengan moral kisah.','E':'Sikap tidak mengejek memang pelajaran pendukung, tetapi A lebih tepat merangkum alasan di baliknya.'},
4:{'A':'Kelelahan terjadi saat gajah terjebak, bukan saat berbicara dengan burung.','B':'Burung tidak pernah meramalkan ia akan membantu suatu hari.','C':'Tidak ada pernyataan bahwa nyanyian burung menenangkan gajah.','D':'Tidak diceritakan hewan lain datang ketika gajah berbicara dengan burung.','E':'Burung tidak membuat janji membawa makanan.'},
5:{'A':'Menjelaskan rutinitas makan, relatif sedikit tentang sifat gajah.','B':'Pertanyaan bernada meremehkan dapat memberi petunjuk karakter, walau tidak sekuat D.','C':'Menggambarkan tindakan burung kecil, bukan sifat gajah.','D':'Menunjukkan kesombongan dan kebiasaan memandang rendah makhluk kecil.','E':'Menunjukkan kesediaan mengakui kesalahan dan perkembangan karakter.'},
6:{'A':'Menyiapkan bahan menghemat waktu dan mencegah gangguan, tetapi kalimat tentang konsentrasi ada di langkah 4.','B':'Tujuan jelas membantu arah belajar, tidak secara langsung disebut meningkatkan konsentrasi.','C':'Benar: istirahat singkat membuat pikiran segar dan meningkatkan konsentrasi.','D':'Pengulangan teratur dijelaskan berguna untuk ingatan.','E':'Catatan berguna membuat informasi lebih mudah diingat, bukan penjelasan paling langsung tentang konsentrasi.'},
7:{'A':'Sesuai dengan urutan langkah 1, 2, 3, 4, lalu 7.','B':'“Take long breaks” dan “Watch lesson videos” tidak menjadi urutan langkah yang ditulis.','C':'“Play music” dan “Study all night” tidak dianjurkan dalam teks.','D':'Melewati latihan dan beristirahat lama tidak sesuai instruksi.','E':'Kelompok belajar dan belajar semalaman tidak tercantum sebagai tahapan.'},
8:{'A':'Terlalu sempit: teks juga membahas apa yang dilakukan selama dan setelah belajar.','B':'Teks memberi panduan untuk efektivitas, bukan sekadar menawarkan kebiasaan sesuai selera.','C':'Identik dengan E dan terlalu berfokus pada lingkungan saat ujian.','D':'Mewakili keseluruhan tujuan: pengaturan belajar dan hasil yang lebih baik.','E':'Duplikat C di PDF; tidak dipilih karena tidak mewakili tujuan keseluruhan.'},
9:{'A':'Tidak membahas jeda atau pengulangan materi.','B':'Membantu mengingat, tetapi tidak menyelesaikan kebiasaan belajar terlalu lama tanpa istirahat.','C':'Menggabungkan sesi pendek, istirahat, dan pengulangan berkala untuk kedua masalah.','D':'Mengurangi gangguan tempat belajar tetapi bukan solusi lengkap.','E':'Latihan dapat membantu pemahaman, namun pilihan ini tidak memecahkan persoalan jeda dan pengulangan sebaik C.'},
10:{'A':'Menguji diri tanpa catatan mengungkap bagian yang belum dikuasai; disimpulkan dari judul langkah 6.','B':'Menulis ulang seluruh bab bukan strategi evaluasi yang ditulis.','C':'Istirahat berguna, tetapi tidak menunjukkan pemahaman setiap bagian.','D':'Rani sudah menyiapkan bahan; bahan tambahan tidak otomatis mengukur pemahaman.','E':'Membaca ulang tidak menguji apakah ia benar-benar bisa menjawab sendiri.'},
11:{'A':'Ya: “tropical forests” tercantum dalam bentang alam taman nasional.','B':'Ya: “coral reefs” tercantum bersama hutan, pantai, dan sabana.','C':'Tidak: salju atau pegunungan bersalju tidak disebutkan.','D':'Tidak: danau beku tidak disebutkan.','E':'Ya: “Padar Island” disebut secara langsung.'},
12:{'A':'Ya: penduduk dan tradisi Manggarai disebut.','B':'Ya: “dances, music” ditulis sebagai wujud tradisi.','C':'Ya: “traditional houses” disebut.','D':'Tidak: tidak ada festival budaya Eropa.','E':'Tidak: tidak ada upacara tradisional Jepang.'},
13:{'A':'Keliru: justru usaha setempat disebut menyediakan pekerjaan.','B':'Tidak disebutkan bahwa ekspor pertanian menjadi sandaran ekonomi utama.','C':'Benar: paragraf ekonomi dibuka dengan peran penting pariwisata.','D':'Benar: pemerintah meningkatkan jalan, fasilitas umum, dan transportasi.','E':'Keliru: teks menyebut peluang kerja meningkat melalui berbagai layanan.'},
14:{'A':'Teks menyatakan area sudah ramai saat mereka tiba; tidak terhindar dari kerumunan.','B':'Benar secara inferensial: antrean sulit tetapi tiket akhirnya disambut syukur.','C':'Kursi dekat panggung justru menjadi harapan yang tidak terpenuhi.','D':'Benar: masa menunggu lama tetapi semangat penonton bertahan.','E':'Benar: foto dan percakapan dengan penggemar mewarnai pengalaman menunggu.'},
15:{'A':'Benar: penggunaan bahasa lokal ditafsirkan sebagai upaya terhubung dengan audiens Indonesia.','B':'Teks menyatakan penampilan terasa personal, tetapi tidak menyebut perasaan Chris Martin sendiri.','C':'Mengucapkan beberapa kata tidak membuktikan kefasihan.','D':'Benar: paragraf secara langsung menyebut interaksi hangat.','E':'Tidak ada informasi tentang segmentasi utama penyelenggara konser.'},
16:{'A':'Benar: penggemar antusias sebelum gerbang dibuka.','B':'Benar: kaus Coldplay dan tongkat lampu tercatat eksplisit.','C':'Keliru: suasana antusias, bukan sebagian besar diam.','D':'Tidak didukung: sorakan bukan bukti bahwa ribuan orang ikut bernyanyi.','E':'Tidak didukung: penulis malah berkenalan dan berbicara dengan penggemar lain.'},
17:{'A':'Keliru: penulis jelas sudah mengikuti musik Coldplay selama bertahun-tahun.','B':'Benar: nyala ribuan gelang disebut menciptakan pemandangan menakjubkan.','C':'Benar: interaksi hangat membuat pertunjukan terasa personal.','D':'Keliru: tempat duduk mereka tidak sedekat yang diharapkan.','E':'Interpretasi menarik, tetapi kesimpulan spesifik tentang musik menyatukan orang tidak dinyatakan dengan jelas.'},
18:{'A':'Ya: pemandu memberi informasi usia candi serta ajaran Buddha.','B':'Ya: demonstrasi membatik mengenalkan tradisi kerajinan setempat.','C':'Tidak: voli dan berjalan di pantai hanya kegiatan rekreasi.'},
19:{'A':'Tidak berhubungan dengan perubahan cuaca atau aktivitas di pantai.','B':'Ya, jelas menunjukkan cuaca memburuk sehingga rencana diubah.','C':'Tindakan pindah tempat benar, tetapi pelaku di sumber adalah guru, bukan pemandu wisata; status Ya/Tidak perlu keputusan editorial sumber.'},
20:{'A':'Ya: penulis mendapat pelajaran sejarah dan budaya, serta kenangan bersama teman.','B':'Tidak: penulis mengatakan perjalanan bukan hanya mengunjungi tempat indah.','C':'Ya: meskipun melelahkan, perjalanan dianggap salah satu pengalaman paling berkesan.'}
}
issues={
4:'Premis pertanyaan (membiarkan burung pergi/tidak mengusirnya) tidak muncul di cerita; tidak ada pilihan didukung.',
5:'Instruksi tidak mengatakan pilih lebih dari satu, tetapi D dan E sama-sama menunjukkan karakter; B juga mungkin relevan.',
8:'Pilihan C dan E merupakan duplikasi verbatim dari sumber.',
10:'Langkah 6 dalam sumber hanya berisi judul, tanpa uraian; jawaban A memakai inferensi pedagogis dari judul.',
17:'Pilihan E dapat diperdebatkan sebagai interpretasi tematis; teks tidak mengungkap klaim khusus “music to bring people together”.',
19:'Pernyataan C salah mengidentifikasi guru (“teacher”) sebagai pemandu wisata (“tour guide”).'
}
for p in source['passages']:
    p['translationId']=passage_id[p['id']]
    p.pop('startPage',None)
for q in source['questions']:
    n=q['number']
    q['translationId']={'prompt':question_translation[n], 'options':dict(zip('ABCDE',option_translations[n]))}
    q['answer']=keys[n]
    q['answerProvenance']='independently-derived' if keys[n] is not None else 'unresolved'
    q['explanationId']=explanations[n]
    q['optionReasonId']=reasons[n]
    q['evidence']=[{'quote':t,'kind':'direct' if n not in (2,10,14,17,20) else 'supporting-text'} for t in evidence[n]]
    q['vocabulary']=({1:[['regardless of','tanpa memandang'],['trapped','terjebak']],2:[['anticipate','memperkirakan']],3:[['conveys','menyampaikan']],6:[['concentration','konsentrasi']],9:[['regular reviews','pengulangan teratur']],10:[['referring to','merujuk pada']],11:[['coral reefs','terumbu karang']],14:[['appreciation','rasa menghargai / rasa syukur']],15:[['fluently','dengan fasih']],17:[['memorable','berkesan']],20:[['reflection','renungan / refleksi']]}.get(n,[]))
    if n in issues: q['sourceIssue']=issues[n]
    if q['type']=='category':
       q['categories']=[{'id':'Yes','label':'Yes','translation':'Ya'}, {'id':'No','label':'No','translation':'Tidak'}]
       q['scoring']='all-rows-correct'
    elif q['type']=='multiple': q['scoring']='exact-set'
    else: q['scoring']='single-exact'
    if n in (4,5,19): q['graded']=False
    else: q['graded']=True
    for ev in q['evidence']:
       passage=next(p['original'] for p in source['passages'] if p['id']==q['passageId'])
       if ev['quote'] not in passage:
         raise AssertionError(f'Q{n} evidence quote NOT found: {ev["quote"]!r}')
    assert len(q['options'])==len(q['translationId']['options'])==len(q['optionReasonId'])
source.update({'schemaVersion':1,'id':'tka-eng-to03-elephant-study-labuan-bajo','title':'TKA Bahasa Inggris — TO 03','subtitle':'Elephant · Study Session · Labuan Bajo · Coldplay · Yogyakarta','exam':'TKA','subject':'Bahasa Inggris Wajib','topics':['Reading comprehension','Narrative','Procedure','Description','Recount'],'language':'en','supportLanguage':'id','questionCount':20,'estimatedMinutes':None,'officialDurationMinutes':None,'year':None,'source':{'file':'103 TO 03 TKA ENG (Elephant, Study Session, Labuan Bajo).pdf','pages':8,'answerKeyIncluded':False,'publicationRights':'not verified','editorialReview':'independently-derived, nonofficial; unresolved keys excluded from score'},'contentRevision':1,'gradingPolicy':{'single':'exact match','multiple':'exact-set, no partial credit','category':'all-rows-correct, no partial credit','unresolved':'excluded from points and denominator'},'keyStatus':'independently-derived-with-unresolved'})
# Enrich passage with real page: page #1 title for first, #3, #4, #6, #7 respectively.
for p,page in zip(source['passages'],[1,3,4,6,7]):p['page']=page
out=root/'data/tests/tka-eng-to03.json'
out.write_text(json.dumps(source,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print('saved',out,'graded',sum(q['graded'] for q in source['questions']))
