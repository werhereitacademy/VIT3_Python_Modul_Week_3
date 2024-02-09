"""
English
Question 1: Task Manager Application
Project Description: In this assignment, you will create a task manager application using the Python programming language. This application allows users to add, complete, delete, and list their tasks.

Requirements:
1- Tasks will be stored in a Python list, and each task will be represented as a dictionary.
Each task should have the following properties:

Order Number (Automatically assigned)
Task Name
Status (Successful, Pending, or Deleted)
2- Operations that the user can perform:
Add a new task
Complete a task
Delete a task
List completed tasks
List all tasks with their statuses
Exit
3- Tasks should automatically receive an order number based on their addition order.
4- Newly added tasks should replace deleted task numbers.
5- Tasks should be sorted by order number when listed.
6- Appropriate feedback should be provided to the user after each operation. For example, when adding a new task, the user should see a message indicating that the task has been added.
"""
class TaskManagerApplication:
    def __init__(self):
        self.tasks = []
        self.completed_tasks = []

    def find_empty_order(self):
        order_numbers = []
        for task in self.tasks:
            if "order number" in task:
                order_numbers.append(task["order number"])
        order_numbers.sort()

        for i, order in enumerate(order_numbers, start=1):
            if i != order:
                return i

        return len(order_numbers) + 1

    def add_task(self, task_name, task_status):
        self.task_name = task_name
        for i, task in enumerate(self.tasks):
            if task_name in task['task name']:
                print("The same task already exists in the system.")
                return

        self.task_status = task_status
        empty_order = self.find_empty_order()
        self.tasks.append({
            "order number": empty_order,
            "task name": self.task_name,
            "task status": self.task_status})
        print(f"The task '{self.task_name}' has been successfully added.")

    def complete_task(self):
        choice = input("Enter the task you want to complete:")
        for i, task in enumerate(self.tasks):
            if choice == task['task name']:
                self.tasks[i]['task status'] = "Successful"
                print(f"The task '{choice}' has been successfully completed.")
                self.completed_tasks.append(choice)

    def completed_task(self, task_name):
        self.completed_tasks.append(task_name)
        print(f"The task '{task_name}' has been successfully added to the completed tasks list.")
        print("Your updated list of completed tasks:")
        print(self.completed_tasks)

    def delete_task(self):
        choice = input("Enter the task you want to delete:")
        for i, task in enumerate(self.tasks):
            if choice == task['task name']:
                self.tasks.pop(i)
                print(f"The task '{choice}' has been deleted.")

    def view_completed_tasks(self):
        return print(self.completed_tasks)

    def view_all_tasks(self):
        sorted_list = sorted(self.tasks, key=lambda x: x["order number"])
        return print(sorted_list)


task_manager = TaskManagerApplication()
while True:

    choice = input(
        "≀~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ≀" +  # kullaniciya ilk giriste gorunecek olan menu tasarimi.
        "\n≀                                                  ≀" +
        "\n≀  Press 1 to add a task                           ≀" +
        "\n≀  Press 2 to mark a task as completed             ≀" +
        "\n≀  Press 3 to delete a task                        ≀" +
        "\n≀  Press 4 to view completed tasks                 ≀" +
        "\n≀  Press 5 to view all tasks                       ≀" +
        "\n≀  Press 6 to exit the application                 ≀" +
        "\n≀                                                  ≀" +
        "\n≀~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ≀")
    
    if choice == "1":
        task_name = input("Please enter the task name:")
        task_status_selection = input("Please specify the task status as follows:\n"
                                      "Press `1` to select Successful\n"
                                      "Press `2` to select Pending.")
        if task_status_selection == "1":
            task_manager.add_task(task_name=task_name, task_status="Successful")
            task_manager.completed_task(task_name=task_name)

        elif task_status_selection == "2":
            task_manager.add_task(task_name=task_name, task_status="Pending")
        else:
            print("You pressed a wrong key.")

    elif choice == "2":
        task_manager.complete_task()
    elif choice == "3":
        task_manager.delete_task()
    elif choice == "4":
        task_manager.view_completed_tasks()
    elif choice == "5":
        task_manager.view_all_tasks()
    elif choice == "6":
        print("Exiting the system.")
        break









"""
Turkce
Soru1:Görev Yöneticisi Uygulaması
Proje Açıklaması: Bu ödevde, Python programlama dilini kullanarak bir görev yöneticisi uygulaması oluşturacaksınız. Bu uygulama, kullanıcılara görevlerini eklemelerine, tamamlamalarına, silmelerine ve listelemelerine olanak tanır.

Gereksinimler:
1- Görevler, bir Python listesi içinde saklanacak ve her görev bir sözlük olarak temsil edilecektir.
Her görev aşağıdaki özelliklere sahip olmalıdır:
-Sıra Numarası (Otomatik olarak atanmalıdır)
-Görevin Adı
-Durumu (Başarılı, Beklemede veya Silindi)
2- Kullanıcının yapabileceği işlemler:
-Yeni bir görev ekle
-Bir görevi tamamla
-Bir görevi sil
-Tamamlanmış görevleri listele
-Tüm görevleri durumları ile birlikte listele
Çıkış
3-Görevler, eklenme sırasına göre otomatik olarak sıra numarası almalıdır.
4-Yeni eklenecek görevler silinen görev numaralarının yerine kaydedilmelidir.
5-Görevler listelenirken sıra numarasına göre sıralanmalıdır.
6-Kullanıcıya her işlem sonrasında uygun geri bildirimler verilmelidir. Örneğin, yeni bir görev eklediğinde, görev eklenmiş olduğuna dair bir mesaj görmelidir.
"""


class GorevYoneticisiUygulamasi:
    def __init__(self):
        self.gorevler = []
        self.tamamlanan_gorevler= []
    def bos_sira_bul(self):
        sira_numaralari = []
        for islem in self.gorevler:
            if "sira no" in islem:
                sira_numaralari.append(islem["sira no"])
        #Mesela [{'sira no': 1, 'gorev adi': 'Kitap okumak', 'gorev durumu': 'Basarili'}, {'sira no': 2, 'gorev adi': 'Ders Calismak', 'gorev durumu': 'Beklemede'}
        #diye listemiz var burada sira nolarda dolasip sira numaralarini bir listede topluyoruz.
        sira_numaralari.sort()
        ## Burada liste elemanlarını küçükten büyüğe sıraliyoruz.
        """enumerate, bir döngü içinde hem indeks (sıra numarası) hem de eleman üzerinde dolaşmayı sağlar."""

        for i, sira in enumerate(sira_numaralari, start=1):
            if i != sira:
                return i
                # Sira numarasi sayisinca icinde dolasiyoruz eğer i ve sira numarası eşleşmiyorsa (boş bir sıra bulduk demektir)

        return len(sira_numaralari) + 1
        # Döngüden çıktıktan sonra hiç boş sıra bulamamışsak, en sonuncu sıranın bir fazlasını döndür.

    def gorevekle(self, gorevadi, gorevdurumu):

        self.gorevadi = gorevadi
        for i, gorev in enumerate(self.gorevler):
            if gorevadi in gorev['gorev adi']:
                print("Ayni gorev sistemde bulunmaktadir.")
                return

        self.gorevdurumu = gorevdurumu
        bos_sira = self.bos_sira_bul()
        #verecegimiz sirayi hazirladigimiz fonksiyondan cagiriyoruz.
        self.gorevler.append({
            "sira no": bos_sira,
            "gorev adi": self.gorevadi,
            "gorev durumu": self.gorevdurumu})
        print(f"{self.gorevadi} gorevi eklenmesi basari ile tamamlandi.")


        #sira numarasina(keys) gore siralamak icin bu islemi yapiyoruz
        #her bir gorev eklendigi zaman listeyi sira numarasina gore siralayacak.
    def gorevtamamla(self):
        secim = input("Tamamlamak istediğiniz görevi giriniz:")
        #enumerate, bir döngü içinde hem indeks (sıra numarası) hem de eleman üzerinde dolaşmayı sağlar.
        for i, gorev in enumerate(self.gorevler):
            if secim == gorev['gorev adi']:
                self.gorevler[i]['gorev durumu'] = "Basarili"
                print(f"{secim} görevi başarıyla tamamlandı.")

                #self.tamamlanan_gorevler.append({secim:"Basarili"})
                #bu sekilde icinde sozluk olarak da ekleyebilirdik ama soruda sadece listele diyor
                self.tamamlanan_gorevler.append(secim)

    def tamamlanan_gorev(self,gorevadi):
        self.tamamlanan_gorevler.append(gorevadi)
        print(f"Basari ile tamamlanan {gorevadi} gorevi, tamamlanan gorevler listesine eklenmistir.")
        print("Guncel tamamlanan gorevler listeniz;")
        print( self.tamamlanan_gorevler)


    def gorevsil(self):
        secim = input("Silmek istediginiz gorevi yaziniz:")
        for i, gorev in enumerate(self.gorevler):
            if secim == gorev['gorev adi']:
                self.gorevler.pop(i)
                print(f"{secim} görevi silindi.")

    def tamgorevgoruntule(self):
        return print(self.tamamlanan_gorevler)

    def tumgorevgoruntule(self):
        sirali_liste = sorted(self.gorevler,key=lambda x: x["sira no"])
        return print(sirali_liste)


g1 = GorevYoneticisiUygulamasi()
while True:

    secim = input("≀~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ≀" +     #kullaniciya ilk giriste gorunecek olan menu tasarimi.
         "\n≀                                                           ≀" +
         "\n≀   Gorev eklemek icin 1'e basin                            ≀" +
         "\n≀   Bir gorevi tamamlamak icin 2'ye basin                   ≀" +
         "\n≀   Bir gorevi silmek icin 3'e basin                        ≀" +
         "\n≀   Tamamlanan gorevleri goruntulemek icin 4'e basin        ≀" +
         "\n≀   Tum gorevleri goruntulemek icin 5'e basin               ≀" +
         "\n≀   Uygulamadan cikmak icin 6`ya basin                      ≀" +
         "\n≀                                                           ≀" +
         "\n≀~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ≀")




    if secim == "1":
        gorevadi = input("Lutfen gorev adi giriniz:")
        gorevdurumu_belirleme = input("Lutfen gorev durumunuzu asagidakilere gore belirtiniz:\n"
                                      "Basarili diye secmek icin `1`\n"
                                      "Beklemede diye secmek icin `2`ye basiniz.")
        if gorevdurumu_belirleme == "1":
            g1.gorevekle(gorevadi=gorevadi, gorevdurumu="Basarili")
            g1.tamamlanan_gorev(gorevadi=gorevadi)

        elif gorevdurumu_belirleme == "2":
            g1.gorevekle(gorevadi=gorevadi, gorevdurumu="Beklemede")
        else:
            print("Yanlis bir tusa bastiniz.")

    elif secim == "2":
        g1.gorevtamamla()
    elif secim == "3":
        g1.gorevsil()
    elif secim == "4":
        g1.tamgorevgoruntule()
    elif secim == "5":
        g1.tumgorevgoruntule()
    elif secim == "6":
        print("Sistemeden cikis yapiliyor")
        break
