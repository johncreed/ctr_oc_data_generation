import sys

def get_PY(va):
    rf = open(va, 'r')
    sample = 0.0
    for line in rf:
        toks = line.strip().split()
        labels = toks[0].strip(',').split(',')
        for label in labels:
            item, click = label.split(':')
            label_cnt.setdefault(click, 0.0)
            label_cnt[click] += 1
            sample += 1
    print sample, label_cnt['0'], label_cnt['1']
    for key, val in label_cnt.iteritems():
        label_cnt[key] = val / sample
    return label_cnt

def get_YO(tr):
    rf = open(tr, 'r')
    max_u = 0.0
    max_i = 0.0
    for line in rf:
        toks = line.strip().split()
        labels = toks[0].strip(',').split(',')
        for label in labels:
            item, click = label.split(':')
            label_cnt.setdefault(click, 0.0)
            label_cnt[click] += 1
            max_i = max(max_i, int(item) + 1)
        max_u += 1
    print max_i, max_u
    for key, val in label_cnt.iteritems():
        label_cnt[key] = val / (max_i * max_u)


if __name__ == '__main__':
    va = sys.argv[1]
    tr = sys.argv[2]

    PY = get_PY(va)
    YO = get_YO(tr)

    for key, val in PY.iteritems():
        print( key, YO[key] / PY[key])