from tabulate import tabulate
from datetime import date, datetime, timedelta
from time import sleep

# ===============================================================
# Fungsi Menu Utama
def main_menu() :
    print("\n=================================")
    print("WELCOME TO OHMYNYO'S MINI LIBRARY")
    print("=================================")
    print("What do you want to do?")
    print("1. Check Novel List")
    print("2. Add New Novel List")
    print("3. Update Novel List")
    print("4. Delete Novel From The List")
    print("5. Borrow A Novel")
    print("6. Check Membership")
    print("7. I don't want to do anything")
    print("=================================")

# ===============================================================
# List Novel
novel = [
    ["F01", "Funiculi Funicula", "Toshikazu Kawaguchi", "Fantasy", 2015, 4],
    ["F02", "Harry Potter And The Prisoner Of Azkaban", "J. K. Rowling", "Fantasy", 1999, 7],
    ["F03", "The Curse Of Imperfection", "Ohmynyo", "Fantasy", 2024, 0],
    ["H01", "Laut Bercerita", "Leila S. Chudori", "Historical Fiction", 2017, 8],
    ["M01", "One Of Us Is Lying", "Karen M. McManus", "Mystery", 2017, 6],
    ["M02", "The Devotion Of Suspect X", "Keigo Higashino", "Mystery", 2017, 5],
    ["R01", "As A Spark Goes Wild", "Ohmynyo", "Romance", 2022, 10],
    ["T01", "Nowhere To Hide", "Ohmynyo", "Thriller", 2021, 1],
    ["T02", "One New Message", "Ohmynyo", "Thriller", 2023, 3],
    ["T03", "The Silent Patient", "Alex Michaelides", "Thriller", 2019, 9]
]

header = ["Code", "Title", "Author", "Genre", "Year", "Availability"]

def show_novel():
    print(tabulate(novel, headers = header, tablefmt = "fancy_grid"))

# ===============================================================
# Membership
member = [
    ["MM001", "Deva Marine", 29, date(2025, 1, 28), "Active"],
    ["MM002", "Cahyo Wicaksono", 25, date(2023, 12, 12), "Expired"],
    ["MM003", "Adinda Rahmah", 27, date(2024, 3, 12), "Active"]
]

header_member = ["ID", "Name", "Age", "Date Expired", "Status"]

def show_member():
    print(tabulate(member, headers = header_member, tablefmt = "fancy_grid"))

# ===============================================================
# Novel yang dipinjam
borrower_list = [
    ["MM003", "Adinda Rahmah", "As A Spark Goes Wild", date(2021, 6, 15), date(2021, 6, 28)],
    ["MM002", "Cahyo Wicaksono", "Harry Potter And The Prisoner Of Azkaban", date(2022, 11, 2), date(2022, 11, 29)],
    ["MM003", "Adinda Rahmah", "Nowhere To Hide", date(2023, 2, 20), date(2023, 3, 1)],
    ["MM001", "Deva Marine", "One Of Us Is Lying", date(2023, 9, 6), date(2023, 9, 27)],
    ["MM003", "Adinda Rahmah", "One New Message", date(2023, 12, 11), date(2023, 12, 31)],
    ["MM001", "Deva Marine", "Nowhere To Hide", date(2024, 2, 14), ""],
    ["MM003", "Adinda Rahmah", "The Curse of Imperfection", date(2024, 2, 27), ""]
]

header_borrower = ["ID", "Name", "Title", "Loan Date", "Return Date/Must Be Return Date"]

def show_borrower():
    print(tabulate(borrower_list[:], headers = header_borrower, tablefmt = "fancy_grid"))

# ===============================================================
# Sinopsis novel
synopsis = [
    ["F01", "\tKafe tua yang berada di gang kecil Tokyo terletak di bawah gedung lain, tidak butuh pendingin untuk mendinginkan Kafe tersebut. Tidak begitu ramai, namun terkenal karena bisa membawa pengunjungnya menjelajahi waktu. Keajaiban kafe itu menarik seorang wanita yang ingin memutar waktu untuk berbaikan dengan kekasihnya, seorang perawat yang ingin membaca surat yang tak sempat diberikan suaminya yang sakit, seorang kakak yang ingin menemui adiknya untuk terakhir kali, dan seorang ibu yang ingin bertemu dengan anak yang mungkin takkan pernah dikenalnya. Namun ada banyak peraturan yang harus diingat. Satu, mereka harus tetap duduk di kursi yang telah ditentukan. Dua, apapun yang mereka lakukan di masa yang didatangi takkan mengubah kenyataan di masa kini. Tiga, mereka harus menghabiskan kopi khusus yang disajikan sebelum kopi itu dingin. Rentetan peraturan lainnya tak menghentikan orang-orang itu untuk menjelajahi waktu. Akan tetapi, jika kepergian mereka tak mengubah satu hal pun di masa kini, layakkah semua itu dijalani?"],
    ["F02", "\tKetika Bus Ksatria membelah kegelapan malam dan berhenti mendadak di hadapan Harry Potter, maka dimulailah tahun ajaran berikutnya di Hogwarts yang jauh dari biasa-biasa saja. \n\tSirius Black, pembunuh massal dan pengikut Lord Voldemort, kabur dari penjara Azkaban— dan konon dia memburu Harry. \n\tPada pelajaran Ramalan pertama, Profesor Trelawney melihat terawangan kematian dalam ampas teh anak itu...\n\tNamun, tak ada yang lebih menakutkan daripada para Dementor, sosok-sosok pengisap jiwa, yang gentayangan di sekeliling sekolah."],
    ["F03", "\tPada suatu hari, di suatu dunia yang berbeda dimana hidup berbagai macam makhluk astral, lahirlah dua bayi kembar berdarah campuran manusia. \n\t'Ketidaksempurnaan' ini dilihat oleh seseorang sebagai sebuah kesempatan untuk mendapatkan kekuatan absolut. Sebagian kekuatan pun telah berhasil diperoleh olehnya. \n\tSejak saat itu, dua makluk kembar berdarah campuran telah memutuskan untuk membalas apa yang telah diperbuat oleh seseorang yang mereka panggil 'ayah'."],
    ["H01", "\tLaut Bercerita bertutur tentang kisah keluarga yang kehilangan, sekumpulan sahabat yang merasakan kekosongan di dada, sekelompok orang yang gemar menyiksa dan lancar berkhianat, sejumlah keluarga yang mencari kejelasan makam anaknya, dan tentang cinta yang tak akan luntur."],
    ["M01", "\tSenin sore, lima murid memasuki ruang detensi. Bronwyn, si genius, nilai akademis sempurna dan tidak pernah melanggar peraturan. Addy, si cewek populer, gambaran sempurna pemenang kontes kecantikan. Nate, si bandel, dalam masa percobaan karena transaksi narkoba. Cooper, si atlet, pelempar bola andalan tim bisbol dan pangeran di hati semua orang. Dan Simon, si orang buangan, pencipta aplikasi gosip terdepan mengenai kehidupan Bayview High. Namun sebelum detensi berakhir, Simon tewas. Menurut para penyidik, kematiannya disengaja. Apalagi kemudian ditemukan draft artikel gosip terbaru untuk ditayangkan pada Selasa, sehari setelah kematian Simon. Gosip heboh tentang empat orang yang berada dalam ruangan detensi bersamanya. Mereka berempat dicurigai, dan semuanya punya rahasia terpendam. Salah satu di antara mereka pasti ada yang berbohong."],
    ["M02", "\tKetika si mantan suami muncul lagi untuk memeras Yasuko Hanaoka dan putrinya, keadaan menjadi tak terkendali, hingga si mantan suami terbujur kaku di lantai apartemen. Yasuko berniat menghubungi polisi, tetapi mengurungkan niatnya ketika Ishigami, tetangganya, menawarkan bantuan untuk menyembunyikan mayat itu. \n\tSaat mayat tersebut ditemukan, penyidikan Detektif Kusanagi mengarah kepada Yasuko. Namun sekuat apa pun insting detektifnya, alibi wanita itu sulit sekali dipatahkan. Kusanagi berkonsultasi dengan sahabatnya, Dr. Manabu Yukawa sang Profesor Galileo, yang ternyata teman kuliah Ishigami. \n\tDiselingi nostalgia masa-masa kuliah, Yukawa sang pakar fisika beradu kecerdasan dengan Ishigami, sang genius matematika. Ishigami berjuang melindungi Yasuko dengan berusaha mengakali dan memperdaya Yukawa, yang baru kali ini menemukan lawan paling cerdas dan bertekad baja."],
    ["R01", '\tThe fireworks festival is being held to welcome New Year’s Eve. People are over-enthusiastic, but not everyone shares the excitement. Here lies, myself, who still struggling inside my own void, seeking a brief flash of light. \n\n"As a spark on those fireworks that goes wild, my feeling towards you do the same."'],
    ["T01", "\tRasendriya adalah seorang agen rahasia yang bekerja di bawah naungan sebuah agensi. Selama sepuluh tahun berkarir, ia telah menjalani begitu banyak misi dan hampir selalu dapat menyelesaikannya dengan hasil yang memuaskan. Ya, ia merupakan agen papan atas dengan prestasi yang cemerlang. Tidak ada yang tidak dapat ia lakukan. Ia sangat mahir dalam segalanya, terutama... menghabisi targetnya. \n\tNamun, kali ini Rasendriya dihadapkan oleh misi yang berbeda. Ia diharuskan berpura-pura menjadi seorang mahasiswa di suatu kampus untuk mendapatkan informasi mengenai seseorang yang 'hanya' mahasiswi biasa. Siapakah mahasiswi tersebut hingga Rasendriya yang notabene adalah agen rahasia harus turun tangan?"],
    ["T02", "\tSelayaknya mahasiswa lainnya, hidupku terasa membosankan. Kegiatanku hanya menghadiri kelas, bermain game bersama gengku, dan sesekali harus menghadapi dosen mata keranjang yang mencoba menggodaku. \n\tSetidaknya seperti itulah kehidupanku……sampai hari itu tiba. \n\tAku menemukan sebuah ponsel tergeletak tak bertuan. Keusilan serta rasa penasaran pun membuatku gelap mata. Tanpa berpikir panjang, aku segera mengambil ponsel tersebut dan menunjukkannya pada teman-temanku dengan niat bercanda. \n\tNamun, sang pemilik ponsel tiba-tiba mengirimkan pesan dengan mengatakan bahwa ia mengetahui masa laluku. Sebuah pesan yang akhirnya membuatku menyesali semuanya. Dan ketika sadar kesalahan yang telah aku perbuat, semuanya sudah terlambat."],
    ["T03", "\tSepasangan suami istri, Alicia Berenson dan Gabriel Berenson tinggal di sebuah rumah besar yang memiliki jendela besar, yang menghadap ke taman di salah satu daerah yang paling diminati di London. Alicia Berenson yang merupakan pelukis terkenal menikahi Gabriel Berenson yang merupakan seorang fotografer. Suatu malam, Gabriel bekerja lembur. Ia pulang terlambat dari sebuah pemotretan mode. Di malam itu, sesaat setelah Gabriel pulang, terdengar suara tembakan dari rumah Alicia dan Gabriel. Polisi menemukan jasad Gabriel yang sudah tidak bernyawa, dengan posisi diikat ke kursi, dan luka tembak sebanyak lima buah. \n\tSenjata yang menjadi alat pembunuh Gabriel tergeletak di lantai. Alicia berdiri di samping tubuh Gabriel, terdiam mematung, tidak mengeluarkan sepatah kata pun. Alicia sejak saat itu membisu. Ia tak menjawab pertanyaan satu pun. Ia tetap diam ketika dituduh membunuh Gabriel. Alicia tetap bungkam sewaktu ditahan, tidak menyangkal atau mengaku. Ia tak pernah bicara lagi. Alicia tetap membisu - tapi menyatakan satu hal. Dengan lukisan berupa potret diri. Ia memberikan judul lukisan tersebut di sudut kiri bawah kanvas, dengan huruf-huruf Yunani biru terang yang membentuk satu kata: ALCESTIS."]
]

# Fungsi looping sinopsis (DONE)
def loop_synopsis() :
    input_synopsis = input("\nDo you wish to read the synopsis? (Y/N) ").capitalize()
    if input_synopsis == "Y" or input_synopsis == "YES" :
        print("\tYES, PLEASEEEE\n")
        print("Which one do you like to read?")
        input_read_synopsis = input("Please, input the code only : ").capitalize()
        for i in range(len(synopsis)) : 
            if synopsis[i][0] == input_read_synopsis :
                print(f"\n\n\t\t\t\t============ {novel[i][1]} ============")
                print("\nSinopsis:")
                print(synopsis[i][1])
                print("\nDo you like it?")
                input_borrow_syn = input("Do you want to borrow this novel? (Y/N) : ").capitalize()
                if input_borrow_syn == "Y" or input_borrow_syn == "YES" :
                    print("\tPlease wait a second. We will moving you to 'Borrow's Menu'")
                    sleep(3)
                    menu_borrow()
                    return menu_borrow()
                elif input_borrow_syn == "N" or input_borrow_syn == "NO" :
                    print("\tPerhaps your taste is not that good...")
                    sleep(3)
                else : 
                    print("\tYour input is invalid. Please try again.")
                return loop_synopsis()
            elif synopsis[i] == synopsis[-1] :
                print("\tYour input is invalid. Please try again.")
                return loop_synopsis()
    elif input_synopsis == "N" or input_synopsis == "NO" :
        print("\tIt's sad to think my novel didn't pick your interest.")
        sleep(3)
        return
    else :
        print("\tYour input is invalid. Please try again.")
    return loop_synopsis()

# ===============================================================
# Popularity

popularity = [
    ["F01", "Funiculi Funicula", "Toshikazu Kawaguchi", "Fantasy", 2015, 23],
    ["F02", "Harry Potter And The Prisoner Of Azkaban", "J. K. Rowling", "Fantasy", 1999, 85],
    ["F03", "The Curse Of Imperfection", "Ohmynyo", "Fantasy", 2024, 74],
    ["H01", "Laut Bercerita", "Leila S. Chudori", "Historical Fiction", 2017, 92],
    ["M01", "One Of Us Is Lying", "Karen M. McManus", "Mystery", 2017, 63],
    ["M02", "The Devotion Of Suspect X", "Keigo Higashino", "Mystery", 2017, 51],
    ["R01", "As A Spark Goes Wild", "Ohmynyo", "Romance", 2022, 19],
    ["T01", "Nowhere To Hide", "Ohmynyo", "Thriller", 2021, 106],
    ["T02", "One New Message", "Ohmynyo", "Thriller", 2023, 77],
    ["T03", "The Silent Patient", "Alex Michaelides", "Thriller", 2019, 89]
]

header_pop = ["Code", "Title", "Author", "Genre", "Year", "Popularity (times borrowed)"]
popularity_list = sorted(popularity, key=lambda x: x[5])

def most_popular() :    
    print("\n =============================== MOST POPULAR ================================")
    print(tabulate(popularity_list[-1:], headers = header_pop, tablefmt = "fancy_grid"))
    print("\n\t\tYOU ABSOLUTELY HAVE TO READ THIS!!!")
    sleep(3)

# ===============================================================
# CHECK/READ 
# ===============================================================
# Menu dari check novel list
def check_novel() :
    print("\n========== NOVEL LIST ==========\n")
    print("Choose the options below :")
    print("1. All novel list")
    print("2. Search by code")
    print("3. Search by title")
    print("4. Search by author")
    print("5. Search by genre")
    print("6. List by popularity")
    print("7. Back to Main Menu")
    return

# Fungsi untuk search kode (DONE)
def search_code() :
    input_code = input("\nEnter novel's code : ").capitalize()
    for i in range(len(novel)) : 
        if novel[i][0] == input_code :  # input in novel[i][]
            print(tabulate(novel[i:i+1], headers = header, tablefmt = "fancy_grid"))
            loop_synopsis()
            input_continue_code = input("\nDo you want to search another code? (Y/N) : ").capitalize()
            if input_continue_code == "Y" or input_continue_code == "YES" :
                return search_code()
            elif input_continue_code == "N" or input_continue_code == "NO" :
                break
            else :
                print("\tYour input is incorrect. Please try again.")
                sleep(2)
                return search_code()
        elif novel[i] == novel[-1] : 
            print("\tThe code is not found. Please try again.")
            sleep(2)
            return search_code()
        
# Fungsi untuk search title (DONE)
def search_title() :
    input_title = input("\nEnter novel's title : ").title()
    for i in range(len(novel)) : 
        if novel[i][1] == input_title :  
            print(tabulate(novel[i:i+1], headers = header, tablefmt = "fancy_grid"))
            loop_synopsis()
            input_continue_title = input("\nDo you want to search another title? (Y/N) : ").capitalize()
            if input_continue_title == "Y" or input_continue_title == "YES" :
                return search_title()
            elif input_continue_title == "N" or input_continue_title == "NO" :
                break
            else :
                print("\tYour input is incorrect.")
                sleep(2)
                return search_title()
        elif novel[i] == novel[-1] : 
            print("\tThe title is not found. Please try again.")
            sleep(2)
            return search_title()

# Fungsi untuk search author (DONE)
def search_author() :
    author_list = []
    input_author = input("\nEnter novel's author : ").title()
    for i in range(len(novel)) :
        list_author_name = novel[i][2].split() 
        if input_author in list_author_name :  
            author_list.append(novel[i:i+1][0])
            continue
    if author_list == [] :
        print("\tThe author is not found. Please try again.")
        sleep(2)
        return search_author()    
    elif author_list != [] : 
        print(tabulate(author_list, headers = header, tablefmt = "fancy_grid"))
        loop_synopsis()
        input_continue_author = input("\nDo you want to search another author? (Y/N) : ").capitalize()
        for i in input_continue_author : 
            if i == "Y" or i == "YES" :
                return search_author()
            elif i == "N" or i == "NO" :
                break
            else :
                print("\tYour input is incorrect. Please try again")
                return search_author()

# Fungsi untuk search genre (DONE)
def search_genre() : 
    genre_list = []
    input_genre = input("\nEnter novel's genre : ").title()
    for i in range(len(novel)) : 
        if novel[i][3] == input_genre :
            genre_list.append(novel[i:i+1][0])
            continue
    if genre_list == [] :
        print("\tThe genre is not found. Please try again.")
        sleep(2)
        return search_genre()    
    elif genre_list != [] : 
        print(tabulate(genre_list, headers = header, tablefmt = "fancy_grid"))
        loop_synopsis()
        input_continue_genre = input("\nDo you want to search another genre? (Y/N) : ").capitalize()
        for i in input_continue_genre : 
            if i == "Y" or i == "YES" :
                return search_genre()
            elif i == "N" or i == "NO" :
                break
            else :
                print("\tYour input is incorrect. Please try again")
                sleep(2)
                return search_genre()

# Fungsi untuk melihat popularity
def search_popularity() :
    print("\n========== LIST BY POPULARITY ==========\n")
    print("Choose the options below :")
    print("1. Popularity list")
    print("2. Most Popular")
    print("3. Back to previous menu")
    
    input_popularity = input("\nPlease, enter your choice between 1-3 : ")
    if input_popularity == "1" :
        print(tabulate(popularity_list, headers = header_pop, tablefmt = "fancy_grid"))
        sleep(3)
        return search_popularity()
    elif input_popularity == "2" :
        most_popular()
        sleep(3)
        return search_popularity()
    elif input_popularity == "3" :
        return loop_check_novel()
    else : 
        print("\tYour input is invalid. Please, repeat again.\n")
        sleep(2)
        return search_popularity()

# Fungsi untuk check novel
def loop_check_novel() :
    while True :
        check_novel()
        input_check_novel = input("\nPlease, enter your choice between 1-6 : ")
        if input_check_novel == "1" :
            show_novel()
            loop_synopsis()           
        elif input_check_novel == "2" :
            search_code()
        elif input_check_novel == "3" :
            search_title()
        elif input_check_novel == "4" :
            search_author()
        elif input_check_novel == "5" :
            search_genre()
        elif input_check_novel == "6" :
            search_popularity()
        elif input_check_novel == "7" :
            loop_main_menu()
        else : 
            print("\tYour input is invalid. Please, repeat again.\n")
            sleep(2)

# ===============================================================
# CREATE
# ===============================================================
# Menu dari add new novel list
def add_new() :
    print("\n========== ADD NEW NOVEL ==========\n")
    print("Choose the options below :")
    print("1. Add new novel to the list")
    print("2. Back to Main Menu")

# Loop add new novel
def loop_add_new_novel() :
    input_add_new_novel = input("\nEnter your choice between 1-2 : ")    
    if input_add_new_novel == "1" :
        input_code = input("\nEnter novel's code : ").capitalize()
        for i in range(len(novel)) :
            if novel[i][0] == input_code : 
                i += 1
                print("\nNovel with the code is already in the list.")
                print("Please, enter another one.")
                sleep(2)
                break
        else : 
            novel_title = input("Enter novel's title : ").title()
            novel_author = input("Enter author's name : ").title()
            novel_genre = input("Enter novel's genre : ").title()
            novel_year = input("Enter novel's year published : ")
            novel_stock = input("Enter novel's stock : ")
            novel_synopsis = input("\nEnter the synopsis : \n")

            new_novel = [input_code, novel_title, novel_author, novel_genre, novel_year, novel_stock]
            new_synopsis = [input_code, novel_synopsis]
            # print(new_novel)
            # for i in range(len(novel)) :
            # print(tabulate(new_novel[:-1], headers = header, tablefmt = "fancy_grid"))
            
            print("\nNew Novel's Information")
            print("=======================")
            print(f"Code \t\t: {input_code}")
            print(f"Title \t\t: {novel_title}")
            print(f"Author \t\t: {novel_author}")
            print(f"Genre \t\t: {novel_genre}")
            print(f"Year \t\t: {novel_year}")
            print(f"Availability \t: {novel_stock}")

            print(f"\n\n\t\t\t\t============ {novel_title} ============")
            print("\nSinopsis:")
            print(f"\t{novel_synopsis}")

            while True :
                input_confirmation = input("\nAre you sure to add this novel to the list? (Y/N) : ").capitalize()
                if input_confirmation == "Y" or input_confirmation == "YES" :
                    novel.append(new_novel)
                    synopsis.append(new_synopsis)
                    print("\nNovel successfully added to the list!\n")
                    sleep(2)
                    break
                elif input_confirmation =="N" or input_confirmation == "NO" :
                    print("\nNew novel is not added.\n")
                    sleep(2)
                    break
                else : 
                    print("\nYour input is incorrect.\n")
                    sleep(2)
                    continue
    elif input_add_new_novel == "2" :
        return loop_main_menu()

# ===============================================================
# UPDATE 
# ===============================================================
# Menu dari update novel list
def update_novel() :
    print("\n========== UPDATE NOVEL ==========\n")
    print("Choose the options below :")
    print("1. Update novel in the list")
    print("2. Back to Main Menu")

# Fungsi update novel ====NOT FINISHED YET
def loop_update() :
    input_update = input("\nEnter your choice between 1-2 : ")
    for update in input_update : 
        if update == "1" :
            print("")
            show_novel()
            input_code = input("Enter novel's code : ").capitalize()
            for i in range(len(novel)) :
                if novel[i][0] == input_code : 
                    print("\nInput new information (Leave empty if you don't want to change anything): ")
                    update_title = input(f"Enter new title for {novel[i][0]} '{novel[i][1]}' : ").title()
                    update_author = input(f"Enter new author for {novel[i][0]} '{novel[i][2]}' : ").title()  
                    update_genre = input(f"Enter new genre for {novel[i][0]} '{novel[i][3]}' : ").title()
                    update_year = input(f"Enter new year published for {novel[i][0]} '{novel[i][4]}' : ")
                    update_stock = input(f"Enter new availability for {novel[i][0]} '{novel[i][5]}' : ")
                    update_synopsis = input(f"Enter new synopsis for {novel[i][0]} : ")

                    input_confirmation = input("\nAre you sure to update this novel? (Y/N) : ").capitalize()
                    if input_confirmation == "Y" or input_confirmation == "YES" :
                        if update_title != "" : 
                            novel[i][1] = update_title
                        if update_author != "" :
                            novel[i][2] = update_author
                        if update_genre != "" :
                            novel[i][3] = update_genre
                        if update_year != "" :
                            novel[i][4] = update_year
                        if update_stock != "" :
                            novel[i][5] = update_stock
                        if update_synopsis != "" :
                            synopsis[i][1] = update_synopsis

                        novel[i][1] = update_title
                        novel[i][2] = update_author
                        novel[i][3] = update_genre
                        novel[i][4] = update_year
                        novel[i][5] = update_stock
                        synopsis[i][1] = update_synopsis

                        print(tabulate(novel, headers = header, tablefmt = "fancy_grid"))
                        print("\n\tNovel successfully updated!\n")
                        sleep(2)
                        break
                    else : 
                        print("\tNovel is not updated.\n")
                        sleep(2)
                        break

        elif update == "2" : 
            break
        else :
            print("\tYour input is invalid. Please try again")
            sleep(2)
            return loop_update()

# ===============================================================
# DELETE
# ===============================================================
# Menu menghapus novel
def delete_novel() :
    print("\n========== DELETE NOVEL ==========\n")
    print("Choose the options below :")
    print("1. Delete specific novel from the list")
    print("2. Delete all novel from the list")
    print("3. Back to Main Menu")

# Fungsi delete (DONE)
def loop_delete() :
    input_delete = input("\nEnter your choice between 1-3 : ")
    if input_delete == "1" :
        show_novel()
        input_code_delete = input("\nEnter novel's code to be deleted : ").capitalize()
        for i in range(len(novel)) :
            if novel[i][0] == input_code_delete :
                print(tabulate(novel[i:i+1], headers = header, tablefmt = "fancy_grid"))
                delete_confirmation = input("Are you sure to delete this one? (Y/N) : ").capitalize()
                if delete_confirmation == "Y" or delete_confirmation == "YES" :
                    print("\tHope you did not regret that...")
                    sleep(3)
                    print(f"\n{novel[i][0]} '{novel[i][1]}' successfully deleted!\n")
                    del novel[i]
                    del synopsis[i]
                    break
                else : 
                    print("\tI am glad you did not delete my data...")
                    sleep(3)
                    break
    elif input_delete == "2" :
        delete_all_conf = input("\nAre you sure to delete all novels? (Y/N) : ").capitalize()
        if delete_all_conf == "Y" or delete_all_conf == "YES" :
            delete_all_conf_again = input("\tARE YOU REALLY SURE??? ").capitalize()
            if delete_all_conf_again == "Y" or delete_all_conf_again == "YES" or delete_all_conf_again == '' :
                novel.clear()
                print(tabulate(novel, headers = header, tablefmt = "fancy_grid"))
                print("\tYou happy? It's all gone now.")
                sleep(3) 
                print("\tAll my effort...")
                sleep(3) 
                print("\tYou ruined it...")
                sleep(3) 
                print("\tHow could you betray me...")
                sleep(3) 
                print("\tI'm mad now :(")
                sleep(3) 
                return loop_main_menu()
            else : 
                print("\tThank God you changed your mind! Be careful next time!")
                sleep(3)
                return loop_main_menu()
        else : 
            print("\tI'm glad you choose not to delete all my effort...")
            sleep(3)
            return loop_main_menu()
    else : 
        print("Your input is invalid. Please try again.")
        sleep(2)
        return loop_delete()

# ===============================================================
# BORROW 
# ===============================================================
def menu_borrow() :
    print("\n========== BORROW NOVEL ==========\n")
    print("Choose the options below :")
    print("1. Borrow a novel")
    print("2. List of borrowers")
    print("3. Back to Main Menu")

    input_borrow_menu = input("\nEnter your choice between 1-3 : ")
    if input_borrow_menu == "1" :
        input_borrow_member = input("\nDo you have any membership? (Y/N) : ").capitalize()
        if input_borrow_member == "Y" or input_borrow_member == "YES" :
            input_member = input("Please enter your full name : ").title()
            for name in range(len(member)) :
                if member[name][1] == input_member :
                    print(tabulate(member[name:name+1], headers = header_member, tablefmt = "fancy_grid"))
                    if member[name][4] == "Active" :
                        print(f"\tYour membership valid until {member[name][3]}\n")
                        sleep(2)
                        show_novel()
                        input_borrow_code = input("Which novel do you want to borrow? Please enter the code only : ").capitalize()
                        list_borrow = []
                        for code in range(len(novel)) : 
                            if novel[code][0] == input_borrow_code :
                                print("")
                                print(tabulate(novel[code:code+1], headers = header, tablefmt = "fancy_grid"))
                                total_novel = int(input("How many copies of this novel you want to borrow? "))
                                if novel[code][5] >= total_novel :
                                    novel[code][5] -= total_novel
                                    date_now = date.today() # masih bermasalah
                                    date_return = date_now + timedelta(days=30)
                                    list_borrow = [member[name][0], input_member, novel[code][1], date_now, date_return]
                                    borrower_list.append(list_borrow)
                                    print("")
                                    print(tabulate(borrower_list, headers = header_borrower, tablefmt = "fancy_grid"))
                                    print("\tCongrats! Now you can read this novel!")
                                    sleep(2)
                                    return menu_borrow()
                                elif novel[code][5] < total_novel : 
                                    print("\tThere is no available novel for the quantity you want. Please try to borrow it again next time.")
                                    sleep(2)
                                    return menu_borrow()
                            elif code == len(novel) - 1 : 
                                print("\tYour input is invalid. Please try again.")
                                sleep(2)
                                return menu_borrow()  
                    elif member[name][4] == "Expired" :
                        print("\tYour membership already expired. Please re-register your membership.")
                        sleep(2)
                        print("\tWe will move you to Membership Menu. Please wait a scond.")
                        sleep(2)
                        return loop_membership()
                elif name == len(member) - 1  : 
                    print("\tYou are not registered as membership. Please create membership first.")
                    sleep(2)
                    return loop_membership()
        elif input_borrow_member == "N" or input_borrow_member == "NO" :
            print("\tPlease wait a minute. We will move you to Membership Menu.")
            sleep(3)
            loop_membership()
        else : 
            print("\tYour input is invalid. Please try again.")
            sleep(2)
        return
    elif input_borrow_menu == "2" :
        show_borrower()
        sleep(2)
        return menu_borrow() 
    elif input_borrow_menu == "3" :
        return loop_main_menu()
    else : 
        print("\tYour input is invalid. Please try again.")
        sleep(2)
        return menu_borrow()

# ===============================================================
# MEMBERSHIP
# ===============================================================
# Create membership
def create_membership() :
    global member
    id_member = "MM00" + str(int(member[-1][0][-1]) + 1)
    input_name = input("\nEnter your name : ").title()
    input_age = input("Enter your age : ")
    
    date_now = date.today()
    date_expired = date_now + timedelta(days=365)

    member.append([id_member, input_name, input_age, date_expired, "Active"])
    print(tabulate(member[-1:], headers = header_member, tablefmt = "fancy_grid"))

def loop_membership() :
    print("\n========== MEMBERSHIP ==========\n")
    print("Choose the options below :")
    print("1. Check membership")
    print("2. Create a membership")
    print("3. Back to Main Menu")

    input_membership = input("\nEnter your choice between 1-4 : ")
    if input_membership == "1" :
        show_member()
        return loop_membership()
    elif input_membership == "2" : 
        create_membership()
        print("\tYour membership is now activated!")
        print("\tYou can borrow a novel now (yey)!")
        sleep(2)
        return loop_membership()
    elif input_membership == "3" :
        return main_menu()
    else :
        print("\tYour input is invalid. Please try again.")
        sleep(2)
        return loop_membership()

# ===============================================================
# MAIN MENU
# ===============================================================
# Loop Main Menu
def loop_main_menu() :
    while True :
        main_menu()
        input_main_menu = input("\nPlease, enter your choice between 1-7 : ")
        if input_main_menu == "1" :
            loop_check_novel()
        elif input_main_menu == "2" :
            add_new()
            loop_add_new_novel()
        elif input_main_menu == "3" :
            update_novel()
            loop_update()
        elif input_main_menu == "4" :
            delete_novel()
            loop_delete()
        elif input_main_menu == "5" :
            menu_borrow()
        elif input_main_menu == "6" :
            loop_membership()
        elif input_main_menu == "7" :
            print("\nI know sometimes it's hard to make decision, including this one. \nI'll see you another time, ok?\n")
            sleep(5)
            exit()
        else : 
            print("Your input is incorrect.")
            sleep(2)

loop_main_menu()