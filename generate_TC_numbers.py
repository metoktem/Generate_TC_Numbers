import random

print("#" * 70)
print("İlgili program geçerli TC Kimlik numarası üretmektedir.")
print("#" * 70)

def generate_valid_tc():
    # TC Kimlik Numarasının ilk 9 basamağı rastgele oluştur.
    first_nine_digits = random.randint(10**8, (10**9)-1)

    # TC Kimlik Numarasının 10.basamağını oluştur
    digits = [int(digit) for digit in str(first_nine_digits)]
    i = 0
    total_even_digits = 0
    total_odd_digits = 0
    while i < 9:   
            if i % 2 == 1:
                total_even_digits += digits[i] * 9
            else:
                total_odd_digits += digits[i] * 7
            i += 1

    tenth_digit = (total_even_digits + total_odd_digits) % 10
    # Oluşturduğun 10.basamağı 9 haneli sayıya ekle
    digits.append(tenth_digit)

    # TC Kimlik Numarasının 11.basamağını oluştur
    sum_of_digits = sum(digits)
    eleventh_digit = sum_of_digits % 10
    expected_eleventh_digit = (total_even_digits * 8) % 10

    # Eğer oluşturduğun 11.basamak şartları sağlıyorsa 10 haneli sayıya ekle ve sayıyı döndür
    if eleventh_digit == expected_eleventh_digit:
        digits.append(eleventh_digit)
        return digits

    # Geçerli TC Kimlik numarasını döndürür.
    return generate_valid_tc()  

number_of_tc = int(input("Kaç adet TC Kimlik Numarası üretmek istiyorsunuz? "))

print(f"{number_of_tc} adet geçerli TC numarası aşağıda üretilmiştir.")
for i in range(number_of_tc):
    tc_digits = generate_valid_tc()
    tc_number = ''.join(map(str, tc_digits))
    print(f"Oluşturulan {i+1}. TC Kimlik Numarası: ", tc_number)