def get_wind_class(speed): #объявление функции
    if 1 <= speed <= 4: #только аргумент
        return "weak [1]"
    elif 5 <= speed <= 10:
        return "moderate [2]"
    elif 11 <= speed <= 18:
        return"strong [3]"
    elif speed >= 19:
        return "hurricane [4]"
print(get_wind_class(3)) #мы просим программу напечатать то, что в скобках