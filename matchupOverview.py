import requests
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import selenium
import getpass


class Team:
    def __init__(self):
        self.teamName = None
        self.FGMA = None
        self.FG = 0
        self.FTMA = None
        self.FT = 0
        self.ThreePTM = 0
        self.PTS = 0
        self.REB = 0
        self.AST = 0
        self.ST = 0
        self.BLK = 0
        self.TO = 0
        self.score = [0, 0, 0]


def calStat(team1, team2):
    score = [0, 0, 0]

    if team1.FG > team2.FG:
        score[0] += 1
    elif team1.FG < team2.FG:
        score[1] += 1
    else:
        score[2] += 1

    if team1.FT > team2.FT:
        score[0] += 1
    elif team1.FT < team2.FT:
        score[1] += 1
    else:
        score[2] += 1

    if team1.ThreePTM > team2.ThreePTM:
        score[0] += 1
    elif team1.ThreePTM < team2.ThreePTM:
        score[1] += 1
    else:
        score[2] += 1

    if team1.PTS > team2.PTS:
        score[0] += 1
    elif team1.PTS < team2.PTS:
        score[1] += 1
    else:
        score[2] += 1

    if team1.REB > team2.REB:
        score[0] += 1
    elif team1.REB < team2.REB:
        score[1] += 1
    else:
        score[2] += 1

    if team1.AST > team2.AST:
        score[0] += 1
    elif team1.AST < team2.AST:
        score[1] += 1
    else:
        score[2] += 1

    if team1.ST > team2.ST:
        score[0] += 1
    elif team1.ST < team2.ST:
        score[1] += 1
    else:
        score[2] += 1

    if team1.BLK > team2.BLK:
        score[0] += 1
    elif team1.BLK < team2.BLK:
        score[1] += 1
    else:
        score[2] += 1

    if team1.TO < team2.TO:
        score[0] += 1
    elif team1.TO > team2.TO:
        score[1] += 1
    else:
        score[2] += 1

    return score


def calAdvStat(teams):
    selectedTeam = teams[0]
    seperateStats = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    avgStats = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    for team in teams[1:]:
        if selectedTeam.FG > team.FG:
            seperateStats[0] += 1
        if selectedTeam.FT > team.FT:
            seperateStats[1] += 1
        if selectedTeam.ThreePTM > team.ThreePTM:
            seperateStats[2] += 1
        if selectedTeam.PTS > team.PTS:
            seperateStats[3] += 1
        if selectedTeam.REB > team.REB:
            seperateStats[4] += 1
        if selectedTeam.AST > team.AST:
            seperateStats[5] += 1
        if selectedTeam.ST > team.ST:
            seperateStats[6] += 1
        if selectedTeam.BLK > team.BLK:
            seperateStats[7] += 1
        if selectedTeam.TO < team.TO:
            seperateStats[8] += 1
        avgStats[0] += team.FG
        avgStats[1] += team.FT
        avgStats[2] += team.ThreePTM
        avgStats[3] += team.PTS
        avgStats[4] += team.REB
        avgStats[5] += team.AST
        avgStats[6] += team.ST
        avgStats[7] += team.BLK
        avgStats[8] += team.TO
    for i in range(9):
        avgStats[i] /= leagueSize
    return seperateStats, avgStats


def printOverview(teams):
    selectedTeam = teams[0]
    for team in teams[1:]:
        print("Team:\t" + selectedTeam.teamName +
              " vs " + team.teamName)
        score = calStat(selectedTeam, team)
        print("Score:\t", score[0], "\t: ", score[1])

        if selectedTeam.FG > team.FG:
            print("\033[32m", end="")
        else:
            print("\033[31m", end="")
        print("FGM/A:\t", selectedTeam.FGMA, " : ", team.FGMA)
        print("FG:\t", selectedTeam.FG, "\t: ", team.FG, end="")
        print("\033[0m")

        if selectedTeam.FT > team.FT:
            print("\033[32m", end="")
        else:
            print("\033[31m", end="")
        print("FTM/A:\t", selectedTeam.FTMA, " : ", team.FTMA)
        print("FT:\t", selectedTeam.FT, "\t: ", team.FT, end="")
        print("\033[0m")

        if selectedTeam.ThreePTM > team.ThreePTM:
            print("\033[32m", end="")
        else:
            print("\033[31m", end="")
        print("3PTS:\t", selectedTeam.ThreePTM, "\t: ", team.ThreePTM, end="")
        print("\033[0m")

        if selectedTeam.PTS > team.PTS:
            print("\033[32m", end="")
        else:
            print("\033[31m", end="")
        print("PTS:\t", selectedTeam.PTS, "\t: ", team.PTS, end="")
        print("\033[0m")

        if selectedTeam.REB > team.REB:
            print("\033[32m", end="")
        else:
            print("\033[31m", end="")
        print("REB:\t", selectedTeam.REB, "\t: ", team.REB, end="")
        print("\033[0m")

        if selectedTeam.AST > team.AST:
            print("\033[32m", end="")
        else:
            print("\033[31m", end="")
        print("AST:\t", selectedTeam.AST, "\t: ", team.AST, end="")
        print("\033[0m")

        if selectedTeam.ST > team.ST:
            print("\033[32m", end="")
        else:
            print("\033[31m", end="")
        print("ST:\t", selectedTeam.ST, "\t: ", team.ST, end="")
        print("\033[0m")

        if selectedTeam.BLK > team.BLK:
            print("\033[32m", end="")
        else:
            print("\033[31m", end="")
        print("BLK:\t", selectedTeam.BLK, "\t: ", team.BLK, end="")
        print("\033[0m")

        if selectedTeam.TO < team.TO:
            print("\033[32m", end="")
        else:
            print("\033[31m", end="")
        print("TO:\t", selectedTeam.TO, "\t: ", team.TO, end="")
        print("\033[0m")

        print()

    sepStats, avgStats = calAdvStat(teams)
    print("---------Speerate Stats--------")
    print("FG:\t", sepStats[0], "/", leagueSize)
    print("FT:\t", sepStats[1], "/", leagueSize)
    print("3Pts:\t", sepStats[2], "/", leagueSize)
    print("Pts:\t", sepStats[3], "/", leagueSize)
    print("REB:\t", sepStats[4], "/", leagueSize)
    print("AST:\t", sepStats[5], "/", leagueSize)
    print("ST:\t", sepStats[6], "/", leagueSize)
    print("BLK:\t", sepStats[7], "/", leagueSize)
    print("TO:\t", sepStats[8], "/", leagueSize)
    print()
    print("--------League average--------")
    print("FG:\t{0:.3f}({1:.3f})".format(avgStats[0], selectedTeam.FG))
    print("FT:\t{0:.3f}({1:.3f})".format(avgStats[1], selectedTeam.FT))
    print("3Pts:\t{0:.3f}({1:d})".format(avgStats[2], selectedTeam.ThreePTM))
    print("Pts:\t{0:.3f}({1:d})".format(avgStats[3], selectedTeam.PTS))
    print("REB:\t{0:.3f}({1:d})".format(avgStats[4], selectedTeam.REB))
    print("AST:\t{0:.3f}({1:d})".format(avgStats[5], selectedTeam.AST))
    print("ST:\t{0:.3f}({1:d})".format(avgStats[6], selectedTeam.ST))
    print("BLK:\t{0:.3f}({1:d})".format(avgStats[7], selectedTeam.BLK))
    print("TO:\t{0:.3f}({1:d})".format(avgStats[8], selectedTeam.TO))


def login():
    username = input("Username: ")
    password = getpass.getpass()
    week = input("Week: ")

    Chrome_driver_path = './chromedriver-1'
    web = 'https://login.yahoo.com/config/login?.src=fantasy&specId=usernameRegWithName&.intl=us&.lang=en-US&.done=https://basketball.fantasysports.yahoo.com/'  # Yahoo Fantasy登入頁面
    chrome_options = webdriver.ChromeOptions()
    # 建議可以點選F12看request header的項目
    chrome_options.add_argument(
        'User-Agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"')
    # chrome_options.add_argument('--headless')

    driver = webdriver.Chrome(executable_path=Chrome_driver_path,
                              chrome_options=chrome_options)
    # driver.maximize_window()  # 最大化視窗，因為我發現某些情況下，較小的視窗會導致往下移動的JS沒有辦法執行。

    driver.get(web)  # 開始進入登入頁面

    elem_user = driver.find_element_by_name('username')  # 找到填入帳號的空格
    elem_user.clear()
    elem_user.send_keys(username)  # 填入帳號
    elem_next = driver.find_element_by_id('login-signin')  # 找到確認按鈕
    elem_next.click()  # 點擊確認
    time.sleep(1)

    elem_pass = driver.find_element_by_id('login-passwd')  # 找到填入密碼的空格
    elem_pass.send_keys(password)  # 填入密碼
    elem_signin = driver.find_element_by_id('login-signin')  # 找到確認按鈕
    elem_signin.click()  # 點擊確認
    time.sleep(1)
    return driver, week


def getMatch(driver, week):
    web2 = 'https://basketball.fantasysports.yahoo.com/nba/43003/matchup?week=' + week
    driver.get(web2)

    for i in range(0, 2):
        # 到達網頁後要滾輪持續往下滑，才會出現matchup分數欄位
        driver.execute_script(
            'window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(1)

    # 把撈到的頁面丟給BeautifulSoup解析
    soup = BeautifulSoup(driver.page_source, "html.parser")
    pages = soup.find_all('div', class_='Ta-c Js-hidden')  # 找網址
    names = soup.find_all('a', class_='F-link')  # 找隊名
    return soup, pages, names


def buildStat(rawStat, names2):
    teams = []
    for i in range(leagueSize):
        tmp = Team()
        tmp.teamName = str(names2[i])
        tmp.FGMA = rawStat[0 + i * 12]
        tmp.FG = float(rawStat[1 + i * 12])
        tmp.FTMA = rawStat[2 + i * 12]
        tmp.FT = float(rawStat[3 + i * 12])
        tmp.ThreePTM = int(rawStat[4 + i * 12])
        tmp.PTS = int(rawStat[5 + i * 12])
        tmp.REB = int(rawStat[6 + i * 12])
        tmp.AST = int(rawStat[7 + i * 12])
        tmp.ST = int(rawStat[8 + i * 12])
        tmp.BLK = int(rawStat[9 + i * 12])
        tmp.TO = int(rawStat[10 + i * 12])
        teams.append(tmp)
    return teams


def getLink(pages):
    target_pages = []
    for p in pages:
        target_pages.append(p.a['href'])

    target_pages2 = []
    for p2 in target_pages:
        target_pages2.append('https://basketball.fantasysports.yahoo.com'+p2)
    return target_pages2


leagueSize = 14


def main():

    driver, week = login()
    soup, pages, names = getMatch(driver, week)

    # preprocess names
    names2 = []
    for n in names[2:leagueSize + 2]:
        names2.append(n.text)
    names = names2

    # 搞定對戰連結
    target_pages = getLink(pages)

    # 撈取對戰分數，左半部與右半部各抓一次。
    lg1 = []
    lg2 = []
    index = 0
    for p3 in target_pages:
        index += 1
        driver.get(p3)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        score1 = soup.find_all('td', class_='Ta-c')
        time.sleep(1)

        for i in score1[0: 12]:
            lg1.append(i.text)

        for i in score1[12: 2 * 12]:
            lg2.append(i.text)
        print("Retreiving data({0:d}/7)......".format(index))
    lg3 = []
    for i in range(7):
        for j in range(12):
            lg3.append(lg1[j + 12 * i])
        for j in range(12):
            lg3.append(lg2[j + 12 * i])

    teams = buildStat(lg3, names)
    printOverview(teams)


main()
