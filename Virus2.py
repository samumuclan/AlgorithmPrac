"""得到病毒：二擇一演算法實例"""


class Stage:
    Welcome = ""
    Description = ""
    Attribute = ""
    LEVEL = 1
    EXP = 0
    Money = 0
    Ata = 0.1
    Def = 0.1
    Skill = 0.1

    def __init__(self,
                 Welcome="",
                 Description="",
                 Attribute="",
                 LEVEL=1,
                 EXP=0,
                 Money=0,
                 Ata=0.1,
                 Def=0.1,
                 Skill=0.1
                 ):
        self.Welcome = Welcome
        self.Description = Description
        self.Attribute = Attribute
        self.LEVEL = LEVEL
        self.Money = Money
        self.EXP = EXP
        self.Ata = Ata
        self.Def = Def
        self.Skill = Skill


class StageForest(Stage):
    Place = ""
    Choice1_context = ""
    Choice2_context = ""
    Choice3_context = ""
    Choice4_context = ""
    Input = ""

    def __init__(self,
                 Welcome,
                 Description,
                 Attribute,
                 LEVEL,
                 EXP,
                 Money,
                 Ata,
                 Def,
                 Skill,
                 Place="",
                 Choice1_context="",
                 Choice2_context="",
                 Choice3_context="",
                 Choice4_context="",
                 Input=""
                 ):
        super().__init__(Welcome, Description, Attribute, LEVEL, EXP, Money, Ata, Def, Skill)
        self.Place = Place
        self.Choice1_context = Choice1_context
        self.Choice2_context = Choice2_context
        self.Choice3_context = Choice3_context
        self.Choice4_context = Choice4_context
        self.Input = Input

    def jorney(self):
        print(self.Welcome)
        print("{0} {1}".format(self.Description, self.Place))
        print(self.Choice1_context)
        print(self.Choice2_context)
        print(self.Choice3_context)
        print(self.Choice4_context)
        choice = input(self.Input)
        print("=====================")
        if choice == "A":
            self.Ata += 0.3
            self.Def += 0.2
        elif choice == "B":
            self.Ata += 0.3
            self.Skill += 0.2
        elif choice == "C":
            self.Ata += 0.1
            self.Skill += 0.4
        elif choice == "D":
            self.Ata += 0.1
            self.Def += 0.4

        print(self.Attribute)
        print("LEVEL ：{0}".format(self.LEVEL))
        print("Attack：{:.1f}".format(self.Ata))
        print("Defrnd：{:.1f}".format(self.Def))
        print("Skill ：{:.1f}".format(self.Skill))
        print("EXP   ：{0}".format(self.EXP))
        print("Money ：{0}".format(self.Money))
        print("Let's go to next stage...")

    def get_LEVEL(self):
        return self.LEVEL

    def get_Ata(self):
        return float(self.Ata)

    def get_Def(self):
        return float(self.Def)

    def get_Skill(self):
        return float(self.Skill)

    def get_EXP(self):
        return self.EXP

    def get_Money(self):
        return self.Money


class StageOcean(Stage):
    Situation = ""
    Lobster = 0.5
    FallEXP = 20
    FallMoney = 100
    Weapon1 = 70
    Weapon2 = 60
    Weapon3 = 50

    def __init__(self,
                 Welcome,
                 Description,
                 Attribute,
                 LEVEL,
                 EXP,
                 Money,
                 Ata,
                 Def,
                 Skill,
                 Situation="",
                 Lobster=0.5,
                 FallEXP=20,
                 FallMoney=100,
                 Weapon1=70,
                 Weapon2=60,
                 Weapon3=50):
        super().__init__(Welcome, Description, Attribute, LEVEL, EXP, Money, Ata, Def, Skill)
        self.Situation = Situation
        self.Lobster = Lobster
        self.FallEXP = FallEXP
        self.FallMoney = FallMoney
        self.Weapon1 = Weapon1
        self.Weapon2 = Weapon2
        self.Weapon3 = Weapon3

    def journey(self):
        print("========================")
        print("{0} {1}".format(self.Description, self.Situation))
        print("遭遇 lobster 戰鬥中")
        print("....................")
        print("....................")

        N = self.Ata*2.0+self.Def*1.0+self.Skill*2.0
        if N < self.Lobster:
            print("Game Over!!!")
            SystemExit()
        elif N >= self.Lobster:
            print("恭喜打敗怪獸！！")
            self.EXP += self.FallEXP
            self.Money += self.FallMoney
            print("獲得100金幣")
            print("獲得經驗值")

        if self.EXP >= 20:
            print("Level UP!!!各項數值提升")
            self.LEVEL += 1
            self.EXP -= 20
            self.Ata += 0.2
            self.Def += 0.2
            self.Skill += 0.2
        print("========================")
        print("歡迎來到商店：")
        print("A.長劍,價格 70, 提升Ata 0.7")
        print("B.長杖,價格 60, 提升Skill 0.6")
        print("C.鎧甲,價格 50, 提升Def 0.5")
        choice = input("請輸入選擇：")
        if choice == "A":
            print("購買長劍!!!")
            self.Ata += 0.7
            self.Money -= self.Weapon1
        elif choice == "B":
            print("購買長杖!!!")
            self.Skill += 0.6
            self.Money -= self.Weapon2
        elif choice == "C":
            print("購買鎧甲!!!")
            self.Def += 0.5
            self.Money -= self.Weapon3
        print("========================")
        print(self.Attribute)
        print("LEVEL：{0}".format(self.LEVEL))
        print("Attack：{:.1f}".format(self.Ata))
        print("Defrnd：{:.1f}".format(self.Def))
        print("Skill ：{:.1f}".format(self.Skill))
        print("EXP：{0}".format(self.EXP))
        print("Money：{0}".format(self.Money))
        print("Let's go to next stage...")


stage1 = StageForest("Welcome to GetVirus",
                     "歡迎妳的到來！目前你位於",
                     "目前角色屬性為：",
                     1,
                     0,
                     0,
                     0.1,
                     0.1,
                     0.1,
                     "轉職森林",
                     "A. 劍士",
                     "B. 弓箭手",
                     "C. 法師",
                     "D. 騎士",
                     "請選擇職業："
                     )
stage1.jorney()
stage2 = StageOcean("Welcome to GetVirus",
                    "歡迎妳的到來！目前你位於",
                    "目前角色屬性為：",
                    stage1.get_LEVEL(),
                    stage1.get_EXP(),
                    stage1.get_Money(),
                    stage1.get_Ata(),
                    stage1.get_Def(),
                    stage1.get_Skill(),
                    "海洋之城",
                    0.5,
                    20,
                    100,
                    70,
                    60,
                    50)
stage2.journey()
