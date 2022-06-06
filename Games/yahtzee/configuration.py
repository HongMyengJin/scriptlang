from dice import *

class Configuration:

    configs = [
        "Categoty", "Ones", "Twos", "threes", "Fours", "Fives", "Sixes",
        "Upper Scores", "Upper Bonus(35)",
        "3 of a kind", "4 of a kind", "Full House(25)",
        "Small Straight(30)", "Large Straight(40)", "Yahtzee(50)", "Chance",
        "Lower Scores", "Total"
    ]

    @staticmethod
    def getConfigs():       # 정적 메소드 (객체 없이 사용 가능)
        return Configuration.configs

    # row에 따라 주사위 점수를 계산하여 반환. 
    # 예를 들어, row가 0이면 "Ones"가, 2이면 "Threes"가 채점되어야 함을 의미. 
    # row가 득점위치가 아닌 곳(즉, UpperScore, UpperBonus, LowerScore, Total 등)을 나타내는 경우 -1을 반환.
    @staticmethod
    def score(row, dices):       # 정적 메소드 (객체 없이 사용 가능)
        # TODO: 구현
        dicelist = []
        for n in dices:
            dicelist.append(n.getRoll())
        if (row >= 0 and row <= 6):
            return Configuration.scoreUpper(dicelist, row + 1)
        elif (row == 8):
            return Configuration.scoreThreeOfAKind(dicelist)
        elif (row == 9):
            return Configuration.scoreFourOfAKind(dicelist)
        elif (row == 10):
            return Configuration.scoreFullHouse(dicelist)
        elif (row == 11):
            return Configuration.scoreSmallStraight(dicelist)
        elif (row == 12):
            return Configuration.scoreLargeStraight(dicelist)
        elif (row == 13):
            return Configuration.scoreYahtzee(dicelist)
        elif (row == 14):
            return Configuration.sumDie(dicelist)

    def scoreUpper(d, num):  # 정적 메소드: 객체생성 없이 사용 가능

        # Upper Section 구성 (Ones, Twos, Threes, ...)에 대해 주사위 점수를 매 깁니다. 예를 들어,
        # num이 1이면 "Ones"구성의 주사위 점수를 반환합니다.

        return d.count(num)*num

    def scoreThreeOfAKind(d):
        for i in range(len(d)+1):
            if d.count(i+1) >= 3:
                return sum(d)
        return False

    def scoreFourOfAKind(d):
        for i in range(len(d)+1):
            if d.count(i+1) >= 4:
                return sum(d)
        return False

    def scoreFullHouse(d):
        for i in range(len(d)+1):
            for j in range(len(d)):
                if d.count(i+1) == 2 and d.count(j+1) == 3:
                    return 25
                if d.count(i+1) == 3 and d.count(j+1) == 2:
                    return 25
        return False

    def scoreSmallStraight(d):
        # 1 2 3 4 혹은 2 3 4 5 혹은 3 4 5 6 검사
        # 1 2 2 3 4, 1 2 3 4 6, 1 3 4 5 6, 2 3 4 4 5
        if (1 in d and 2 in d and 3 in d and 4 in d) or (2 in d and 3 in d and 4 in d and 5 in d) or (3 in d and 4 in d and 5 in d and 6 in d):
            return 30
        return False

    def scoreLargeStraight(d):

        # 1 2 3 4 5 혹은 2 3 4 5 6 검사
        if (1 in d and 2 in d and 3 in d and 4 in d and 5 in d) or (2 in d and 3 in d and 4 in d and 5 in d and 6 in d) :
            return 40
        return False

    def scoreYahtzee(d):
        for i in range(len(d)+1):
            if d.count(i+1) == 5:
                print( d.count(i+1))
                return 50
        return False

    def sumDie(d):
        return sum(d)

