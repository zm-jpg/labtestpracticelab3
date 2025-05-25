import price_info as price

def test_total_cost_shopping():
    result=price.total_cost_shopping()
    expected=46.75
    assert(result==expected)


def test_cost_of_fruit():
    result=price.cost_of_fruits("orange", 100)
    expected=140
    assert(result==expected)
