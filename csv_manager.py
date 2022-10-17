class CsvManager:
    __file_name: str = ""
    __is_valid: bool = False

    def __init__(self, file_name):
        self.file_name = file_name
        self.is_valid = True

    def get_file(self) -> str:
        return self.file_name

    def valid(self) -> bool:
        return self.is_valid
