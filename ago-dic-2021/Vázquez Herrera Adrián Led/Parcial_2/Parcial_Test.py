#CyPdS Parcial 2 pt1--Test

import builtins
from Parcial import *
import pytest

def test_code(mocker):
    Cases=[]
    f=open("Cases.txt",'r')
    aux=f.readlines()
    s=""
    for line in aux:
        if line[0]=='-':
            Cases.append(s)
            s=""
        else:
            s+=line
    f.close()
    
    Results=[]
    f=open("Results.txt",'r')
    aux=f.readlines()
    s=""
    for line in aux:
        if line[0]=='-':
            Results.append(s)
            s=""
        else:
            s+=line
    f.close()
    #Testing
    mocker.patch.object(builtins,'open', mocker.mock_open(read_data=Cases[0]))
    assert Results[0]==Promedios()
    mocker.patch.object(builtins,'open', mocker.mock_open(read_data=Cases[1]))
    assert Results[1]==Promedios()
    mocker.patch.object(builtins,'open', mocker.mock_open(read_data=Cases[2]))
    assert Results[2]==Promedios()
    mocker.patch.object(builtins,'open', mocker.mock_open(read_data=Cases[3]))
    assert Results[3]==Promedios()
    
    