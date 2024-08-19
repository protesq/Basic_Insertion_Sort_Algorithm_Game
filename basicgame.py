import random


def insertion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key
    return arr


def game():
    user_1 = input("Username 1: ")
    user_2 = input("Username 2: ")
    user_3 = input("Username 3: ")
    user_4 = input("Username 4: ")

    users = {}

    # Kullanıcılar için rastgele sayılar oluşturup, insertion sort ile sıralıyoruz
    for user in [user_1, user_2, user_3, user_4]:
        arr = [random.randint(1, 100) for _ in range(5)]
        random.shuffle(arr)  # Diziyi karıştır
        users[user] = insertion_sort(arr)  # Kullanıcı adı ile diziyi eşleştir

    user1_total = sum(users[user_1])
    user2_total = sum(users[user_2])
    user3_total = sum(users[user_3])
    user4_total = sum(users[user_4])

    total_list = [user1_total, user2_total, user3_total, user4_total]

    max_total = max(total_list)

    selection_player = input("Kullanıcı adınızı yazınız: ")

    if selection_player in users:
        users[selection_player] = insertion_sort(users[selection_player])
        print(users[selection_player])

    if max_total == user1_total:
        print(f"{user_1} kazandı! Toplam: {user1_total}")
    elif max_total == user2_total:
        print(f"{user_2} kazandı! Toplam: {user2_total}")
    elif max_total == user3_total:
        print(f"{user_3} kazandı! Toplam: {user3_total}")
    elif max_total == user4_total:
        print(f"{user_4} kazandı! Toplam: {user4_total}")

    if selection_player != user_1 and max_total == user1_total:
        print("Kaybettiniz!")
    elif selection_player != user_2 and max_total == user2_total:
        print("Kaybettiniz!")
    elif selection_player != user_3 and max_total == user3_total:
        print("Kaybettiniz!")
    elif selection_player != user_4 and max_total == user4_total:
        print("Kaybettiniz!")

    return users

if __name__ == '__main__':
    result = game()
    print(result)
