import pyautogui
import time

time.sleep(5)

x=1
y=0
smokingStatistics = ['Here is some statistics on smoking you can read up on while I sleep! SEE YOU LATER NERDSSSSS!!! See you on youtube XDDD!!!','https://www.thetruth.com/the-facts?&cid=VAP_SEARCH_GOOGLEGRANTS_NONBRAND&gclid=CjwKCAjw8pH3BRAXEiwA1pvMsRE2kASGLzWbhrz2iOfh7zhRIJClkHaWqEinParHuXcsM-v-IEDHphoCUf0QAvD_BwE&gclsrc=aw.ds','https://www.centeronaddiction.org/?gclid=CjwKCAjw8pH3BRAXEiwA1pvMsU1WjVG3Cyvfq-x4C5jdFyxJjWrreH4_aUvCAOOxlBH2pVOy2wAsxhoCTW0QAvD_BwE','https://www.cdc.gov/tobacco/data_statistics/fact_sheets/fast_facts/index.htm#:~:text=Cigarette%20smoking%20is%20responsible%20for,or%201%2C300%20deaths%20every%20day.&text=On%20average%2C%20smokers%20die%2010%20years%20earlier%20than%20nonsmokers.','https://www.cdc.gov/tobacco/data_statistics/fact_sheets/adult_data/cig_smoking/index.htm','https://www.verywellmind.com/facts-and-statistics-about-cigarette-smoking-2825328','https://ourworldindata.org/smoking','https://www.who.int/news-room/fact-sheets/detail/tobacco','https://ash.org/programs/tobacco-statistics-facts/','https://www.statista.com/topics/1600/smoking/','https://www.lung.org/research/trends-in-lung-disease/tobacco-trends-brief/overall-tobacco-trends','https://en.wikipedia.org/wiki/Prevalence_of_tobacco_use','https://www.swedish.org/classes-and-resources/smoking-cessation/smoking-statistics','Like and subscribe :D https://www.youtube.com/channel/UCtdIELIZlRLJqrKp6vTa50g?view_as=subscriber']

while x != 0:
    pyautogui.click(700,700)
    pyautogui.scroll(-1000)
    time.sleep(.5)
    pyautogui.click(800,700)
    if(y > len(smokingStatistics) - 1):
        y = 0
    if(y <= len(smokingStatistics)):
        pyautogui.write(smokingStatistics[y]+'\n')
        y = y + 1
    time.sleep(30)
