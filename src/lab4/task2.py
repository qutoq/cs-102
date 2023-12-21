class Respondent:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if isinstance(other, Respondent):
            return self.name == other.name and self.age == other.age
        return False

    def __repr__(self):
        return self.name + " " + str(self.age)


def group_respondents(respondents, age_groups):
    group_dict = {age_group: [] for age_group in age_groups}
    for respondent in respondents:
        for age_group in age_groups:
            if age_group[0] <= respondent.age <= age_group[1]:
                group_dict[age_group].append(respondent)
                break

    result = []
    for age_group in age_groups:
        if group_dict[age_group]:
            group_dict[age_group] = sorted(group_dict[age_group], key=lambda x: (-x.age, x.name))
            el = str(age_group[0]) + "-" + str(age_group[1]) + ": "
            el += ", ".join([i.name + " (" + str(i.age) + ")" for i in group_dict[age_group]])
            result.append(el)
    return result


def parse_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        respondents = []
        for line in file:
            line = line.strip()
            if line == "END":
                break
            name, age = line.split(",")
            respondent = Respondent(name, int(age))
            respondents.append(respondent)
    return respondents


def get_groups(input_val):
    group_values = [int(el) for el in input_val.split()]
    result = []
    left = 0
    for value in group_values:
        age_group = (left, value)
        result.append(age_group)
        left = value + 1
    result.append((left, 123))
    return result


if __name__ == "__main__":
    file_path = 'data/people.txt'

    groups = get_groups(input())
    respondents = parse_data(file_path)
    print(respondents)

    output = group_respondents(respondents, groups)
    for el in output:
        print(el)
