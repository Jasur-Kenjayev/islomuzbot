from aiogram.types import Message
from loader import dp


@dp.message_handler(text="Alloh")
async def al_allah(message:
Message):
	await message.answer("<b>الله--Alloh\n\nManosi: Xudoning ismi. Barcha suralarning (bittasidan tashqari) boshlanishida qoʻllaniladi</b>")
	
@dp.message_handler(text="Ar-Rohmān")
async def ar_rohman(message:
Message):
	await message.answer("<b>Ar-Rohmān--الرحمن\n\nManosi: Mehribon — Ulugʻ ne'matlarni beruvchi.Bu sifatfaqat Allohga xos boʻlib, barchaga kofirga ham, moʻminga ham mehribon va ne'mat beruvchi ma'nosini anglatadi.Rahmon sifatini Alloh taolodan boshqa hech kimga nisbatan ishlatib boʻlmaydi.</b>")
	
@dp.message_handler(text="Ar-Rohīm")
async def al_ar_rohim(message:
Message):
	await message.answer("<b>Ar-Rohīm--الرحيم\n\nManosi: Rahmli — „Rohiym“ latif ne'matlarni beruvchi.Bu sifat xosroq boʻlib, qiyomat kuni faqat moʻminlarga rahm qiluvchi ma'nosini anglatadi.Va Allohdan oʻzgalarga, jumladan Paygʻambar alayhissalomga nisbatan ham ishlatiladi.</b>")
	
@dp.message_handler(text="Al-Malik")
async def al_malik(message:
Message):
	await message.answer("<b>Al-Malik--الملك\n\nManosi: Podsho — Barcha narsani egasi. Malik haqiqiy egadir.Undan oʻzga ega yoqdir.Shuning uchun bandalar faqat unga qul boʻladilar.Hech vaqtda bir qulga ikki xoʻjayin boʻlmaydi.Shuning uchun insonlar oʻzlariga oʻxshaganinsonlarga emas, balki yagona yaratganga, haqiqiy Malikka qul boʻlish lozim.</b>")
	
@dp.message_handler(text="Al-Quddūs")
async def al_quddus(message:
Message):
	await message.answer("<b>Al-Quddūs--القدوس\n\nManosi: Muqaddas, nuqsonlardan holi — Barcha ayblardan xoli, noloyiq sifatlardan munazzah, mutlaq muqaddaslik va mutlaq poklik Allohning oʻzigagina hosdir.</b>")
	
@dp.message_handler(text="As-Salām")
async def al_salam(message:
Message):
	await message.answer("<b>As-Salām--السلام\n\nManosi: Ofat va balolardan solomat. Qutqarayotgan — „Salom“-barcha nuqsonlardan salomat. Shuningdek, tinchlik, xotirjamlik va rohat beruvchi degani. Alloh „Salom“ sifati ila bandalarga tinchlik, omonlik, xotirjamlik ato qiladi</b>")
	
@dp.message_handler(text="Al-Mu’min")
async def al_mumin(message:
Message):
	await message.answer("<b>Al-Mu’min--المؤمن\n\nManosi: Moʻmin-iymon va omonlik beruvchi.</b>")
	
@dp.message_handler(text="Al-Muhaymin")
async def al_muhaymin(message:
Message):
	await message.answer("<b>Al-Muhaymin--المهيمن\n\nManosi: Hamma narsani qamrab oluvchi.Alloh bandalarning barcha holatlariga guvoh boʻlib turadi.Undan hech narsa maxfiy qolmaydi.</b>")
	
@dp.message_handler(text="Al-Aziz")
async def al_aziz(message:
Message):
	await message.answer("<b>Al-Aziz--العزيز\n\nManosi: Izzat va qudrat sohibi. Ulugʻ — Barchaning ustidan gʻolib. Undan biror narsa gʻolib kelolmaydi.</b>")
	
@dp.message_handler(text="Al-Jabbār")
async def al_jabbar(message:
Message):
	await message.answer("<b>Al-Jabbār--الجبار\n\nManosi: Bandalarini ishlarini isloh etuvchi. Jabbor — oliy qadar ulugʻ, Uning oldida hamma oʻzini xor tutadi.</b>")
	
@dp.message_handler(text="Al-Mutakabbir")
async def al_mutakabbir(message:
Message):
	await message.answer("<b>Al-Mutakabbir--المتكبر\n\nManosi: Kattalik yarashuvchi zot. Mutakabbir — kibriyosi va ulugʻligi behad. Uning oldida boshqalar qul boʻlib turadi.</b>")
	
@dp.message_handler(text="Al-Holiq")
async def al_holiq(message:
Message):
	await message.answer("<b>Al-Holiq--الخالق\n\nManosi: Yaratuvchi, vujudga keltiruvchi. Xoliq — Asli va oʻxshashi yoq narsaning oʻlchovini mos qilib yaratuvchi. Xoliq mutloq vujudga keltiruvchidir.</b>")
	
@dp.message_handler(text="Al-Bāri")
async def al_bari(message:
Message):
	await message.answer("<b>Al-Bāri'--البارئ\n\nManosi: Bori' — Yoʻqdan paydo qiluvchi, vujudga keltiruvchi, yaratuvchi. Bori’ning vujudga keltirishida tafovut yoqdir.</b>")
	
@dp.message_handler(text="Al-Musovvir")
async def al_musovvir(message:
Message):
	await message.answer("<b>Al-Musovvir--المصور\n\nManosi: Maxluqot va mavjudotlarga suvrat va shakl beruvchi.</b>")
	
@dp.message_handler(text="Al-Gʻoffār")
async def al_goffar(message:
Message):
	await message.answer("<b>Al-Gʻoffār--آل الغفار\n\nManosi: Gʻaffor — Koʻplab magʻfirat qilib, bandalarning aybini oʻz fazli ila kechib yuboruvchi. bandalarning aybu nuqsonlari va gunohu ma'siyatlarini fosh qilmay yopib turuvchi.</b>")
	
@dp.message_handler(text="Al-Qohhār")
async def al_qohhar(message:
Message):
	await message.answer("<b>Al-Qohhār--القهار\n\nManosi: Qahhor — Barcha maxluqotlarni qabzasida tutib, ularni oʻz hukmiga yuritib va qudrati ila boʻysundirib turuvchi.</b>")
	
@dp.message_handler(text="Al-Vahhāb")
async def al_vahhab(message:
Message):
	await message.answer("<b>Al-Vahhāb--الوهاب\n\nManosi: Oʻz ne'matlarini tekin ato etuvchi.</b>")
	
@dp.message_handler(text="Ar-Rozzāq")
async def al_rozzaq(message:
Message):
	await message.answer("<b>Ar-Rozzāq--الرزاق\n\nManosi: Barcha tirik mavjudot rizqini yetkazib beruvchi.</b>")
	
@dp.message_handler(text="Al-Fattāh")
async def al_fattah(message:
Message):
	await message.answer("<b>Al-Fattāh--الفتاح\n\nManosi: Hukm etuvchi, rahmat hazinalarini ochuvchi.</b>")
	
@dp.message_handler(text="Al-'Alīm")
async def al_alim(message:
Message):
	await message.answer("<b>Al-'Alīm--العليم\n\nManosi: Biluvchi, dono, ilm sohibi. Boʻlgan va boʻladigan, avvalgi va oxirgi, zohir va botin narsalarning barchasini biluvchi.</b>")
	
@dp.message_handler(text="Al-Qobiz")
async def al_qobiz(message:
Message):
	await message.answer("<b>Al-Qobiz--القابض\n\nManosi: Kimlarningdir rizqini qiyuvchi, ruhlarni qabz etuvchi (oluvchi).</b>")
	
@dp.message_handler(text="Al-Bāsit")
async def al_basit(message:
Message):
	await message.answer("<b>Al-Bāsit--الباسط\n\nManosi: Kimlargadir keng rizq beruvchi, ruh baxsh etuvchi.</b>")
	
@dp.message_handler(text="Al-Hofiz")
async def al_hofiz(message:
Message):
	await message.answer("<b>Al-Hofiz--الخافض\n\nManosi: Kofirlar martabasini tushiruvchi.</b>")
	
@dp.message_handler(text="Ar-Rāfi")
async def al_rafi(message:
Message):
	await message.answer("<b>Ar-Rāfi'--الرافع\n\nManosi: Moʻminlar martabasini koʻtaruvchi.</b>")
	
@dp.message_handler(text="Al-Mu’izz")
async def al_muizz(message:
Message):
	await message.answer("<b>Al-Mu’izz--المعز\n\nManosi: Kimlarnidir aziz, qadrli etuvchi.</b>")
	
@dp.message_handler(text="Al-Muzill")
async def al_muzill(message:
Message):
	await message.answer("<b>Al-Muzill--المذل\n\nManosi: Kimlarnidur xoru zalil qiluvchi.</b>")
	
@dp.message_handler(text="As-Samī")
async def al_sami(message:
Message):
	await message.answer("<b>As-Samī--السميع\n\nManosi: Maxfiy va oshkora gap va sharpalarni, xatto dildan oʻtganini ham, eshituvchi.</b>")
	
@dp.message_handler(text="Al-Basīr")
async def al_basir(message:
Message):
	await message.answer("<b>Al-Basīr--البصير\n\nManosi: Hamma maxfiy va oshkora narsalarni koʻruvchi.</b>")
	
@dp.message_handler(text="Al-Hakam")
async def al_hakam(message:
Message):
	await message.answer("<b>Al-Hakam--الحكم\n\nManosi: Qat'iy hukm etuvchi</b>")
	
@dp.message_handler(text="Al-Adl")
async def al_adl(message:
Message):
	await message.answer("<b>Al-Adl--العدل\n\nManosi: Oʻta adolatli.</b>")
	
@dp.message_handler(text="Al-Latīf")
async def al_latif(message:
Message):
	await message.answer("<b>Al-Latīf--اللطيف\n\nManosi: Bandalariga sezdirmay oʻz lutfu ehsonini yetkasizb beruvchi.</b>")
	
@dp.message_handler(text="Al-Hobīr")
async def al_hobir(message:
Message):
	await message.answer("<b>Al-Hobīr--الخبير\n\nManosi: Hamma maxfiy va oshkora ishlardan xabardor</b>")
	
@dp.message_handler(text="Al-Halīm")
async def al_halim(message:
Message):
	await message.answer("<b>Al-Halīm--الحليم\n\nManosi: Jazolashga shoshmaydigan, hilm bilan yaxshilik qilib turuvchi.</b>")
	
@dp.message_handler(text="Al-'Azīm")
async def al_azim(message:
Message):
	await message.answer("<b>Al-'Azīm--العظيم\n\nManosi: Azamatli va ulugʻ zot. Aql tasavvur qila olmaydigan darajada azamatli va ulugʻ.</b>")
	
@dp.message_handler(text="Al-Gʻofūr")
async def al_gofur(message:
Message):
	await message.answer("<b>Al-Gʻofūr--الغفور\n\nManosi: Koʻp magʻfirat qiluvchi.</b>")
	
@dp.message_handler(text="Ash-Shakūr")
async def al_shakur(message:
Message):
	await message.answer("<b>Ash-Shakūr--الشكور\n\nManosi: Oʻz amaliga koʻp savob beruvchi.</b>")
	
@dp.message_handler(text="Al-'Aliyy")
async def al_aliyy(message:
Message):
	await message.answer("<b>Al-'Aliyy--العلي\n\nManosi: Martabasi oliylikda benihoya.</b>")
	
@dp.message_handler(text="Al-Kabīr")
async def al_kabir(message:
Message):
	await message.answer("<b>Al-Kabīr--الكبير\n\nManosi: Hammadan ulugʻ.</b>")
	
@dp.message_handler(text="Al-Hafīz")
async def al_hafiz(message:
Message):
	await message.answer("<b>Al-Hafīz--الحفيظ\n\nManosi: Har bir narsani komil muhofaza qiluvchi</b>")
	
@dp.message_handler(text="Al-Muqīt")
async def al_muqit(message:
Message):
	await message.answer("<b>Al-Muqīt--المقيت\n\nManosi: Barcha moddiy va ruhiy rizqlarni yaratuvchi.</b>")
	
@dp.message_handler(text="An-Hasīb")
async def an_hasib(message:
Message):
	await message.answer("<b>An-Hasīb--الحسيب\n\nManosi: Hisob qiluvchi, kifoya qiluvchi.</b>")
	
@dp.message_handler(text="Al-Jalīl")
async def al_jalil(message:
Message):
	await message.answer("<b>Al-Jalīl--الجليل\n\nManosi: Sifatlarida ulugʻlikka ega.</b>")
	
@dp.message_handler(text="Al-Karīm")
async def al_karim(message:
Message):
	await message.answer("<b>Al-Karīm--الكريم\n\nManosi: Saxovatli va karami keng. Birov soʻramasa ham, hech bir evaz olmasdan, narsalarni ato qiluvchi. Qarama-qarshilikdan pok. Karamli ishlar va xislatlar sohibi.</b>")
	
@dp.message_handler(text="Ar-Roqīb")
async def ar_roqib(message:
Message):
	await message.answer("<b>Ar-Roqīb--الرقيب\n\nManosi: Doimo kuzatib turuvchi. Raqiyb — hech bir zararni ham qoʻymay tekshirib turuvchi.</b>")
	
@dp.message_handler(text="Al-Mujīb")
async def al_mujib(message:
Message):
	await message.answer("<b>Al-Mujīb--المجيب\n\nManosi: Duolarni ijobat qiluvchi.</b>")
	
@dp.message_handler(text="Al-Vāsi")
async def al_vasi(message:
Message):
	await message.answer("<b>Al-Vāsi'--الواسع\n\nManosi: Keng va keng qamrovli zotdir</b>")
	
@dp.message_handler(text="Al-Hakīm")
async def al_hakim(message:
Message):
	await message.answer("<b>Al-Hakīm--الحكيم\n\nManosi: Dono</b>")
	
@dp.message_handler(text="Al-Vadūd")
async def al_vadud(message:
Message):
	await message.answer("<b>Al-Vadūd--الودود\n\nManosi: Bandalarini sevuvchi</b>")
	
@dp.message_handler(text="Al-Majīd")
async def al_majid(message:
Message):
	await message.answer("<b>Al-Majīd--المجيد\n\nManosi: Eng ulugʻvor</b>")
	
@dp.message_handler(text="Al-Bā'is")
async def al_bais(message:
Message):
	await message.answer("<b>Al-Bā'is--الباعث\n\nManosi: Oʻliklarning tiriltiruvchisi</b>")
	
@dp.message_handler(text="Ash-Shahīd")
async def Ash_shahid(message:
Message):
	await message.answer("<b>Ash-Shahīd--الشهيد\n\nManosi: Har bir narsaga hoziru nozir. Barchaga shohidlik beruvchi.</b>")
	
@dp.message_handler(text="Al-Haqq")
async def al_haqq(message:
Message):
	await message.answer("<b>Al-Haqq--الحق\n\nManosi: Oʻzgarmas sobit zot. Haqni yuzaga chiqaruvchi zot.</b>")
	
@dp.message_handler(text="Al-Vakīl")
async def al_vakil(message:
Message):
	await message.answer("<b>Al-Vakīl--الوكيل\n\nManosi: Barchaning ishi unga topshirilgan zot.</b>")
	
@dp.message_handler(text="Al-Qovviyy")
async def al_qovviyy(message:
Message):
	await message.answer("<b>Al-Qovviyy--القوى\n\nManosi: Quvvatli zot.</b>")
	
@dp.message_handler(text="Al-Matīn")
async def al_matin(message:
Message):
	await message.answer("<b>Al-Matīn--المتين\n\nManosi: Matonatli zot.</b>")
	
@dp.message_handler(text="Al-Valiyy")
async def al_valiyy(message:
Message):
	await message.answer("<b>Al-Valiyy--الولى\n\nManosi: Himoya qiluvchi doʻst, homiy va yordamchi</b>")
	
@dp.message_handler(text="Al-Hamīd")
async def al_hamid(message:
Message):
	await message.answer("<b>Al-Hamīd--الحميد\n\nManosi: Barcha maqtovlar ila maqtalgan zot.</b>")
	
@dp.message_handler(text="Al-Muhsi")
async def al_muhsi(message:
Message):
	await message.answer("<b>Al-Muhsi--المحصى\n\nManosi: Barcha narsaning hisobini olgan zot</b>")
	
@dp.message_handler(text="Al-Mubdi")
async def al_mubdi(message:
Message):
	await message.answer("<b>Al-Mubdi'--المبدئ\n\nManosi: Barcha narsalarni avval boshdan bor qilgan zot.</b>")
	
@dp.message_handler(text="Al-Mu'īd")
async def al_muid(message:
Message):
	await message.answer("<b>Al-Mu'īd--المعيد\n\nManosi: Yoʻq boʻlgan narsalarni yana qaytadan bor qiluvchi.</b>")
	
@dp.message_handler(text="Al-Muhyi")
async def al_muhyi(message:
Message):
	await message.answer("<b>Al-Muhyi--المحيى\n\nManosi: Tiriltiruvchi. U zot oʻliklarni tiriltiruvchidir va bu ismga ularni tiriltirishdan oldin sazovordir. Uni ularni oʻlik boʻlganlaridan keyin jon kiritib tirik qilganidan keyin tiriltiruvchi, deb atalganidek, ularni xalq qilishdan oldin, ularga hayot berishidan oldin ham, tiriltiruvchi, deyilaveradi. Xuddi, xaloyiqni xalq qilishidan oldin Xoliq boʻlganidek.</b>")
	
@dp.message_handler(text="Al-Mumīt")
async def al_mumit(message:
Message):
	await message.answer("<b>Al-Mumīt--المميت\n\nManosi: Oʻldirivchi. Barcha jonzotlarning jonini oluvchi.</b>")
	
@dp.message_handler(text="Al-Hayy")
async def al_hayy(message:
Message):
	await message.answer("<b>Al-Hayy--الحي\n\nManosi: Tirik. U tirikdir, oʻlmas. Ya'ni, Allohning hayoti abadiydir, oʻlim ila yoʻq boʻlmas. Shuningdek, Allohning hayoti azaliydir, oldindan yoʻq boʻlgan emas.</b>")
	
@dp.message_handler(text="Al-Qoyyūm")
async def al_qoyyum(message:
Message):
	await message.answer("<b>Al-Qoyyūm--القيوم\n\nManosi: Oʻz oʻzidan qoim boʻlgan va boshqalarni qoim qilgan zot.</b>")
	
@dp.message_handler(text="Al-Vājid")
async def al_vajid(message:
Message):
	await message.answer("<b>Al-Vājid--الواجد\n\nManosi: Topuvchi. Xohlagan narsasini topuvchi. Bu ishda birov Uni toʻsa olmaydi.</b>")
	
@dp.message_handler(text="Al-Mājid")
async def al_majid(message:
Message):
	await message.answer("<b>Al-Mājid--الماجد\n\nManosi: Majdu sharaf sohibi boʻlgan zot.</b>")
	
@dp.message_handler(text="Al-Vāhid")
async def al_vahid(message:
Message):
	await message.answer("<b>Al-Vāhid--الواحد\n\nManosi: Yagona. Bita. Boʻlinmas. U zot oʻz zotida ham, sifatlarida ham va ishlarida ham birdir.</b>")
	
@dp.message_handler(text="As-Somad")
async def As_Somad(message:
Message):
	await message.answer("<b>As-Somad--الصمد\n\nManosi: Somad sifati koʻp ma'nolarni oʻz ichiga oladi:- itoat qilingan ulugʻ-Usiz hech bir ish bitmaydi.- hech kimga hojati tushmaydi, barchaning hojati Unga tushadi.- butun maxluqot bitib tugasa ham, Oʻzi doim boqiydir va hokazo.</b>")
	
@dp.message_handler(text="Al-Qodir")
async def al_qodir(message:
Message):
	await message.answer("<b>Al-Qodir--القادر\n\nManosi: Cheksiz qudrat sohibi. U zot har bir narsaga qodirdir. har bir ish unga osondir</b>")
	
@dp.message_handler(text="Al-Muqtadir")
async def al_muqtadir(message:
Message):
	await message.answer("<b>Al-Muqtadir--المقتدر\n\nManosi: Juda ham qudratli</b>")
	
@dp.message_handler(text="Al-Muqoddim")
async def Al_Muqoddim(message:
Message):
	await message.answer("<b>Al-Muqoddim--المقدم\n\nManosi: Oldinga suruvchi. U zot xohlagan shaxs va narsani xohlaganidan oldinga suradi.</b>")
	
@dp.message_handler(text="Al-Mu'ahhir")
async def al_muahhir(message:
Message):
	await message.answer("<b>Al-Mu’ahhir--المؤخر\n\nManosi: Orqaga suruvchi. U zot xohlagan shaxs va narsani xohlaganidan orqaga suradi.</b>")
	
@dp.message_handler(text="Al-'Avval")
async def al_avval(message:
Message):
	await message.answer("<b>Al-'Avval--الأول\n\nManosi: „Avval“ — U hamma narsadan avval, ya'ni, barcha mavjudotlar yoʻqligida Alloh bor edi. Mavjudotlarni „Avval“ sifatiga ega boʻlgan Alloh yaratdi. Ya'ni, Alloh vujudga kelishining boshlanishi yoʻqdir</b>")
	
@dp.message_handler(text="Al-'Ahir")
async def al_ahir(message:
Message):
	await message.answer("<b>Al-'Ahir--الأخر\n\nManosi: „Oxir“ — U hamma narsa yoʻq boʻlib ketganda ham Oʻzi qoladi.</b>")
	
@dp.message_handler(text="Az-Zohir")
async def az_zohir(message:
Message):
	await message.answer("<b>Az-Zohir--الظاهر\n\nManosi: „Zohir“ — Uning mavjudligi oshkor, ochiq-oydindir. U hamma narsadan zohir-ustundir.</b>")
	
@dp.message_handler(text="Al-Bātin")
async def al_batin(message:
Message):
	await message.answer("<b>Al-Bātin--الباطن\n\nManosi: Botin — U koʻzga koʻrinmaydi. Hammadan pinhon-maxfiy narsalarni bilib turuvchidir.</b>")
	
@dp.message_handler(text="Al-Vāli")
async def al_vali(message:
Message):
	await message.answer("<b>Al-Vāli--الوالي\n\nManosi: Har bir narsaga voliy — ega boʻlgan zot.</b>")
	
@dp.message_handler(text="Al-Mutā'ali")
async def al_mutaali(message:
Message):
	await message.answer("<b>Al-Mutā'ali--المتعالي\n\nManosi: Nuqsonlardan yuqori turuvchi zot.</b>")
	
@dp.message_handler(text="Al-Barr")
async def al_Barr(message:
Message):
	await message.answer("<b>Al-Barr--البر\n\nManosi: Ulugʻ yaxshilik qiluvchi.</b>")
	
@dp.message_handler(text="At-Tavvāb")
async def al_tavvab(message:
Message):
	await message.answer("<b>At-Tavvāb--التواب\n\nManosi: Bandalarni tavbaga yoʻllovchi va ularning tavbasini koʻplab qabul qiluvchi zot.</b>")
	
@dp.message_handler(text="Al-Muntaqim")
async def al_muntaqim(message:
Message):
	await message.answer("<b>Al-Muntaqim--المنتقم\n\nManosi: Zolim va osiylardan intiqom oluvchi.</b>")
	
@dp.message_handler(text="Al-Afuvv")
async def al_afuvv(message:
Message):
	await message.answer("<b>Al-Afuvv--العفو\n\nManosi: Afv qiluvchi.</b>")
	
@dp.message_handler(text="Ar-Roʻūf")
async def al_rouf(message:
Message):
	await message.answer("<b>Ar-Roʻūf--الرؤوف\n\nManosi: Oʻta shafqatli va mehribon.</b>")
	
@dp.message_handler(text="Mālik-ul-Mulik")
async def allahismio(message:
Message):
	await message.answer("<b>Mālik-ul-Mulk--مالك الملك\n\nManosi: Mulk egasi. Bu dunyodagi ishlarni oʻzi xohlaganicha qiladi. Uning qazosini qaytaradigan va hukmini oʻzgartiradigan yoʻq.</b>")
	
@dp.message_handler(text="Zūl-Jalāli-Val'ikrom")
async def allahismi(message:
Message):
	await message.answer("<b>Zūl-Jalāli val’ikrom--ذو الجلال والإكرام\n\nManosi: Sharaf va kamol egasi. Karam va ikrom egasi.</b>")
	
@dp.message_handler(text="Al-Muqsiţ")
async def al_muqsit(message:
Message):
	await message.answer("<b>Al-Muqsiţ--المقسط\n\nManosi: Oʻz adolati ila mazlumlarga nusrat va zolimlarga jazo beruvchi.</b>")
	
@dp.message_handler(text="Al-Jāmi")
async def al_jami(message:
Message):
	await message.answer("<b>Al-Jāmi--الجامع\n\nManosi: Jamlovchi. Barcha haqiqatlarni jamlovchi. Odamlarni qiyomat kuni jamlovchi.</b>")
	
@dp.message_handler(text="Al-Gʻoni")
async def al_goni(message:
Message):
	await message.answer("<b>Al-Gʻoni--الغني\n\nManosi: Behojat. Uning hech kim va hech narsaga hojati tushmaydi.</b>")
	
@dp.message_handler(text="Al-Mugʻni")
async def al_mugni(message:
Message):
	await message.answer("<b>Al-Mugʻni--المغني\n\nManosi: Behojat qiluvchi. U zot Oʻz bandalaridan qay birini xohlasa behojat qilib qoʻyadi.</b>")
	
@dp.message_handler(text="Al-Māni")
async def al_mani(message:
Message):
	await message.answer("<b>Al-Māni'--المانع\n\nManosi: Man qiluvchi.</b>")
	
@dp.message_handler(text="Az-Zorr")
async def al_az_zorr(message:
Message):
	await message.answer("<b>Az-Zorr--الضار\n\nManosi: Zarar qiluvchi. Zararli narsalarni ham yaratuvchi.</b>")
	
@dp.message_handler(text="An-Nāfi")
async def al_an_nafi(message:
Message):
	await message.answer("<b>An-Nāfi--النافع\n\nManosi: Manfaat beruvchi.</b>")
	
@dp.message_handler(text="An-Nūr")
async def al_nur(message:
Message):
	await message.answer("<b>An-Nūr--النور\n\nManosi: Oʻz-oʻzi ila zohir boʻlgan va oʻzgalarni zohir qilgan.</b>")
	
@dp.message_handler(text="Al-Hādi")
async def al_hadi(message:
Message):
	await message.answer("<b>Al-Hādi--الهادي\n\nManosi: Hidoyat qiluvchi. U zot Oʻz fazli ila xohlagan kimsani hidoyat qiladi. Ya'ni, Alloh kimni toʻgʻri yoʻlga hidoyat qilsa, albatta, Oʻz xohishi va fazli ila hidoyat qiladi.</b>")
	
@dp.message_handler(text="Al-Badī")
async def al_badi(message:
Message):
	await message.answer("<b>Al-Badī--البديع\n\nManosi: Oʻxshashi yoʻq narsalarni keltiruvchi.</b>")
	
@dp.message_handler(text="Al-Bāqi")
async def al_baqi(message:
Message):
	await message.answer("<b>Al-Bāqi--الباقي\n\nManosi: Boqiy qoluvchi. U doimiy bordir, unga foniylik oriz boʻlmas.</b>")
	
@dp.message_handler(text="Al-Vāris")
async def al_varis(message:
Message):
	await message.answer("<b>Al-Vāris--الوارث\n\nManosi: Muvjudotlar yoʻq boʻlganda ham boqiy qoluvchi zot.</b>")
	
@dp.message_handler(text="Ar-Roshīd")
async def al_roshid(message:
Message):
	await message.answer("<b>Ar-Roshīd--الرشيد\n\nManosi: Toʻgʻri yoʻlga irshod qiluvchi.</b>")
	
@dp.message_handler(text="As-Sobur")
async def As_Sobur(message:
Message):
	await message.answer("<b>As-Sobur--الصبور\n\nManosi: Oʻta sabrli. Osiylarni azoblashga shoshilmaydi.</b>")