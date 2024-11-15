#CHARIN STEFANY
#065002400015

def ordinal_suffix(number):
    if 11 <= number % 100 <= 13:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(number % 10, "th")
    return f"{number}, '{suffix}'"

print("Ordinal Number")
print("ketik 0 untuk menghentikan program")

while True:
    number = int(input("masukkan angka: "))  
    if number == 0:                         
        print("(0, 'th')")
        print("terima kasih telah menggunakan program saya")
        break
    print(f"({ordinal_suffix(number)}")