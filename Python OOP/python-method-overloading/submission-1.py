class TextProcessor:
    # Implement method overloading for format_text method
    # def format_text(self, text1: str, text2:str = None) -> str:
    #     if text2 == None:
    #         return text1.upper()
    #     else:
    #         return text1 + text2
    def format_text(self, *args:str) -> str:
        res:str | None = ""
        if len(args) == 1:
            res = str(args[0]).upper()
        else:
            for arg in args:
                res += str(arg)
        return res



# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
