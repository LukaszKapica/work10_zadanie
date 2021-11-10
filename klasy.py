class FileHandler:
    def __init__(self, file_path_read, file_path_write=None):
        self.history = []
        self.file_path_read = file_path_read
        if file_path_write:
            self.file_path_write = file_path_write
        else:
            file_path_write = file_path_read

    def read_history(self):
        with open(self.file_path_read) as file:
            for line in file:
                line = line.rstrip()
                komenda = [line]
                if line == 'stop':
                    break
                if line == 'saldo':
                    value = int(file.readline().rstrip())
                    comment = file.readline().rstrip()
                    komenda.extend([value, comment])
                if line in ['zakup', 'sprzedaz']:
                    product_name = file.readline().rstrip()
                    product_price = int(file.readline().rstrip())
                    product_value = int(file.readline().rstrip())
                    komenda.extend([product_name, product_price, product_value])
                self.history.append(komenda)

    def write_history(self):
        with open(self.file_path_write, 'w') as file:
            for komenda in self.history:
                for element in komenda:
                    file.write(str(element) + '\n')
            file.write('stop')
