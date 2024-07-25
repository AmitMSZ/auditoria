import pytest
from main import ingresardatos, modificardatos, ingresoUsuarios, clientes, usuarios, idcliente, idusuario

def mock_input(prompt, value):
    return value

def test_ingresardatos(monkeypatch):
    global idcliente
    idcliente = 0
    inputs = iter(["123456789", "Juan", "Perez", "Calle Falsa 123", 123456789, "juan.perez@example.com", "101", "50000"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    ingresardatos()

    assert 0 in clientes
    assert clientes[0][2] == "Juan"
    assert clientes[0][3] == "Perez"
    assert clientes[0][7] == "101"
    assert clientes[0][8] == "50000"

def test_modificardatos(monkeypatch):
    global idcliente
    idcliente = 1
    clientes[idcliente] = [idcliente, "123456780", "Juan", "Perez", "Calle Falsa 123", 123456789, "juan.perez@example.com", "101", "50000", "0"]
    
    inputs = iter(["1", "si", "Carlos", "no", "no", "no", "no", "no", "no"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    modificardatos()

    assert clientes[1][2] == "Carlos"  # Nombre modificado

def test_ingresoUsuarios(monkeypatch):
    global idusuario
    idusuario = 0
    inputs = iter(["carlos123", "password123", "Carlos", "Lopez", "carlos.lopez@example.com"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    ingresoUsuarios()

    assert "carlos123" in usuarios
    assert usuarios["carlos123"][3] == "Carlos"
    assert usuarios["carlos123"][4] == "Lopez"
