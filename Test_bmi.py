import Lab2.bmi as BMI

def test_bmi_normal():
    assert(BMI.calculate_bmi(1.65, 60)==0)


def test_bmi_over():
    assert(BMI.calculate_bmi(1.65, 70)==0)


def test_bmi_under():
    assert(BMI.calculate_bmi(1.65, 45)==0)

