from abc import ABC, abstractmethod
import pytest
from mission import Car, ElectricCar, Vehicle, Chargablemixin, SlottedVehicle

def test_car():
    car = Car("Honda", "City", 2025)

    assert car.brand == "Honda"
    assert car.model == "City"
    assert car.year == 2025
    assert car.start() == "Car started."

def test_electric_car():
    car = ElectricCar("Tesla", "Cybertruck", 2025, 96)

    assert car.brand == "Tesla"
    assert car.model == "Cybertruck"
    assert car.year == 2025
    assert car.battery == 96
    assert car.start() == "Electric car started."
    assert car.charge() == "Charging: 96 kwH Battery."

def test_vehicle_is_abstract():
    with pytest.raises(TypeError):
        Vehicle("Toyota", "Corolla", 2025)

def test_electric_car_mro():
    assert ElectricCar.__mro__ == (
        ElectricCar,
        Vehicle,
        ABC,
        Chargablemixin,
        object
    )

def test_electric_car_type():
    car = ElectricCar("Tesla", "Cybertruck", 2025, 96)

    assert isinstance(car, ElectricCar)
    assert isinstance(car, Vehicle)
    assert isinstance(car, Chargablemixin)

    assert type(car) is ElectricCar
    assert type(car) is not Vehicle
    assert type(car) is not Chargablemixin

def test_slotted_vehicle():
    vehicle = SlottedVehicle("Toyota", "Corolla", 2025)

    assert vehicle.brand == "Toyota"
    assert vehicle.model == "Corolla"
    assert vehicle.year == 2025

    with pytest.raises(AttributeError):
        vehicle.color = "red"

def test_super_initialization():
    car = ElectricCar("Tesla", "Cybertruck", 2025, 96)

    # Vehicle.__init__() initialized these
    assert car.brand == "Tesla"
    assert car.model == "Cybertruck"
    assert car.year == 2025

    # Chargablemixin.__init__() initialized this
    assert car.battery == 96