def main(lines):
    total = 0

    for line in lines:
        nums = ""
        last_seen_digit = ""
        for c in line:
            if c.isdigit():
                last_seen_digit = c
                if len(nums) == 0:
                    nums += last_seen_digit
        nums += last_seen_digit
        total += int(nums)
        # print(f"#{line=} #{last_seen_digit=} #{nums=}")

    print(total)


with open('input1', 'r') as file:
    lines = file.readlines()
    lines = [s.strip() for s in lines]
    main(lines) 

# - [ ] add hyperfine to test a few versions
