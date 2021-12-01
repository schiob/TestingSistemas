#Práctica 3. Testeo

from P4_Main import calc_prom
import pytest

def test_calc_prom(mocker):
    mocker.patch('P4_Main.Get_Data', return_value=[10,10,5,7])
    assert 8 == calc_prom()
