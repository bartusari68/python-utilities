def mm_to_m(mm):
    return mm / 1000


def cm_to_m(cm):
    return cm / 100


def m_to_mm(m):
    return m * 1000


def m_to_cm(m):
    return m * 100


if __name__ == "__main__":
    print("1000 mm =", mm_to_m(1000), "m")
    print("15.24 cm =", cm_to_m(15.24), "m")
    print("2 m =", m_to_mm(2), "mm")
    print("2 m =", m_to_cm(2), "cm")
