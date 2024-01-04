class FriedChicken():
    def __init__(self,price,taste,num,part,combo): #建構子(價錢,口味,數量,部位,套餐)
        self.price=price
        self.taste=taste
        self.num=num
        self.part=part
        self.combo=combo

    def search_price(self): #查詢價錢
        if self.combo==True: #有套餐則價錢+100
            return self.price*self.num+100
        else:
            return self.price*self.num

    def search_taste(self):#查詢口味
        return self.taste

    def change_taste(self,taste):#改變口味
        self.taste=taste


class Employer():
    def __init__(self,name,seniority,working_hours,hourly_rate=178): #建構子(名字,年資,時數,時薪:預設178)
        self.name=name
        self.seniority=seniority
        self.working_hours=working_hours
        self.hourly_rate=hourly_rate
    def search_name(self): #查詢名字
        return self.name
    def search_seniority(self):#查詢年資
        return self.seniority
    def search_working_hours(self):#查詢時數
        return self.working_hours
    def calculate_monthly_salary(self):#計算月薪
        return self.working_hours*self.hourly_rate
    def add_working_rate(self,hours):#更改時數
        self.working_hours+=hours
    def add_seniority(self,years):#更改時數
        self.seniority+=years


class Drink():
    def __init__(self,name,sweetness,price): #建構子(名字,甜度,價錢)
        self.name=name
        self.sweetness=sweetness
        self.price=price
    
    def change_name(self,name): #更改名字
        self.name=name
    
    def change_sweetness(self,sweetness): #更改甜度
        self.sweetness=sweetness

    def change_price(self,price): #更改價錢
        self.price=price

class ColdDrink(Drink): #繼承自Drink
    def __init__(self,name,sweetness,price,ice): #建構子(冰塊)
        super().__init__(name,sweetness,price)
        self.ice=ice

class HotDrink(Drink): #繼承自Drink
    def __init__(self,name,sweetness,price): #建構子
        super().__init__(name,sweetness,price)

def test_1():
    meals=[] #建構餐點列表
    meals.append(FriedChicken(90,"original",2,"drumstick",True))
    meals.append(FriedChicken(50,"hot",4,"chicken wings",False))
    meals.append(FriedChicken(60,"peppery",3,"chicken",False))
    meals.append(FriedChicken(100,"original",1,"chicken steak",True))

    for idx,i in enumerate(meals): #印出餐點資料
        print("meal number {}:".format(idx+1))
        print("price:{}".format(i.search_price()))
        print("taste:{}".format(i.search_taste()))

    print("\nchange taste:")
    for i in meals: #更改餐點口味並印出
        taste=i.search_taste()
        i.change_taste("Korean style")
        print("taste:{}->{}".format(taste,i.search_taste()))

def test_2():
    employer=[] #建構員工列表
    employer.append(Employer("Kevin",3,50))
    employer.append(Employer("Cruz",4,40))
    employer.append(Employer("Jane",1,55))

    for i in employer: #印出員工月薪
        print("employer [{}]:".format(i.search_name()))
        print("seniority:{}".format(i.search_seniority()))
        print("working hours:{}\n".format(i.search_working_hours()))

    for i in employer: 
        print("{}:{}".format(i.search_name(),i.calculate_monthly_salary()))

    print("")
    for i in employer: #更改員工年資並印出
        seniority=i.search_seniority()
        i.add_seniority(1)
        print("[{}] seniority:{}->{}".format(i.search_name(),seniority,i.search_seniority()))

    print("")
    for i in employer: #更改員工時數並印出
        working_hours=i.search_working_hours()
        i.add_working_rate(10)
        print("[{}] working hours:{}->{}".format(i.search_working_hours(),working_hours,i.search_working_hours()))

def test_3():
    drinks=[] #建構飲料列表
    drinks.append(HotDrink("milk tea",2,60))
    drinks.append(ColdDrink("black tea",1,30,2))
    drinks.append(ColdDrink("tea",0,30,1))

    for idx,i in enumerate(drinks): #印出飲料資料
        print("drink [{}]:".format(idx+1))
        print("name:{}".format(i.name))
        print("sweetness:{}".format(i.sweetness))
        if isinstance(i, ColdDrink):
            print("ice:{}".format(i.ice))
        print("price:{}\n".format(i.price))

    print("")
    for idx,i in enumerate(drinks): #更改飲料,甜度,價錢並印出
        print("drink [{}]:".format(idx+1))
        name=i.name
        i.change_name("fruit tea")
        print("name:{}->{}".format(name,i.name))
        sweetness=i.sweetness
        i.change_sweetness(3)
        print("sweetness:{}->{}".format(sweetness,i.sweetness))
        price=i.price
        i.change_price(50)
        print("price:{}->{}\n".format(price,i.price))



if __name__=="__main__":
    print("----------題目1----------")
    test_1()
    print("----------題目2(員工)----------")
    test_2()
    print("----------題目2(飲料)----------")
    test_3()