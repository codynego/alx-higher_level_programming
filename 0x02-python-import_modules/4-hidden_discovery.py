#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import hidden_4

    for m in dir(hidden_4):
        if m[:1] != "__":
            print(m)
