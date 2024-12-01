print(f"♔   {'\u00A9'}   ♕ 	 a a  ♖ 	♗ 	♘ 	♙ 	♚ 	♛ 	♜ 	♝ 	♞ 	♟")
print("\033[32mThis is red font.\033[0m")
print("\033[41m Highlighted Red Text\033[0m")
print("\033[30;43m Grey text on a Highlighted Yellow background \033[0m")

# print("\033[00m00: nothing\033[0m")
# print("\033[01m01: bold?\033[0m")
# print("\033[02m02: gray\033[0m")
# print("\033[03m03: italic\033[0m")
# print("\033[04m04: underline\033[0m")
# print("\033[05m05-06: nothing\033[0m")
print("\n\033[07m07: inverted\033[0m")
# print("\033[08m08: invisible?\033[0m")
# print("\033[09m09: strike through\033[0m")
# print("\033[10m10-20: nothing\033[0m")
# print("\033[21m21: double underline\033[0m")
# print("\033[22m22-29: nothing\033[0m")
# print("\033[30m30: gray\033[0m")
# print("\033[31m31: red\033[0m")
# print("\033[32m32: green\033[0m")
# print("\033[33m33: yellow\033[0m")
# print("\033[34m34: blue\033[0m")
# print("\033[35m35: magenta\033[0m")
# print("\033[36m36: cyan\033[0m")
# print("\033[37m37+: nothing\033[0m")


def esc(code):
    return f'\033[{code}m'
a = f'this is {esc('31')} really {esc(0)} important'
print(a)
print('this is ', esc('07'), 'really', esc(0), ' important', sep='')