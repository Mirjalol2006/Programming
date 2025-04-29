import pickle

class Talaba:
    def init(self, FISH, guruh, baholar):
        self.FISH = FISH
        self.guruh = guruh
        self.baholar = baholar  

def yukla_va_sanash(t_fayl, b_fayl):
    n = 0
    while True:
        satr = t_fayl.readline()
        if not satr:
            break
        qism = satr.strip().split(",")
        if len(qism) < 5:
            continue
        FISH = qism[0]
        guruh = int(qism[1])
        baholar = list(map(int, qism[2:5]))
        talaba = Talaba(FISH, guruh, baholar)
        pickle.dump(talaba, b_fayl)
        n += 1
    return n

def a_qarzdorlar(b_fayl):
    print("\n(a) Kamida bitta fandan qarzdor talabalar:")
    bor = False
    try:
        while True:
            talaba = pickle.load(b_fayl)
            if 2 in talaba.baholar:
                print(f"- {talaba.FISH}")
                bor = True
    except EOFError:
        if not bor:
            print("Qarzdor talabalar yo'q.")

def b_foiz_yaxshi(talabalar_soni, b_fayl):
    son = 0
    try:
        while True:
            talaba = pickle.load(b_fayl)
            if all(b >= 4 for b in talaba.baholar):
                son += 1
    except EOFError:
        pass
    foiz = (son / talabalar_soni) * 100 if talabalar_soni else 0
    print(f"\n(b) 4 va 5 baholar bilan topshirganlar foizi: {foiz:.2f}%")

def d_eng_yaxshi_fan(b_fayl):
    fanlar = ["Matematika", "Algebra", "Dasturlash"]
    natijalar = [[], [], []]

    try:
        while True:
            talaba = pickle.load(b_fayl)
            for i in range(3):
                natijalar[i].append(talaba.baholar[i])
    except EOFError:
        pass

    o_rta = [sum(f) / len(f) if f else 0 for f in natijalar]
    eng = o_rta.index(max(o_rta))
    print(f"\n(d) Eng yaxshi topshirilgan fan: {fanlar[eng]}")

def e_guruhlar_ortacha(b_fayl):
    guruhlar = {}
    try:
        while True:
            talaba = pickle.load(b_fayl)
            ort = sum(talaba.baholar) / 3
            guruh = talaba.guruh
            if guruh not in guruhlar:
                guruhlar[guruh] = []
            guruhlar[guruh].append(ort)
    except EOFError:
        pass

    ortachalar = {g: sum(b)/len(b) for g, b in guruhlar.items()}
    saralangan = sorted(ortachalar.items(), key=lambda x: x[1])

    print("\n(e) Guruhlar o'smasdan o'rtacha baho bo'yicha:")
    for guruh, qiymat in saralangan:
        print(f"Guruh {guruh}: {qiymat:.2f}")

def main():
    m_nomi = input("Matn fayl nomini kiriting: ")  
    b_nomi = input("Binar fayl nomini kiriting: ") 

    try:
        with open(m_nomi, "r") as f_m, open(b_nomi, "wb") as f_b:
            n = yukla_va_sanash(f_m, f_b)
        print(f"\nJami {n} ta talaba yozildi.")

        with open(b_nomi, "rb") as f_b:
            a_qarzdorlar(f_b)

        with open(b_nomi, "rb") as f_b:
            b_foiz_yaxshi(n, f_b)

        with open(b_nomi, "rb") as f_b:
            d_eng_yaxshi_fan(f_b)

        with open(b_nomi, "rb") as f_b:
            e_guruhlar_ortacha(f_b)

    except FileNotFoundError:
        print("Fayl topilmadi!")
    except Exception as e:
        print(f"Xatolik: {str(e)}")

if __name__ == "__main__":
    main()
    