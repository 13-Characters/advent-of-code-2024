def part_1():
    raw_text = open("input.txt").readlines()
    rules = [line.removesuffix("\n").split("|") for line in raw_text if "|" in line]
    orderings = [line.removesuffix("\n").split(",") for line in raw_text if "," in line]

    valid_orderings = orderings.copy()
    for ordering in orderings:
        for rule in rules:
            if rule[0] in ordering and rule[1] in ordering and ordering.index(rule[0]) > ordering.index(rule[1]):
                valid_orderings.remove(ordering)
                break
    print(sum([int(ordering[len(ordering)//2]) for ordering in valid_orderings]))
def part_2():
    # I considered using functools.cmp_to_key for this but decided not to
    raw_text = open("input.txt").readlines()
    rules = [line.removesuffix("\n").split("|") for line in raw_text if "|" in line]
    orderings = [line.removesuffix("\n").split(",") for line in raw_text if "," in line]

    valid_orderings = orderings.copy()
    def swap(ordering, rule_0, rule_1):
        index_0 = ordering.index(rule_0)
        index_1 = ordering.index(rule_1)
        ordering[index_0] = rule_1
        ordering[index_1] = rule_0
        return ordering

    for ordering in orderings:
        for rule in rules:
            if rule[0] in ordering and rule[1] in ordering and ordering.index(rule[0]) > ordering.index(rule[1]):
                swap(ordering, rule[0], rule[1])
    print(sum([int(ordering[len(ordering) // 2]) for ordering in valid_orderings]))

part_1()
part_2()
