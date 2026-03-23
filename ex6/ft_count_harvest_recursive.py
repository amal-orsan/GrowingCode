def ft_count_harvest_recursive():
    cur_num = int(input("Days until harvest:   "))

    def helper(num):
        if num > cur_num:
            print("Harvest time!")
            return
        print(f"Day {num}")
        helper(num + 1)
    helper(1)
