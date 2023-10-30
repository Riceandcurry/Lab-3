import Lab2.pythonProject.bmi as bmi
def test_bmi_normal_weight():
    input_value_weight = 54
    input_value_height = 1.68
    test_result = 0
    result = bmi.calculate_bmi(input_value_height, input_value_weight)
    assert (result == test_result)
def test_bmi_over_weight():
    input_value_weight = 54
    input_value_height = 1.68
    result = bmi.calculate_bmi(input_value_height, input_value_weight)


def test_bmi_under_weight():