from django.shortcuts import render
import random
import requests
# Create your views here.

def lotto(request):
    BASE_URL = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1'

    req_lotto = requests.get(BASE_URL)
    lotto_No = req_lotto.json()
    lotto_number = [lotto_No['drwtNo1'], lotto_No['drwtNo2'], lotto_No['drwtNo3'], lotto_No['drwtNo4'], lotto_No['drwtNo5'], lotto_No['drwtNo6']]
    bonus_number = lotto_No['bnusNo']
    cnt_1, cnt_2, cnt_3, cnt_4, cnt_5, cnt_0 = 0, 0, 0, 0, 0, 0
    
    for _ in range(1000):
        select_number = random.sample(range(1,46),6)
        cnt = 0
        cnt_bonus = 0
        for i in range(6):
            cnt += lotto_number.count(select_number[i])
            cnt_bonus += select_number.count(bonus_number)
        if cnt == 3:
            cnt_5 += 1
        elif cnt == 4:
            cnt_4 += 1
        elif cnt == 5 and cnt_bonus == 0:
            cnt_3 += 1
        elif cnt == 5 and cnt_bonus == 1:
            cnt_2 += 1
        elif cnt == 6:
            cnt_1 += 1
        else:
            cnt_0 += 1

    context = {
        'lotto_number' : lotto_number,
        'bonus_number' : bonus_number,
        'cnt_1' : cnt_1,
        'cnt_2' : cnt_2,
        'cnt_3' : cnt_3,
        'cnt_4' : cnt_4,
        'cnt_5' : cnt_5,
        'cnt_0' : cnt_0,
    }



    return render(request, 'pages/lotto.html', context)