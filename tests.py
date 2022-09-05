from app.py import sector, eclipse, paralelogramo

def test_sector_1():
    assert sector(5,45) == 9.817477042468104
def test_sector_2():
    assert sector(7.5, 90) == 44.178646691106465

def test_eclipse_1():
    assert eclipse(5,2) == 31.41592653589793
def test_eclipse_2():
    assert eclipse(8.5,3.1) == 82.78096642209105

def test_paralelogramo_1():
    assert paralelogramo(7.2,4.6) == 33.12
def test_paralelogramo_2():
    assert paralelogramo(5.3,2.5) == 13.25      
