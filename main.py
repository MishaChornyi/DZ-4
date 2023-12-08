import random

class NumberEncryptor:
    def __init__(self, number):
        self._number = number

    def _perform_random_operation(self):
        operation = random.choice(["add", "multiply"])

        if operation == "add":
            return self._number + random.randint(1, 10)
        elif operation == "multiply":
            return self._number * random.randint(2, 5)

    def encrypt(self):
        result = self._perform_random_operation()
        return result

    def decrypt(self, encrypted_result):
        return encrypted_result - self._number

original_number = 42

encryptor = NumberEncryptor(original_number)

encrypted_result = encryptor.encrypt()

print(f"Зашифрований результат: {encrypted_result}")

decrypted_result = encryptor.decrypt(encrypted_result)

print(f"Розшифрований результат: {decrypted_result}")
