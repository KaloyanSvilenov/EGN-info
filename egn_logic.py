class Logic:
    def __init__(self, egn):
        self.egn = egn
        self.num_of_baby = 0
        self.region_num = 0
        self.values = {
            43: "Blagoevgrad",
            93: "Burgas",
            139: "Varna",
            169: "Veliko Tarnovo",
            183: "Vidin",
            217: "Vratsa",
            233: "Gabrovo",
            281: "Kardzali",
            301: "Kyustendil",
            319: "Lovech",
            341: "Montana",
            377: "Pazardzhik",
            395: "Pernik",
            435: "Pleven",
            501: "Plovdiv",
            527: "Razgrad",
            555: "Ruse",
            575: "Silistra",
            601: "Sliven",
            623: "Smolyan",
            721: "Sofia - city",
            751: "Sofia - region",
            789: "Stara Zagora",
            821: "Dobrich",
            843: "Targovishte",
            871: "Haskovo",
            903: "Shumen",
            925: "Yambol",
            999: "other"
        }
        self.num_babys_per_city = [
            44,  # blagoevgrad
            50,  # burgas
            46,  # varna
            30,  # veliko tarnovo
            14,  # vidin
            34,  # vratsa
            16,  # gabrovo
            48,  # kardzhali
            20,  # kyustendil
            18,  # lovech
            22,  # montana
            36,  # pazardzik
            18,  # pernik
            40,  # pleven
            66,  # plovdiv
            26,  # razgrad
            28,  # ruse
            20,  # silistra
            26,  # sliven
            22,  # smolqn
            98,  # sofiq - grad
            30,  # sofiq - okrag
            38,  # stara zagora
            32,  # dobrich
            22,  # targovishte
            28,  # haskovo
            32,  # shumen
            22  # yambol
        ]

    # true/false check if it is valid
    def check(self):

        if self.egn == '0000000000':
            return False

        mod = 11

        while 1:

            num = 0
            st = 2

            if len(self.egn) != 10:
                return False

            try:
                a = int(self.egn)
            except:
                return False

            cif = int(self.egn[9])
            self.egn = self.egn[0:9]

            for c in self.egn:
                num = (num + int(c) * st) % mod
                st *= 2

            # num = num % 10

            if num == cif:
                return True

            return False

    # get year
    def year(self):
        if 0 <= int(self.egn[2]) <= 1:
            # get the 19** years
            return "/19" + self.egn[0:2]
        else:
            # get the 20** years
            return "/20" + self.egn[0:2]

    # get day/month
    def date(self):
        egn_list = list(self.egn)
        edited_egn = ""

        if int(self.egn[2]) != 1:
            egn_list[2] = "0"
            edited_egn = ''.join(egn_list)
            return edited_egn[4:6] + "/" + edited_egn[2:4]
        else:
            # dates with months **/1*/**/****
            return edited_egn[4:6] + "/" + edited_egn[2:4]

    # get city and calculate the number of the baby
    def city(self):
        self.region_num = int(self.egn[6:9])
        counter = 0
        for x, y in self.values.items():
            if self.region_num <= x:
                if y == "other":
                    return "unknown city and number"
                else:
                    # calculate which number baby for the day is born
                    self.num_of_baby = (self.num_babys_per_city[counter] - (x - self.region_num)) // 2
                    # return city
                    return y
            counter += 1

    # get the number of the baby for the day
    def baby(self):
        return self.num_of_baby

    # return male/female
    def gender(self):
        if self.region_num % 2 == 0:
            return "М"
        else:
            return "Ж"
