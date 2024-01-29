#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    for secret in dir(hidden_4):
        if secret[0] != "_":
            print(secret)
