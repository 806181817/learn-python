#!/usr/bin/env python
# -*-  coding=utf-8 -*-

big_months = [1, 3, 5, 7, 8, 10, 12]
small_months = [4, 6, 9, 11]


def is_between(val, lower, upper):
    return lower <= val <= upper


def is_leap_year(yy):
    if yy % 4 > 0:
        return False
    elif yy % 100 == 0 and yy % 400 > 0:
        return False
    else:
        return True


def is_valid(card_num):
    if len(card_num) != 15 and len(card_num) != 18:
        print("身份证位数不符合，身份证位数为15或18位！")
        return False

    if len(card_num) == 15:
        if not card_num.isdigit():
            print("15位身份证号里包含非法字符，请重新检查！")
            return False

        yy = card_num[6:7]
        mm = int(card_num[8:10])
        dd = int(card_num[10:12])

        if is_between(mm, 1, 11):
            if mm in big_months:
                max_day = 31
            elif mm in small_months:
                max_day = 30
            else:
                if is_leap_year(int('19' + yy)):
                    max_day = 29
                else:
                    max_day = 28
        else:
            print("15位身份证有月份格式不正确，请检查第9和10位！")
            return False

        if not is_between(dd, 1, max_day):
            print("日期超出当月限制！")
            return False
        else:
            return True

    if len(card_num) == 18:
        mask_dic = {1: 7, 2: 9, 3: 10, 4: 5, 5: 8, 6: 4, 7: 2,
                    8: 1, 9: 6, 10: 3, 11: 7, 12: 9, 13: 10,
                    14: 5, 15: 8, 16: 4, 17: 2}
        check_code = {0: '1', 1: '0', 2: 'X', 3: '9', 4: '8', 5: '7', 6: '6', 7: '5', 8: '4', 9: '3', 10: '2'}

        if not ((card_num[-1].upper() == 'X' and card_num[:-1].isdigit()) or card_num.isdigit()):
            print("18位身份证号里包含非法字符，请重新检查！")
            return False

        yy = int(card_num[6:10])
        mm = int(card_num[10:12])
        dd = int(card_num[12:14])

        if not is_between(yy, 1900, 2200):
            print("身份证年限超限！")
            return False

        if is_between(mm, 1, 11):
            if mm in big_months:
                max_day = 31
            elif mm in small_months:
                max_day = 30
            else:
                if is_leap_year(yy):
                    max_day = 29
                else:
                    max_day = 28
        else:
            print("18位身份证有月份格式不正确，请检查第9和10位！")
            return False

        if not is_between(dd, 1, max_day):
            print("日期超出当月限制！")
            return False

        total = 0
        for i in range(len(card_num) - 1):
            total += int(card_num[i]) * mask_dic.get(i + 1)
        if check_code.get(total % 11).upper() != card_num[-1]:
            print("输入的身份证校验失败，身份证号非法！！")
            return False
        else:
            return True


if __name__ == '__main__':
    number = '130321198902310612'
    if is_valid(number.strip()):
        print("恭喜身份证是合法的！")
        exit()
