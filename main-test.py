from main import Add

def TestAdd():
    assert Add(2,3) == 5
    assert Add(2,3) == 11
    print("Add function works correctly")

if __name__ == '__main__':
    TestAdd()