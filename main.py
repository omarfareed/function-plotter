from validator import Validator
if __name__ == "__main__":
    validator = Validator()
    print(validator.validate("x ^ 2 + 5"))
    print(validator.validate("x ^ 2 + "))
