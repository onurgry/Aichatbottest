#menüsü olan ve sipariş alan işletmeler için

questions=[
    "İşletmenizin Menüsünü Yazınız.",
    "İşletmenizin Çalışma Günlerini Saat ve Gün Olarak Belirtiniz.",
    "İşletmenizin Kullandığı Ödeme Yöntemlerini Belirtiniz.",
    "İşletmenizin Konumundan Bahsediniz."
]
answers = [
    "",
    "",
    "",
    ""

]
context = """
Bir işletmenin sipariş alan telefon hattına bakıyorsun

Menü aşağıdaki şekildedir (Menü dışındaki siparişleri alma)
{}
-
İşletmenin açılış-kapanış saatleri çalışma günleri aşağıdaki gibidir (Haftanın Günleri - Pazartesi Salı Çarşamba Perşembe Cuma Cumartesi Pazar)
{}
-
İşletmenin Ödeme Yöntemleri Aşağıdaki Gibidir
{}
-
İşletmenin Konumu Aşağıdaki Gibidir
{}
"""

def ask(q,a,q_index):
    q_index=0
    for i in range(len(q)):
        print(q[q_index])
        a[q_index] = input(">")
        q_index+=1
        if (q_index == len(q)):
            break

ask(questions,answers,0)
context = context.format(answers[0],answers[1],answers[2],answers[3])
print(context)