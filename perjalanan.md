
# Perjalanan

Markdown file ini gunanya untuk merekam perjalanan kita supaya ga sesat di tengah jalan. Juga untuk kilas balik dan ngeliat kita belajar apa aja.

## Speech Recognition & Mic Library untuk Python 
Kita ga puas kalo cuma pake API yg tersedia online untuk Speech Recognition. Gimana kalo misalnya kita pengen mbak-chan untuk ngertiin kita lebih dalam? Kata" gaul pastinya ga akan dikenali API yang ada diluar sana. Jadi, kita akhirnya berniat untuk membuat Speech Recognition ML kita sendiri, yakni menjadi bagian otak nya mbak-chan.
Untuk telinganya mbak-chan, Ferry yg memang lebih pakar di hardware jadi *in charge* untuk konfigurasi mic nya dan gimana supaya mbak-chan bisa mendengar kita dgn baik. Untuk mic-nya kita pake mic $5 dari shopee yg awalnya harus teriak supaya mbak-chan bisa denger. (2 Sept 2020)
<hr>

### Speech Recognition (@FolkLoreee)

<hr>

Tujuan Speech Recognition ini sebenernya simpel aja, gara" kita gamau mode input yg konvensional (keyboard dan mouse). Jadi pilihan kita emang terbatas: suara, atau visual. Visual akhirnya kita kesampingkan soalnya mahal (untuk tingkat *inference* yg cepet, harus pake usb coral atau sejenisnya yg lumayan mahal buat kantong kita saat ini). Jadi, solusi murah meriahnya: microphone $5. 

Karena gw ga berpengalaman di bidang AI dan audio secara umum, gw pertama harus belajar teori di balik AI dlm bidang speech recognition ini, supaya seenggaknya tau apa yg harus gw research nanti.
Material bacaan pertama: [Artikel Medium tentang ML Speech Recognition](https://medium.com/@ageitgey/machine-learning-is-fun-part-6-how-to-do-speech-recognition-with-deep-learning-28293c162f7a)

Selanjutnya, gw bakal baca lebih dlm lagi untuk AI dan audio dlm artikel / paper research yg khusus ngebahas material" ini.
Material bacaan AI:
* [Recurrent Neural Network](https://medium.com/@ageitgey/machine-learning-is-fun-part-2-a26a10b68df3)
* [Baidu Speech Recognition Talk](https://www.youtube.com/watch?v=9dXiAecyJrY&feature=youtu.be&t=13874)
* [Riset ttg Recurrent Neural Network](http://www.cs.toronto.edu/~graves/icml_2006.pdf)

Material bacaan audio:
* [Pengenalan Fourier Transformation](https://en.wikipedia.org/wiki/Fourier_transform). Fourier Transformation ini jadi gunanya untuk membagi audio ke dlm beberapa segment. Soalnya, setiap kata yg terucap dari mulut orang itu terdiri dari macem" frekuensi.
* [Video penjelasan tentang fungsi Fourier Transformation](https://www.youtube.com/watch?v=spUNpyF58BY). Secara matematis, fungsi ini berupa:  
> $$\int_{t1}^{t2} g(t)e^{-2\pi ift}dt $$ 
Kalau kita *Fourier*-kan fungsi ini, bisa diliat kalo:
> $$e^{-2\pi ift}$$
cuma fungsi untuk gambar lingkaran, dan
> $$g(t)$$
cuma fungsi arbitrari (dlm konteks ini fungsi tekanan udara terhadap waktu)
> $$\int_{t1}^{t2} dt $$
cuma ngasih *magnitude* dari "center of mass" graph nya dari waktu *t1* sampe *t2*. Konsekuensinya itu ya kalo magnitude ini ga deket" sama 0 berarti salah satu konstituen suara itu berasal dari frekuensi tersebut.

<hr>

## Konfigurasi Telinga (@FerryC13)

<hr>