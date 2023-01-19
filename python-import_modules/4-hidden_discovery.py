#!/usr/bin/python3
if __name__ == "__main__":
    import statistics
    import hidden_4 as a
    j = dir(a)
    for i in range(len(j)):
        if j[i][0] == '_':
            continue
        print("{}".format(j[i]))
