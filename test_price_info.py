import price_info as price

def test_total_cost_shopping():

    result = price.total_cost_shopping()
    assert(result == 46.75)

def test_cost_of_fruit():

    result = price.cost_of_fruits('watermelon',15)
    assert(result == 97.5)