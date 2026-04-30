import sys


import pytest



from src.models import DecisionTree

def test_decision_tree():
    model=DecisionTree(max_depth=5)

   
    assert model.max_depth==5
    assert model.layers==4
