import math
import sys
from collections import defaultdict


class Calculator:
    doc = """***
Справочник по командам
stop - завершение работы 
doc - справка
принимаются стандартные операции в python
можно использовать однобуквенные переменные
и менять их значение: a = 5 ; a * 2 -> 10
e и p уже используется
если переменная не была задана, то её значение 0.0
vars - список заданных переменных
***"""
    oper = "()+-*/%=. "
    vars = defaultdict(float)
    vars["p"] = math.pi
    vars["e"] = math.e

    def solve(self, formula):
        status = self.check(formula)
        if status != "OK" or status != "OK":
            return status
        formula = self.reformat(formula)
        if "=" in formula:
            return self.if_eq(formula)
        elif formula == "":
            pass
        else:
            try:
                return eval(formula, {"vars": self.vars})
            except Exception as err:
                return err

    def if_eq(self, formula):
        if not (len(formula) > 9 and formula[9] == "="):
            return "Знак = не на своём месте"
        elif formula[:4] != "vars":
            return formula[:4]
        else:
            element = formula[6]
            try:
                result = eval(formula[10:], {"vars": self.vars})
                self.vars[element] = result
                return result
            except Exception as err:
                return err

    def reformat(self, formula) -> str:
        result = ""
        for elemnt in formula:
            if elemnt.isalpha():
                result += "vars['" + elemnt + "']"
            else:
                result += elemnt
        return result

    def check(self, formula) -> str:
        if len(formula) > 100:
            return "Слишком длинное выражение"
        if formula.isspace():
            return "Неккоректное выражение"

        only_letters = ""
        cnt = 0
        for element in formula:
            cnt += element.count("=")
            if cnt > 1:
                return "В выражении может быть только 1 знак ="
            res = self.check_symbol(element)
            if len(res) > 1:
                return res
            only_letters += res

        for element in only_letters.split():
            if len(element) > 1:
                return "Длина переменых должна быть равна 1"

        return "OK"

    def check_symbol(self, symbol) -> str:
        if symbol.isdigit() or symbol in self.oper:
            return " "
        if symbol.isalpha():
            return symbol
        return "В вашей формуле есть неккоректные символы"

    def run(self):
        print("показать справку - doc")
        while True:
            formula = input("\nВведите команды:\n")
            formula = formula.lower().replace(" ", "")
            if "stop" in formula or "стоп" in formula:
                self.stop()
            elif formula == "doc":
                print(self.doc)
            elif formula == "vars":
                print(self.vars.items())
            else:
                print(self.solve(formula))

    def stop(self):
        print("\nДо встречи")
        sys.exit(0)


if __name__ == "__main__":
    my_calc = Calculator()
    try:
        my_calc.run()
    except KeyboardInterrupt:
        my_calc.stop()
    except Exception as err:
        print("oops")
        print(err)
