from experta import *
import experta
import os

def input_validation(question):
    while True:
        data = input(question)
        if not data:
            print("Error, no answer.")
            continue
        else:
            if data.lower() not in ('no', 'low', 'high'):
                print("Not an appropriate answer")
            else:
                break
    return data

class Greetings(KnowledgeEngine):
    def __init__(self, symptom_map, if_not_matched, get_treatments, get_details):
        self.symptom_map = symptom_map
        self.if_not_matched = if_not_matched
        self.get_details = get_details
        self.get_treatments = get_treatments
        KnowledgeEngine.__init__(self)

    #code giving instructions on how to use the Expert System
    @DefFacts()
    def _initial_action(self):
        os.system('cls')
        print("\nCar Brand Chooser: Expert System")
        print("\nAnswer the following questions to find the perfect match for your next car. (Answer with high, low or no)")
        yield Fact(action="get_Brand")

    #taking various input from user
    @Rule(Fact(action="get_Brand"), NOT(Fact(Quality=W())), salience=4)
    def symptom_0(self):
        self.declare(Fact(Quality=input_validation("Is quality important to you? ")))

    @Rule(Fact(action="get_Brand"), NOT(Fact(Comfortable=W())), salience=1)
    def symptom_1(self):
        self.declare(Fact(Comfortable=input_validation("Do you need a comfortable car? ")))

    @Rule(Fact(action="get_Brand"), NOT(Fact(Affordable=W())), salience=1)
    def symptom_2(self):
        self.declare(Fact(Affordable=input_validation("Could money be a limitation for you? ")))

    @Rule(Fact(action="get_Brand"), NOT(Fact(Reliable=W())), salience=3)
    def symptom_3(self):
        self.declare(Fact(Reliable=input_validation("Is reliability an important aspect for your purchase? ")))

    @Rule(Fact(action="get_Brand"), NOT(Fact(Economical_to_operate=W())), salience=1)
    def symptom_4(self):
        self.declare(Fact(Economical_to_operate=input_validation("After buying, are you looking for cheap maintenance? ")))

    @Rule(Fact(action="get_Brand"), NOT(Fact(Fast=W())), salience=1)
    def symptom_5(self):
        self.declare(Fact(Fast=input_validation("Do you need a fast car? ")))

    @Rule(Fact(action="get_Brand"), NOT(Fact(Good_Looking=W())), salience=1)
    def symptom_6(self):
        self.declare(Fact(Good_Looking=input_validation("Is appearance and design important to you? ")))

    @Rule(Fact(action="get_Brand"), NOT(Fact(Fuel_Saver=W())), salience=1)
    def symptom_7(self):
        self.declare(Fact(Fuel_Saver=input_validation("Would you like it to be fuel saver? ")))

    @Rule(Fact(action="get_Brand"), NOT(Fact(Great_Drive=W())), salience=1)
    def symptom_8(self):
        self.declare(Fact(Great_Drive=input_validation("Do you focus on having a good drive in your car? ")))

    @Rule(Fact(action="get_Brand"), NOT(Fact(Good_Resale=W())), salience=1)
    def symptom_9(self):
        self.declare(Fact(Good_Resale=input_validation("Are you looking for a good amount of cash in your car resale? ")))

    @Rule(Fact(action="get_Brand"), NOT(Fact(Customization=W())), salience=1)
    def symptom_10(self):
        self.declare(Fact(Customization=input_validation("Do you prefer a car that is customizable to your tastes? ")))

    @Rule(Fact(action="get_Brand"), NOT(Fact(Quick_Delivery=W())), salience=1)
    def symptom_11(self):
        self.declare(Fact(Quick_Delivery=input_validation("Do you need immediate delivery? ")))

    @Rule(Fact(action="get_Brand"), NOT(Fact(Financing=W())), salience=1)
    def symptom_12(self):
        self.declare(Fact(Financing=input_validation("Do you need to complete money and need financing? ")))

    #different rules checking for each disease match
    @Rule(
        Fact(action="get_Brand"),
        Fact(Quality="high"),
        Fact(Comfortable="high"),
        Fact(Affordable="high"),
        Fact(Reliable="high"),
        Fact(Economical_to_operate="high"),
        Fact(Good_Resale="high"),
        Fact(Fast="no"),
        Fact(Great_Drive="low"),
        Fact(Fuel_Saver="high"),
        Fact(Customization="no"),
        Fact(Good_Looking="low"),
        Fact(Quick_Delivery="no"),
        Fact(Financing="high"),
    )
    def disease_0(self):
        self.declare(Fact(disease="Toyota"))

    @Rule(
        Fact(action="get_Brand"),
        Fact(Quality="high"),
        Fact(Comfortable="high"),
        Fact(Affordable="high"),
        Fact(Reliable="high"),
        Fact(Economical_to_operate="high"),
        Fact(Good_Resale="high"),
        Fact(Fast="no"),
        Fact(Great_Drive="low"),
        Fact(Fuel_Saver="high"),
        Fact(Customization="no"),
        Fact(Good_Looking="low"),
        Fact(Quick_Delivery="high"),
        Fact(Financing="high"),
    )
    def disease_1(self):
        self.declare(Fact(disease="Nissan"))

    @Rule(
        Fact(action="get_Brand"),
        Fact(Quality="high"),
        Fact(Comfortable="low"),
        Fact(Affordable="no"),
        Fact(Reliable="low"),
        Fact(Economical_to_operate="low"),
        Fact(Fast="high"),
        Fact(Good_Looking="low"),
        Fact(Fuel_Saver="low"),
        Fact(Great_Drive="high"),
        Fact(Good_Resale="low"),
        Fact(Customization="no"),
        Fact(Quick_Delivery="low"),
        Fact(Financing="high"),
    )
    def disease_2(self):
        self.declare(Fact(disease="Mazda"))

    @Rule(
        Fact(action="get_Brand"),
        Fact(Quality="low"),
        Fact(Comfortable="high"),
        Fact(Affordable="high"),
        Fact(Reliable="low"),
        Fact(Economical_to_operate="high"),
        Fact(Good_Resale="high"),
        Fact(Fast="low"),
        Fact(Great_Drive="low"),
        Fact(Fuel_Saver="high"),
        Fact(Customization="low"),
        Fact(Good_Looking="high"),
        Fact(Quick_Delivery="high"),
        Fact(Financing="high"),
    )
    def disease_3(self):
        self.declare(Fact(disease="Kia"))

    @Rule(
        Fact(action="get_Brand"),
        Fact(Quality="low"),
        Fact(Comfortable="low"),
        Fact(Affordable="high"),
        Fact(Reliable="low"),
        Fact(Economical_to_operate="high"),
        Fact(Good_Resale="no"),
        Fact(Fast="no"),
        Fact(Great_Drive="high"),
        Fact(Fuel_Saver="high"),
        Fact(Customization="low"),
        Fact(Good_Looking="high"),
        Fact(Quick_Delivery="high"),
        Fact(Financing="high"),
    )
    def disease_4(self):
        self.declare(Fact(disease="Hyundai"))

    @Rule(
        Fact(action="get_Brand"),
        Fact(Quality="high"),
        Fact(Comfortable="high"),
        Fact(Affordable="no"),
        Fact(Reliable="high"),
        Fact(Economical_to_operate="no"),
        Fact(Good_Resale="high"),
        Fact(Fast="high"),
        Fact(Great_Drive="high"),
        Fact(Fuel_Saver="no"),
        Fact(Customization="no"),
        Fact(Good_Looking="high"),
        Fact(Quick_Delivery="no"),
        Fact(Financing="high"),
    )
    def disease_5(self):
        self.declare(Fact(disease="Honda"))

    @Rule(
        Fact(action="get_Brand"),
        Fact(Quality="low"),
        Fact(Comfortable="high"),
        Fact(Affordable="low"),
        Fact(Reliable="high"),
        Fact(Economical_to_operate="low"),
        Fact(Good_Resale="no"),
        Fact(Fast="no"),
        Fact(Great_Drive="low"),
        Fact(Fuel_Saver="low"),
        Fact(Customization="low"),
        Fact(Good_Looking="low"),
        Fact(Quick_Delivery="low"),
        Fact(Financing="low"),
    )
    def disease_6(self):
        self.declare(Fact(disease="Ford"))

    @Rule(
        Fact(action="get_Brand"),
        Fact(Quality="high"),
        Fact(Comfortable="low"),
        Fact(Affordable="low"),
        Fact(Reliable="high"),
        Fact(Economical_to_operate="high"),
        Fact(Good_Resale="high"),
        Fact(Fast="low"),
        Fact(Great_Drive="low"),
        Fact(Fuel_Saver="high"),
        Fact(Customization="high"),
        Fact(Good_Looking="low"),
        Fact(Quick_Delivery="no"),
        Fact(Financing="low"),
    )
    def disease_7(self):
        self.declare(Fact(disease="Volkswagen"))

    @Rule(
        Fact(action="get_Brand"),
        Fact(Quality="no"),
        Fact(Comfortable="low"),
        Fact(Affordable="high"),
        Fact(Reliable="no"),
        Fact(Economical_to_operate="high"),
        Fact(Good_Resale="low"),
        Fact(Fast="high"),
        Fact(Great_Drive="no"),
        Fact(Fuel_Saver="no"),
        Fact(Customization="no"),
        Fact(Good_Looking="high"),
        Fact(Quick_Delivery="high"),
        Fact(Financing="high"),
    )
    def disease_8(self):
        self.declare(Fact(disease="MG"))

    @Rule(
        Fact(action="get_Brand"),
        Fact(Quality="low"),
        Fact(Comfortable="low"),
        Fact(Affordable="no"),
        Fact(Reliable="high"),
        Fact(Economical_to_operate="low"),
        Fact(Good_Resale="high"),
        Fact(Fast="high"),
        Fact(Great_Drive="low"),
        Fact(Fuel_Saver="high"),
        Fact(Customization="low"),
        Fact(Good_Looking="high"),
        Fact(Quick_Delivery="low"),
        Fact(Financing="no"),
    )
    def disease_9(self):
        self.declare(Fact(disease="Seat"))

    @Rule(
        Fact(action="get_Brand"),
        Fact(Quality="low"),
        Fact(Comfortable="low"),
        Fact(Affordable="high"),
        Fact(Reliable="no"),
        Fact(Economical_to_operate="no"),
        Fact(Good_Resale="high"),
        Fact(Fast="high"),
        Fact(Great_Drive="low"),
        Fact(Fuel_Saver="high"),
        Fact(Customization="no"),
        Fact(Good_Looking="low"),
        Fact(Quick_Delivery="high"),
        Fact(Financing="low"),
    )
    def disease_10(self):
        self.declare(Fact(disease="Renault"))

    @Rule(
        Fact(action="get_Brand"),
        Fact(Quality="no"),
        Fact(Comfortable="low"),
        Fact(Affordable="high"),
        Fact(Reliable="low"),
        Fact(Economical_to_operate="no"),
        Fact(Good_Resale="no"),
        Fact(Fast="no"),
        Fact(Great_Drive="low"),
        Fact(Fuel_Saver="no"),
        Fact(Customization="no"),
        Fact(Good_Looking="low"),
        Fact(Quick_Delivery="high"),
        Fact(Financing="no"),
    )
    def disease_11(self):
        self.declare(Fact(disease="Suzuki"))

    @Rule(
        Fact(action="get_Brand"),
        Fact(Quality="no"),
        Fact(Comfortable="high"),
        Fact(Affordable="low"),
        Fact(Reliable="low"),
        Fact(Economical_to_operate="high"),
        Fact(Good_Resale="low"),
        Fact(Fast="no"),
        Fact(Great_Drive="high"),
        Fact(Fuel_Saver="low"),
        Fact(Customization="high"),
        Fact(Good_Looking="low"),
        Fact(Quick_Delivery="high"),
        Fact(Financing="high"),
    )
    def disease_12(self):
        self.declare(Fact(disease="Chevrolet"))
    
    @Rule(
        Fact(action="get_Brand"),
        Fact(Quality="high"),
        Fact(Comfortable="low"),
        Fact(Affordable="no"),
        Fact(Reliable="low"),
        Fact(Economical_to_operate="no"),
        Fact(Good_Resale="no"),
        Fact(Fast="high"),
        Fact(Great_Drive="high"),
        Fact(Fuel_Saver="low"),
        Fact(Customization="high"),
        Fact(Good_Looking="high"),
        Fact(Quick_Delivery="no"),
        Fact(Financing="no"),
    )
    def disease_13(self):
        self.declare(Fact(disease="Peugeot"))

    #when the user's input doesn't match any disease in the knowledge base
    @Rule(Fact(action="get_Brand"), Fact(disease=MATCH.disease), salience=-998)
    def disease(self, disease):
        id_disease = disease
        disease_details = self.get_details(id_disease)
        treatments = self.get_treatments(id_disease)
        os.system('cls')
        print(f"\nAccording to your necessities you are looking for a: {id_car_brand}\n")
        print(f"Description: {car_brand_details}\n")
        print(f"Brand Best Seller: {characteristics}\n")
        

    @Rule(
        Fact(action="get_Brand"),
        Fact(Quality=MATCH.Quality),
        Fact(Comfortable=MATCH.Comfortable),
        Fact(Affordable=MATCH.Affordable),
        Fact(Reliable=MATCH.Reliable),
        Fact(Economical_to_operate=MATCH.Economical_to_operate),
        Fact(Good_Resale=MATCH.Good_Resale),
        Fact(Fast=MATCH.Fast),
        Fact(Fuel_Saver=MATCH.Fuel_Saver),
        Fact(Great_Drive=MATCH.Great_Drive),
        Fact(Customization=MATCH.Customization),
        Fact(Good_Looking=MATCH.Good_Looking),
        Fact(Quick_Delivery=MATCH.Quick_Delivery),
        Fact(Financing=MATCH.Financing),
        NOT(Fact(disease=MATCH.disease)),
        salience=-999
    )
    def not_matched(self,Quality,Comfortable, Affordable,Reliable,Economical_to_operate,Good_Resale,
                    Fast,Great_Drive,Fuel_Saver,Customization,Good_Looking,Quick_Delivery, Financing,):
        os.system('cls')
        #<print("\nThe bot did not find any diseases that match your exact symptoms.")
        lis = [Quality,Comfortable, Affordable,Reliable,Economical_to_operate,Good_Resale,
               Fast,Great_Drive,Fuel_Saver,Customization,Good_Looking,Quick_Delivery, Financing]
        max_count = 0
        max_disease = ""
        for key, val in self.symptom_map.items():
            count = 0
            temp_list = eval(key)
            for j in range(0, len(lis)):
                if temp_list[j] == lis[j] and (lis[j] == "high" or lis[j] == "low" or lis[j] == "yes"):
                    count = count + 1
            if count > max_count:
                max_count = count
                max_disease = val
        if max_disease != "":
            self.if_not_matched(max_disease)